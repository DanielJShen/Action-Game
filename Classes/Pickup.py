from Classes.Utilities.Vector import Vector
from Classes.Spritesheet import Spritesheet

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

class Pickup:
    def __init__(self,pos,img,colunms,rows,type,value):
        self.spritesheet = Spritesheet(img,colunms,rows,0)
        self.pos = pos
        self.width, self.height = 50,50
        self.radius = max(self.width,self.height)/2
        self.type = type
        self.value = value


    def draw(self,canvas,offset):
        self.spritesheet.update()
        self.spritesheet.draw(canvas,offset,self.pos,self.width,self.height)