# Import stuff here -----------------------
import pygame
from os import getcwd
##import random
##import math
# ----------------------------------------------


# Control frames per second:----------------
clock = pygame.time.Clock()
# ----------------------------------------------------
#COLOURS: (Refer to RGB dictionary)----------------------------------------------------------
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
darkgreen = (34, 139, 34)
yellow = (255, 255, 0)
gold = (255, 215, 0)
goldenrod = (218, 165, 32)
blue = (0, 0, 255)
lightblue = (0, 191, 255)
darkblue = (0, 0, 220)
lightgrey = (218, 218, 218)
tomato = (255, 99, 71)
sienna = (160, 82, 45)
darkorange = (255, 140, 0)
purple = (0, 255, 255)
# --------------------------------------------------------------------------
#IMPORTANT CONSTANTS FOR DESIGN OF GAME DISPLAY------------------------------------------
display_width, display_height = 1000, 750
gameDisplay = pygame.display.set_mode((display_width, display_height), pygame.FULLSCREEN)
gameDisplay.fill(white)
pygame.display.update()
# --------------------------------------------------------------------------------------
# Images:

folder = getcwd() + "\\images\\"

"BACKGROUND IMAGES:"
pitchback = pygame.image.load(folder+"pitch.png")


"OtherImages:"
smallball1 = pygame.image.load(folder+"smallball1.png")
smallball2 = pygame.image.load(folder+"smallball2.png")
bigball1 = pygame.image.load(folder+"bigball1.png")
bigball2 = pygame.image.load(folder+"bigball2.png")
# ---------------------------------------------------------------------------
def background(images, xpos, ypos):         # All three are lists!
    for i in range(len(images)):
        gameDisplay.blit(images[i], [xpos[i], ypos[i]])
        # No updating coz otherwise there'll be a slight lag between background and foreground
                                                

# -------------------------------------------------------------------------------------------
                    
def main():
    gameDisplay.fill(white)

    gameon = True
    background([pitchback], [0], [0])
    ballsize = smallball1.get_size()
    while gameon:
        # Variables:
        ballx, bally = 5 + ballsize[0], display_height/2
        balllist = [bigball1, bigball2]
        for i in range(len(balllist)):
            balllist[i] = pygame.transform.scale(balllist[i], (20,20))
        bigballlist = [bigball1, bigball2]
        backx, backy = 0,0
        fps = 60
        
        # --------------------------------
        
        pygame.display.flip()
        count = 0
        
        while ballx < display_width/2 - 140:
            clock.tick(fps)
            ballimg = balllist[count%2]
            s = ballimg.get_size()
            if s[0] > 120 or s[1] > 120:
                balllist = bigballlist
            
            background([pitchback, ballimg], [backx, ballx], [backy, bally])
            ballx += 25
            
            if bally <> display_height/2 - s[1]/2:
                bally = display_height/2 - s[1]/2
            
            count += 1
            
            
                
            if s[0] < 280 and s[1] < 270 and count % 3 == 0:
                
                if s[0] * 2 >= 280 or s[1] >= 280:
                    pass
##                    balllist = bigballlist
##                    for i in range(len(balllist)):
##                        
##                        balllist[i] = pygame.transform.scale(balllist[i], (280, 280))
                else:
                    for i in range(len(balllist)):
                        size = balllist[i].get_size()
                        balllist[i] = pygame.transform.scale(balllist[i], [(9 *size[0])/5 , (9*size[1])/5])
            pygame.display.flip()

        else:
            size = bigball1.get_size()
            background([pitchback, bigball2], [backx, (display_width/2 - size[0]/2)], [backy, (display_height/2-size[1]/2)-5])
            pygame.display.update()
            

        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE: 
                        pygame.quit()
                        quit()
        

# TOP LEVEL STATEMENTS!
#main()
        
