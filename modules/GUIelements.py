"""Module for buttons, list boxes etc, as well as the module that will contain any generic function for GUI stuff
Each of the interface elements must be a python class

This module will heavily use the following things in python:

1. functions can be assigned to variables, be values in dictionaries, be passed as arguments in function definitions
and generally act like class objects
eg:
x = int
x(4.90) return 4 etc.

2. functions have 2 special kind of arguments:
*parameter and **keywordparameter

what *parameter does is take multiple letf over arguments passed in function definition and combine them in a tuple.
eg:
def test(a, *numbers):
    for i in numbers:
        print i+a, ",", 

test(4, 1, 2, 3, 4, 5) #outputs:  '5, 6, 7, 8, 9,'

what **keywords does is take multiple left over keyword arguments and combine them as a dictionary.
eg:
def test(**stuff):
    for key in stuff:
        print key, stuff[key]
test(a = 2, b = 3.0, lol = '100', d = [5, 6])
output:
a 2
b 3.0
lol 100
d [5, 6]
"""
import pygame as pg
from Colours import *

def text_objects(text, colour, size, numreturn = 2):
##    font_dict = {'small':smallfont, 'medium':medfont, 'large':largefont, 'smallmed':smallmedfont, 'mediumlarge':mediumlargefont}
    #size is font size as an integer
    
    textSurface = pg.font.SysFont("comicsansms", size).render(text, True, colour)
    if numreturn == 2: return textSurface, textSurface.get_rect()
    else: return textSurface.get_rect()

def text_to_button(screen, msg, color, btnx, btny, btnwidth, btnheight, size = 25):
    textSurf , textRect = text_objects(msg, color, size)
    textRect.center = ((btnx + (btnwidth / 2)), (btny + (btnheight / 2)))
    screen.blit(textSurf, textRect)

def message_to_screen(screen, msg, color, center_loc, size):
    textSurf , textRect = text_objects(msg, color, size)
    textRect.center = center_loc
    screen.blit(textSurf, textRect)
    return textRect

class Clickable(object):
    """parent class for any GUI element that takes a mouse click"""
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.ht = height
        self.wd = width
    def get_click(self, left = True):
        #left is a parameter for choosing which mouse key gets clicked.
        #left = True for left click and left = False for right click
        i = 0 if left == True else 1
        cur = pg.mouse.get_pos()
        clicked = pg.mouse.get_pressed()[i]
        if clicked and (self.x < cur[0] < self.x + self.wd) and (self.y < cur[1] < self.y + self.ht):
            return True
        return False

class Button(Clickable):
    RETURN_TRUE = 1
    RETURN_FALSE = 2
    RETURN_NONE = 0
    def __init__(self, x, y, width, height, action = RETURN_TRUE, inactivecolour = red, activecolour = orange,
                 text = None, textcolour = black, size = 25):
        """'action' parameter will take either a function object, or a constant value defined in the class attributes of Button.
if action is a function, then the function should not take any parameters (this class will not pass any parameters)
when the action function is called, this class will return whatever the action() function returns.

if action is a constant defined in the class attributes of Button, then action will be assigned a particular null function
as defined by the name of the constant."""
        super(Button, self).__init__(x, y, width, height)
        if action == Button.RETURN_TRUE:
            def temp(): return True
            action = temp
        self.action = action
        self.inactive = inactivecolour
        self.active = activecolour
        if text == None:
            text = action.__name__.upper()
        self.text = text
        self.textcolour = textcolour
        self.size = size
    def blit(self, surface, update = False):
        cur = pg.mouse.get_pos()
        if (self.x < cur[0] < self.x+self.wd) and (self.y < cur[1] < self.y + self.ht):
            c = self.active
        else:
            c = self.inactive
        pg.draw.rect(surface, c, (self.x, self.y, self.wd, self.ht))
        text_to_button(surface, self.text, self.textcolour, self.x, self.y, self.wd, self.ht, self.size)
        if update:
            pg.display.update()
    def get_click(self):
        flag = super(Button, self).get_click(True)
        if flag:
            return self.action()

class Dragable(object):
    '''Object that can be dragged by the mouse.
Mouse has to be held while shifting.
'''
    def __init__(self, x, y, width, height, colour = black, restrict = 'y'):
        ''''restrict' restricts the movement of the object along a particular axis
restrict can only be 'y', 'x' to lock the y axis and x axis respectively
anything else does not lock any axis.'''
        self.x = x
        self.y = y
        self.movex = not(restrict == 'x')
        self.movey = not(restrict == 'y')
        self.wd = width
        self.ht = height
        self.drag = False
        self.colour = colour
        self.dx = 0
        self.dy = 0
    def __is_inside(self, (mx, my)):
        return (self.x < mx < self.x + self.wd) and (self.y < my < self.y + self.ht)
    def get_dragged(self):
        cur = pg.mouse.get_pos()
        clicked = pg.mouse.get_pressed()[0]
        if not self.drag and self.__is_inside(cur) and clicked:
            self.drag = True
            self.dx = cur[0] - self.x
            self.dy = cur[1] - self.y
        if self.drag and clicked:
            if self.movex:
                self.x = cur[0] - self.dx
            if self.movey:
                self.y = cur[1] - self.dy
        elif self.drag and not clicked:
            self.drag = False
            self.dx = 0
            self.dy = 0
    def blit(self, surface, update = False):
        pg.draw.rect(surface, self.colour, (self.x, self.y, self.wd, self.ht))
        if update: pygame.display.update()
            
##class ListBox(object): #coming up!
##    def __init__(self, x, y, width, height, *items):
##        self.x = a
##        self.y = y
##        self.wd = width
##        self.ht = height
##        self.items = items
####(x, y, width, height, action = RETURN_TRUE, inactivecolour = red, activecolour = orange,
####                 text = None, textcolour = black, size = 25)
##        self.uparrow = Button(self.x+self.wd-5, self.y, 
##    def __iter__(self):
##        for i in self.items:
##            yield i
##    def blit(self):
        
if __name__ == '__main__':
    pg.init()
    screen = pg.display.set_mode((500, 500))
    screen.fill(white)
    clock = pg.time.Clock()
    obj = Dragable(25, 25, 100, 50, restrict = 'x')
    while True:
        for e in pg.event.get():
            if e.type == pg.QUIT or (e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE):
                pg.quit()
                quit()
        screen.fill(white)
        obj.get_dragged()
        obj.blit(screen)
        clock.tick(10)
        pg.display.update()
        
