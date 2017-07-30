"""module for all specific animation functions.
All functions in this module will be only for specific animations/transitions/specific visual effects that will be required.

this module does not contain any generic functions which will be used repeatedly (eg does not have text to screen functions
etc). Refer to GUIanimations for details on generic functions

Also, for ease of use and to avoid any issues with namespaces etc, pass all required variables as function parameters.
for example, pass gameDisplay as a parameter.
Note that this will not be the main file run, and so should be import friendly
Hence, this should not run anything (like initializing the screen surface) unless explicitly checked that
the namespace is __main__"""

import pygame
pygame.init()
import time
from math import sqrt
from os import getcwd
import GUIelements as gui

# ------------------------------------------
# Control frames per second:----------------
clock = pygame.time.Clock()
# ----------------------------------------------------
#COLOURS: (Refer to RGB dictionary)----------------------------------------------------------
from Colours import *

# --------------------------------------------------------------------------
#IMPORTANT CONSTANTS FOR DESIGN OF GAME DISPLAY------------------------------------------
##gameDisplay.fill(white)
##pygame.display.update()
# --------------------------------------------------------------------------------------
# Images:

if __name__ != "__main__":
    folder = getcwd() + "\\modules\\images\\"
else:
    folder = getcwd() + "\\images\\"
    display_width, display_height = 1000, 750
    gameDisplay = pygame.display.set_mode((display_width, display_height), pygame.FULLSCREEN)

"BACKGROUND IMAGES:"
pitchback = pygame.image.load(folder+"pitch.png")
centrecircle = pygame.image.load(folder+"CentreCircle.png")


"OtherImages:"
smallball1 = pygame.image.load(folder+"smallball1.png")
smallball2 = pygame.image.load(folder+"smallball2.png")
bigball1 = pygame.image.load(folder+"bigball1.png")
bigball2 = pygame.image.load(folder+"bigball2.png")
mediumball1 = pygame.image.load(folder+"mediumball1.png")
mediumball2 = pygame.image.load(folder+"mediumball2.png")


# ---------------------------------------------------------------------------
# Any lists:
#allTeams = []
# ----------------------------------------------------------------------------------------

"""The functions that are for visual effect are defined here!!"""
def background(images, xpos, ypos):         # All three are lists!
    for i in range(len(images)):
        gameDisplay.blit(images[i], [xpos[i], ypos[i]])
        # No updating coz otherwise there'll be a slight lag between background and foreground

def checkquit():
    for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: 
                    pygame.quit()
                    quit()

##
##def button(textinbutton, x, y, width1, height1, inactivecolour,
##           activecolour, action = None):
##    cur = pygame.mouse.get_pos()
##    click = pygame.mouse.get_pressed()
##
##    if x + width1 > cur[0] > x and y + height1 > cur[1] > y:
##        
##        pygame.draw.rect(gameDisplay, activecolour, (x, y, width1,
##                                                     height1))
##    
##        if click[0] == 1 and action <> None:
##            if action.lower() == "begin":
##                return True
##                
##
##            return action
##    else:
##        pygame.draw.rect(gameDisplay, inactivecolour, (x, y, width1, height1))
##        
##    text_to_button(textinbutton, black, x, y, width1, height1)
##    pygame.display.update()
##

# Main INTRO Function! 
def intro(gameDisplay, display_width, display_height):
    gameDisplay.fill(white)
    pygame.display.update()
    gameon = True
    background([pitchback], [0], [0])
    ballsize = smallball1.get_size()
    bigballsize = bigball1.get_size()
    while gameon:
        # Variables:
        ballx, bally = 5 + ballsize[0], display_height/2
        balllist = [bigball1, bigball2]
        for i in range(len(balllist)):
            balllist[i] = pygame.transform.scale(balllist[i], (20,20))
        bigballlist = [bigball1, bigball2]
        mediumballlist = [mediumball1, mediumball2]
        backx, backy = 0,0
        fps = 60
        
        # --------------------------------
        
        pygame.display.flip()
        count = 0
        Medium = False
        Big = False

##        pygame.mixer.init()
##        pygame.mixer.music.load("Cheer.mp3")
##        pygame.mixer.music.play(-1)

        while ballx < display_width/2 - 140:    # Taking into account the size of the ball at the time

            checkquit()                 # Function that checks if escape key is pressed and if so
                                        # it quits
            clock.tick(fps)
            ballimg = balllist[count%2]   # Two images are of the ball in two positions giving the effect of it spinning
            s = ballimg.get_size()

            if (s[0] > 180 or s[1] > 180) and not Big:              # Resizing a very small image to large sizes can cause
                balllist = bigballlist                                  #  loss in resolution
                                                                        
                for i in range(len(balllist)):
                    balllist[i] = pygame.transform.scale(balllist[i], [(9 *180)/5 , (9*180)/5])  # i.e., making it approx 1.8 times its size
                Big = True

            elif (s[0] > 50 or s[1] > 50) and not Medium:
                balllist = mediumballlist
                for i in range(len(balllist)):
                    balllist[i] = pygame.transform.scale(balllist[i], [(9 *50)/5 , (9*50)/5])
                Medium = True
            
            bally = display_height/2 - s[1]/2
            background([pitchback, ballimg], [backx, ballx], [backy, bally])
            
            if ballx + 25 > (display_width/2 - bigballsize[0]/2):
                ballx = (display_width/2 - bigballsize[0]/2)
                
            else:
                ballx += 25
            
            
            
            count += 1
            
            
            
                
            if s[0] < 280 and s[1] < 280 and count % 2 == 0: 
                
                for i in range(len(balllist)):
                    size = balllist[i].get_size()
                    balllist[i] = pygame.transform.scale(balllist[i], [(9 *size[0])/5 , (9*size[1])/5])
                        
            pygame.display.flip()
            

        else:                       # => ball is right in the centre circle
            
            checkquit()             # Basic Function that checks if Escape Key is pressed, if so quits
            size = bigball1.get_size()
            background([pitchback, bigball2], [backx, (display_width/2 - size[0]/2)], [backy, (display_height/2-size[1]/2)-5])
            pygame.display.update()


        time.sleep(0.5)  # Slight pause for effect
        
        # More Variables:
        radius = 10
        a, b, c, = 255, 255, 255  
        
        while radius < 155:
            checkquit() # Check if you want to quit

            pygame.draw.circle(gameDisplay, (a, b, c), (display_width/2, display_height/2), radius)
            # An inner coloured circle of colour value (a, b, c) is drawn (fades in from black to white)

            if a - radius < 0:
                a = 0
            else:
                a -= radius
            if b - radius < 0:
                b = 0
            else:
                b -= radius
            if c - radius < 0:
                c = 0
            else:
                c -= radius
            
            radius += 20
            time.sleep(0.1)
            pygame.display.flip()

            
        # Next Part => Getting the words "SOCCERMETRICS 101" on the edge of the circle
        text = "SOCCERMETRICS 101"
        textx = display_width/2 - radius + 34  
        texty = display_height/2
        change = 15
        textsize = 23
        centre = (display_width/2, display_height/2)  # Centre of the circle
        temp_rad = radius - textsize - 10

                  
        for letter in text:
            textx += change    
            texty = centre[1] - sqrt(temp_rad ** 2 - (textx - centre[0])**2)   # Using the circle formula to get coordinates of points on the edge of it
            # This function gets the letters on the screen
            gui.message_to_screen(gameDisplay, letter, white, (textx, texty), textsize) 
            pygame.display.update()
            time.sleep(0.2)             # Makes the letters appear one at a time for visual effect

            
            
            
                


        # More Variables:
        buttonheight = 100
        buttonwidth = 200
        buttonx = display_width/2 - buttonwidth/2
        buttony = display_height/2 - buttonheight/2
        #Button.__init__(x, y, height, width, action = Button.RETURN_TRUE, inactivecolour = red,
        #                activecolour = orange, text = None, textcolour = black, size = 25)
        button = gui.Button(buttonx, buttony, buttonwidth,
                   buttonheight, inactivecolour = yellow, activecolour = gold, text = "Begin")

        colour = [255, 255, 255]        # i.e., Starting colour of the button
        while True:
            
            while colour <> list(yellow):       # The button fades in from white to yellow
                for i in range(3):
                    
                    if colour[i] < yellow[i]:
                        colour[i] += 1
                    elif colour[i] > yellow[i]:
                        colour[i] -= 1
                pygame.draw.rect(gameDisplay, colour,
                                 (buttonx, buttony, buttonwidth, buttonheight))
                time.sleep(0.002)
                pygame.display.flip()
                checkquit()

            start = button.get_click()
            button.blit(gameDisplay, True)
            checkquit()
            if start:
                while radius < max(display_width, display_height):
                    checkquit()
                    radius += 25
                    pygame.draw.circle(gameDisplay, black, centre, radius)
                    pygame.display.flip()
                    time.sleep(0.02)

                backsize = centrecircle.get_size()
                backx = (display_width-backsize[0])/2
                backy = (display_height - backsize[1])/2
                background([centrecircle], [backx], [backy])
                
                while True:
                    checkquit()
                    if radius - 20 > 0:
                        radius -= 20
                    else:
                        break
                    pygame.draw.circle(gameDisplay, black, centre, radius)
                    pygame.display.flip()
                    background([centrecircle], [backx], [backy])

                    
                    
                pygame.display.flip()
                Choose_Option(gameDisplay, display_width, display_height)
                
           

def Choose_Option(gameDisplay, display_width, display_height):
    gameDisplay.fill(white)
    choosing = True
    backsize = centrecircle.get_size()
    backx = (display_width-backsize[0])/2
    backy = (display_height - backsize[1])/2
    background([centrecircle], [backx], [backy])


    
    while choosing:
        background([centrecircle], [backx], [backy])
        checkquit()
            

# -------------------------------------------------------------------------------------------
if __name__ == '__main__':
    intro(gameDisplay, display_width, display_height)
