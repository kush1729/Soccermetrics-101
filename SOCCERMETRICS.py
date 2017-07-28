"""This will be the main program file to be run.
Every module in the 'modules' folder accesses files with respect to this file only.
Hence, beware while importing/running the modules in the 'modules' folder."""

import sys
import os
folder = os.getcwd()
sys.path.append(folder+"\\modules")

import players
import teams
import animations
import Main

animations.intro()

##print teams.allTeams
##teams.close()
