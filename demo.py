import pickle as pkl
import pacman
import util, layout
from learningAgents import GeneticAgent
from featureExtractors import AdvancedExtractor
from graphicsDisplay import PacmanGraphics
from ghostAgents import DirectionalGhost
from ghostAgents import GhostAgent
from game import Agent
from layout import Layout
from pacman import ClassicGameRules


if __name__ == '__main__':
    hypes = ['cr_prob-0.8']
    for name in hypes:
        with open("{}.pkl".format(name),"rb") as bin:
            data = pkl.load(bin)
            gene = data["genome"]
            pac = GeneticAgent(gene, AdvancedExtractor())
            lay = layout.getLayout("mediumClassic")
            ghosts = [DirectionalGhost(1),DirectionalGhost(2)]
            rules = ClassicGameRules()
            game = rules.newGame( lay, pac, ghosts, PacmanGraphics(1.0,0.2), False, False)
            game.run()            