install python2.7 if it is not already installed, python2.7 should be the only thing you need to run this project, other versions of python2 may also work

navigate to the SRC directory in the terminal

run "python2.7 demo.py" without the quotes
If python2.7 is the only version of python you have than "python demo.py" should also work

The demo will run 1 game for the best gene for each of the hyper parameter combinations we tested, 10 games for the best gene of the best of the hyper parameter combinations we tested and then train and test approximate q-learning after 800 training episodes for comparison. 

we stopped training the approximate q-learning agent after 800 training episodes because it looked like training it any longer than that makes it perform worse, we are not sure why this happens but it is possible that it is overfitting in some way. 

The demo will not need to train the genetic algorithm since we already did the training and saved the results. Training the approximate q-learning may take a while on slow computers but it finished in only a few minutes on a university computer. If you would like to see a genetic algorithm you can run it with "python2.7 paceman.py --gen" and optional arguments:
