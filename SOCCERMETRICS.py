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
import algorithms

import animations
import pygame

import GUIelements as gui
import back_up as bu

import traceback

def Quit(gameDisplay, display_width, display_height):
    teams.close()
    bu.backupplayers()
    bu.backupteams()
    animations.quit_function(gameDisplay, display_width, display_height)
    pygame.quit()
    quit()

pygame.init()
display_width = 1000
display_height = 750
gameDisplay = pygame.display.set_mode((display_width, display_height),pygame.FULLSCREEN)

try:
    animations.intro(gameDisplay, display_width, display_height)
    animations.Load_Screen(gameDisplay, display_width, display_height)
    teams.table = table = teams.Simulate(teams.allTeams)

    for team in teams.allTeams.values():
        for player in team.player_list:
            player.rater()
    algorithms.suggester()

    animations.Menu1(gameDisplay, display_width, display_height, [t.name for t in table])
    #print teams.allTeams
    Quit(gameDisplay, display_width, display_height)
except Exception as e:
    traceback.print_exc()
    pygame.quit()
    quit()
