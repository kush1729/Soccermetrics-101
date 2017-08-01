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
                 text = None, textcolour = black, size = 25, border = None):
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
        self.border = border 
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
        if self.border != None:
            pg.draw.rect(surface, self.border, (self.x, self.y, self.wd, self.ht), 1)
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
    def __init__(self, x, y, width, height, colour = black, restrict = None, xinterval = (-50, 100000),
                 yinterval = (-50, 100000), steps = 1):
        ''''restrict' restricts the movement of the object along a particular axis
restrict can only be 'y', 'x' to lock the y axis and x axis respectively
anything else does not lock any axis.

xinterval/yinterval is a 2-tuple of integers that gives a lower and upper bound
if they are None, then no limits shall be taken.

steps gives the jumps that the object will make'''
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
        self.xlim = xinterval
        if not self.movex:
            self.xlim = (self.x, self.x)
        if not self.movey:
            self.ylim = (self.y, self.y)
        self.ylim = yinterval 
        self.steps = steps
        self.active = tuple(min(25+c, 200) for c in colour)
        self.dragcolour = tuple(min(int(1.5*c), 240) for c in colour)

        if self.steps == 1:
            self.xbuckets = None
            self.ybuckets = None
            self.xind = None
            self.yind = None
        else:
            self.xbuckets = tuple(x for x in xrange(self.xlim[0], self.xlim[1]+1, self.steps))
            self.ybuckets = tuple(y for y in xrange(self.ylim[0], self.ylim[1]+1, self.steps))
            self.xind = (self.x - self.xlim[0])/self.steps
            self.yind = (self.y - self.ylim[0])/self.steps
            if self.xind >= len(self.xbuckets) or self.xind < 0:
                self.xind = 0
                self.x = self.xbuckets[self.xind]
            if self.yind >= len(self.ybuckets) or self.yind < 0:
                self.yind = 0
                self.y = self.ybuckets[self.yind]
                
    def __is_inside(self, (mx, my)):
        return (self.x < mx < self.x + self.wd) and (self.y < my < self.y + self.ht)
    def get_dragged(self):
        cur = pg.mouse.get_pos()
        clicked = pg.mouse.get_pressed()[0]
        if not self.drag and self.__is_inside(cur) and clicked:
            self.drag = True
            self.dx = self.steps*((cur[0] - self.x)//self.steps)
            self.dy = self.steps*((cur[1] - self.y)//self.steps)
        if self.drag and clicked:
            oldx = self.x
            oldy = self.y
            if self.steps == 1:
                self.x = cur[0] - self.dx
                self.y = cur[1] - self.dy
            else:
                supx = cur[0] - self.dx
                supy = cur[1] - self.dy
                self.xind = abs(supx - self.xlim[0])/self.steps
                self.yind = abs(supy - self.ylim[0])/self.steps
                if 0 > self.xind:
                    self.xind = 0
                elif self.xind >= len(self.xbuckets):
                    self.xind = len(self.xbuckets) - 1
                if 0 > self.yind:
                    self.yind = 0
                elif self.yind >= len(self.ybuckets):
                    self.yind = len(self.ybuckets) - 1
                self.x = self.xbuckets[self.xind]
                self.y = self.ybuckets[self.yind]
            if not(self.xlim[0] <= self.x <= self.xlim[1]) or not self.movex:
                self.x = oldx
            if not(self.ylim[0] <= self.y <= self.ylim[1]) or not self.movey:
                self.y = oldy
        elif self.drag and not clicked:
            self.drag = False
            self.dx = 0
            self.dy = 0
        
        return self.drag
    
    def blit(self, surface, update = False):
        if self.drag:
            c = self.dragcolour
        elif self.__is_inside(pg.mouse.get_pos()):
            c = self.active
        else:
            c = self.colour
        pg.draw.rect(surface, c, (self.x, self.y, self.wd, self.ht))
        if update: pygame.display.update()
            
class ListBox(object):
    def __init__(self, x, y, width, height, ind_ht, bkgcolour, *items):
        #ind_ht is the individual height of each box in the ListBox
        #the height will auto adjust to ensure that ind_ht divides height
        self.x = x
        self.y = y
        self.wd = width
        self.arrowsize = 20
        if height % ind_ht != 0:
            dyup = height % ind_ht
            dydown = ind_ht - (height%ind_ht)
            if dyup > dydown:
                dht = dydown
            else:
                dht = -dyup
        else:
            dht = 0
        self.ht = height + dht
        self.numvisible = (self.ht/ind_ht)
        if len(items) == 1 and (isinstance(items[0], list) or isinstance(itmes[0], tuple)):
            items = tuple(items[0])
        if len(items) < self.numvisible:
            items += ('',)*(self.numvisible-len(items))
        self.items = items
        self.ind_ht = ind_ht
        if items[-1] != '':
            self.hidden = len(items) - self.numvisible
        else:
            self.hidden = 0
##(x, y, width, height, action = RETURN_TRUE, inactivecolour = red, activecolour = orange,
##                 text = None, textcolour = black, size = 25)
        self.uparrow = Button(self.x+self.wd, self.y, self.arrowsize, self.arrowsize, Button.RETURN_TRUE,
                              grey, lightgrey, text = '/\\', size = self.arrowsize/5, border = black)
        self.downarrow = Button(self.x+self.wd, self.y+self.ht-self.arrowsize, self.arrowsize, self.arrowsize,
                                Button.RETURN_TRUE, grey, lightgrey, text = '\\/', size = self.arrowsize/5,
                                border = black)
        self.bkgcolour = bkgcolour
        self.scroll = self.__get_scroller()
        self.pos = 0

    def __get_scroller(self):
        ht = ((self.ht - 2*self.arrowsize)*self.numvisible)/len(self.items)
        remitems = self.hidden
        remspace = ((self.ht - 2*self.arrowsize)*self.hidden)/len(self.items)
        try:
            step = remspace/remitems
        except ZeroDivisionError:
            return None
        topmost = self.y + self.uparrow.ht 
        bottom = topmost + step*self.hidden
        return Dragable(self.x+self.wd, self.y+self.uparrow.wd, self.uparrow.wd, ht, colour = grey, restrict = 'x',
                        yinterval = (topmost, bottom), steps = step)
    
    def __iter__(self):
        for i in self.items:
            yield i

    def __drag_scroller(self):
        if self.hidden == 0 or self.scroll == None: return
        topmost = self.y+self.uparrow.ht
        buckets = [topmost+self.scroll.steps*i for i in xrange(self.hidden+1)]
        if self.scroll.get_dragged():
            self.pos = abs(topmost - self.scroll.y)/self.scroll.steps
    
    def shift(self):
        self.__drag_scroller()
        if self.downarrow.get_click():
            if self.pos < len(self.items) - self.numvisible:
                self.pos += 1
                if self.scroll != None:
                    self.scroll.y += self.scroll.steps
        elif self.uparrow.get_click():
            if self.pos > 0:
                self.pos -= 1
                if self.scroll != None:
                    self.scroll.y -= self.scroll.steps
    
    def blit(self, screen, update = False):
        pg.draw.rect(screen, self.bkgcolour, (self.x+self.wd, self.y, self.uparrow.wd, self.ht))
        self.uparrow.blit(screen, update = False)
        self.downarrow.blit(screen, update = False)
        if self.scroll == None:
            pg.draw.rect(screen, grey, (self.x+self.wd, self.y+self.uparrow.ht, self.uparrow.wd, self.ht - 2*self.arrowsize))
        else:
            self.scroll.blit(screen, update = False)
        pg.draw.rect(screen, black, (self.x-1, self.y-1, self.wd+self.uparrow.wd+2, self.ht+2), 1)
        pg.draw.line(screen, black, (self.x+self.wd, self.y), (self.x+self.wd, self.y+self.ht))
        pg.draw.rect(screen, self.bkgcolour, (self.x, self.y, self.wd, self.ht))
        for i in xrange(self.pos, self.pos + self.numvisible):
            j = i - self.pos
            text_to_button(screen, str(self.items[i]), black, self.x, self.y + j*self.ind_ht, self.wd,
                           self.ind_ht, int(self.ind_ht//(2.5)))
            if i != self.pos + self.numvisible - 1:
                pg.draw.rect(screen, black, (self.x, self.y+(j+1)*self.ind_ht-1, self.wd, 2))
        if update: pg.display.update()
        
if __name__ == '__main__':
    pg.init()
    screen = pg.display.set_mode((500, 500))
    screen.fill(white)
    clock = pg.time.Clock()
    obj = ListBox(10, 10, 200, 400, 100, green, ['ITEM %d'%(k) for k in xrange(3)])
    #s = Dragable(50, 50, 50, 200, colour = red, restrict = 'x',  yinterval = (50, 150),steps = 25)
    while True:
        for e in pg.event.get():
            if e.type == pg.QUIT or (e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE):
                pg.quit()
                quit()
        screen.fill(white)
        obj.shift()
##        s.get_dragged()
##        for i in xrange(20):
##            y = 10+20*i
##            pg.draw.line(screen, black, (0, y), (400, y))
##            message_to_screen(screen, str(y), black, (450, y), 20)
##        s.blit(screen)
        obj.blit(screen)
        clock.tick(20)
        pg.display.update()
        
