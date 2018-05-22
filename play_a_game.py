#for choosing the right directory, and moving there
import os
#for fixing a couple common issues with directories
from re import sub
#for launching the random game (i like it more than the os way)
from subprocess import Popen
#for choosing a random game
from random import randrange

#list of games
#could also open a random line % file length
#but that would mean keeping track of the number of games in the file
#which i don't feel like doing.
#if you have enough games that the difference in speed would matter,
#you have a problem. 
games = open("games.txt").readlines()

#gotta change to the location where the game is
#in order to launch it, so we choose a game from
#the list beforehand.  
#also remove any newlines and "" in the directory name
chosen_game = sub("[\n\"]","",games[randrange(len(games))])

#change directory to the chosen game's
os.chdir(os.path.dirname(chosen_game))

#open the game
Popen("\""+chosen_game+"\"")