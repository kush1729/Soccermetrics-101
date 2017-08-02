"""This will be the main program file to be run.
Every module in the 'modules' folder accesses files with respect to this file only.
Hence, beware while importing/running the modules in the 'modules' folder."""

import sys
import os
folder = os.getcwd()
sys.path.append(folder+"\\modules")
sys.path.append(folder)

import players
import teams
import animations
import pygame

def Quit(gameDisplay, display_width, display_height):
    teams.close()
    pygame.quit()
    animations.quit_function(gameDisplay, display_width, display_height)
    quit()

pygame.init()
display_width = 1000
display_height = 750
gameDisplay = pygame.display.set_mode((display_width, display_height),pygame.FULLSCREEN)

animations.intro(gameDisplay, display_width, display_height)
animations.Load_Screen(gameDisplay, display_width, display_height)

#print teams.allTeams
Quit(gameDisplay, display_width, display_height)
