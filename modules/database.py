# Import stuff here:
from os import getcwd
from pickle import load, dump
import pygame
pygame.init()
import time
# ------------------------------------------
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
##gameDisplay.fill(white)
##pygame.display.update()
# --------------------------------------------------------------------------------------
# Images:

"BACKGROUND IMAGES:"
pitchback = pygame.image.load("pitch.png")


"OtherImages:"
smallball1 = pygame.image.load("smallball1.png")
smallball2 = pygame.image.load("smallball2.png")
bigball1 = pygame.image.load("bigball1.png")
bigball2 = pygame.image.load("bigball2.png")
# ---------------------------------------------------------------------------
# Any lists:
allTeams = []
# ----------------------------------------------------------------------------------------





"""The functions that are for visual effect are defined here!!"""
def background(images, xpos, ypos):         # All three are lists!
    for i in range(len(images)):
        gameDisplay.blit(images[i], [xpos[i], ypos[i]])
        # No updating coz otherwise there'll be a slight lag between background and foreground


# Main INTRO Function! (ACTUALLY CALLED BY ANOTHER FUNCTION CALLED "INTRO" xD)
def introductory_function():
    gameDisplay.fill(white)
    pygame.display.update()
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
        
        while ballx < display_width/2 - 140:            # Taking into account the size of the ball at the time
            clock.tick(fps)
            ballimg = balllist[count%2]
            s = ballimg.get_size()
            if s[0] > 120 or s[1] > 120:
                balllist = bigballlist
            
            background([pitchback, ballimg], [backx, ballx], [backy, bally])
            ballx += 25
            
            
            
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
                        if bally <> display_height/2 - size[1]/2:
                            bally = display_height/2 - size[1]/2
            pygame.display.flip()
            

        else:
            size = bigball1.get_size()
            background([pitchback, bigball2], [backx, (display_width/2 - size[0]/2)], [backy, (display_height/2-size[1]/2)-5])
            pygame.display.update()

##        yield
        time.sleep(0.5)
        # More Variables:
        radius = 10
        while radius < 156:
            pygame.draw.circle(gameDisplay, white, (display_width/2, display_height/2), radius)
            radius += 20
            time.sleep(0.1)
            pygame.display.flip()
        gameon = not gameon
            

        


def intro():
    introductory_function()
    while True:

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: 
                    pygame.quit()
                    quit()
    

# -------------------------------------------------------------------------------------------



"""Class Definition is incomplete.
Methods to calculate ELO, financial status etc are required."""
class Team(object):
    """Base Class of Team object.
The Team Object will store all relevant data of a particular team."""
    def __init__(self, name, players = []):
        self.name = name
        self.player_list = players
        self.ELO = 0  #to be calculated later
        allTeams.append(self)
    def __str__(self):
        """string representation of the team"""
        return self.name
    def __repr__(self):
        """formal string representaion for debugging"""
        return "< %s: dict:= %s > \n"%(self.name, str(self.__dict__))
    def __del__(self):
        """On deletion of the object, the team shall be removed from the list of teams, as well as the binary file.
Hence, proper care must be taken when deleting a Team object."""
        allTeams.remove(self)
    def __lt__(self, obj):
        """Compares current ELO rating with obj.
If obj is an int object, then it will be assumed to be an ELO rating."""
        if isinstance(obj, int):
            return self.ELO < obj
        elif isinstance(obj, Team):
            return self.ELO < obj.ELO
        raise NotImplemented
    def __le__(self, obj):
        """Compares current ELO rating with obj.
If obj is an int object, then it will be assumed to be an ELO rating."""
        if isinstance(obj, int):
            return self.ELO <= obj
        elif isinstance(obj, Team):
            return self.ELO <= obj.ELO
        raise NotImplemented
    def __gt__(self, obj):
        return not(self <= obj)
    def __ge__(self, obj):
        return not(self < obj)
    def __eq__(self, obj):
        """If obj is of team type, then checks if they have the same name.
Otherwise, the object should be an integer, which will be compared with the ELO rating"""
        if isinstance(obj, int):
            return self.ELO == int
        elif isinstance(obj, Team):
            return self.name == obj.name
        raise NotImplemented
    def __ne__(self, obj):
        return not (self == obj)
    def __hash__(self):
        """name of the team will be used for the hash"""
        return hash(self.name)
    def __len__(self):
        return len(self.player_list)
    def __iter__(self):
        """Iterates over all the players in the team"""
        for p in self.player_list:
            yield p
    def __contains__(self, player):
        """Checks whether the player is currently in the team"""
        return (player in self.player_list)

def _load():
    global allTeams
    folder = getcwd()
    filename = folder + r"\data\TeamDatabase.pydb"
    allTeams = []
    with open(filename, "rb") as f:
        while True:
            try:
                t = load(f)
            except EOFError:
                break
            else:
                allTeams.append(t)

def _dump():
    global allTeams
    folder = getcwd()
    filename = folder + r"\data\TeamDatabase.pydb"
    with open(filename, "wb") as f:
        for t in allTeams:
            dump(t, f)
    allTeams = []

def save_backup():
    """Function that will save all the data in a text file as a backup.
This text file will only be accessed by this function and the function 'load_backup()'"""
    folder = getcwd()
    filename = folder + r"\data\BackupDatabase.txt"
    with open(filename, "wb") as f:
        for t in allTeams:
            dump(t, f)

def load_backup():
    """Will load the backup database that is stored in the text file.
Will return a list of all the team objects stored in the text file."""
    folder = getcwd()
    filename = folder + r"\data\BackupDatabase.txt"
    l = []
    with open(filename, "rb") as f:
        while True:
            try:
                t = load(f)
            except EOFError:
                break
            else:
                l.append(t)
    return l

def close():
    """This method should be called everytime the program stops using this module, especially if any data has been changed"""
    _dump()
    save_backup()
    quit()

##if __name__ != "__main__":
##    allTeams = _load()
##elif __name__ == "__main__":
##    testobj = Team("Test Team", ["Player Name 1", "Player Name 2"])
##    save_backup()
    


# ---------------------------------------------------------------------------------------------------------------------------------------------------------

# TOP LEVEL
intro()





        
        
