import pickle as pkl
import pacman
import util, layout
from learningAgents import GeneticAgent
from featureExtractors import AdvancedExtractor
from graphicsDisplay import PacmanGraphics
from ghostAgents import *
from game import Agent
from layout import Layout
from pacman import *
from qlearningAgents import ApproximateQAgent

if __name__ == '__main__':
    #plays the best of each hyperparameter combination tested once
    hypes = ['cr_prob-0.4','cr_prob-0.8','cr_prob-0.15','cr_prob-0.99','cull_prop-0.75','cull_prop-0','elitism_size-5','elitism_size-10','elitism_size-20','mating_size-2','mating_size-10','mating_size-50','mut_prob-0.0198412698413','mut_prob-0.0992063492063','mut_prob-0.000992063492063','repl-True']
    lay = layout.getLayout("mediumClassic")
    ghosts = [DirectionalGhost(1),DirectionalGhost(2)]
    rules = ClassicGameRules()    
    for name in hypes:
        with open("{}.pkl".format(name),"rb") as bin:
            print "\nplaying the best from "+name
            data = pkl.load(bin)
            gene = data["genome"]
            pac = GeneticAgent(gene, AdvancedExtractor())
            game = rules.newGame( lay, pac, ghosts, PacmanGraphics(1.0,0.05), True, False)
            game.run()
            if game.state.data._win:
                print "Pacman emerges victorious! Score: %d" % game.state.data.score
            else:
                print "Pacman died! Score: %d" % game.state.data.score            
         
    #plays the best of the best hyperparameter combinations 10 times
    print "\nplaying the best from the training with the best hyperparameters 10 times"
    with open("cr_prob-0.15.pkl","rb") as bin:
        data = pkl.load(bin)
        gene = data["genome"]
        pac = GeneticAgent(gene, AdvancedExtractor())        
        for i in range(10):
            game = rules.newGame( lay, pac, ghosts, PacmanGraphics(1.0,0.05), True, False) 
            game.run()
            if game.state.data._win:
                print "Pacman emerges victorious! Score: %d" % game.state.data.score
            else:
                print "Pacman died! Score: %d" % game.state.data.score            
    
    #trains and runs approximate q-learning
    pac = ApproximateQAgent(extractor="SimpleExtractor")
    runGames(lay,pac,ghosts,PacmanGraphics(1.0,0.05),30,False,20,False,30,False,10,100,True)
