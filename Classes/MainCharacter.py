try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Classes.Vector import Vector
from Classes.Objects.Projectile import Projectile
import math
class Character:
    def __init__(self,vel,pos,image,rotation):
        self.vel:Vector = vel
        self.pos:Vector = pos
        self.speed = 0.7
        self.maxSpeed = 3
        self.image:simplegui.Image = image
        self.rotation = rotation
        self.dim = ( self.image.get_width() , self.image.get_height() )
        self.center = ( self.image.get_width()/2 , self.image.get_height()/2 )

    def fire(self,pos:Vector,projectiles:list):
        vel = pos.copy().subtract(self.pos).getNormalized()*10
        projectiles.append( Projectile(vel,self.pos.copy(),10,20,True,10,"player") ) #TODO Fire type based on ability and powerups

    def draw(self,canvas):
        canvas.draw_image(self.image, self.center, self.dim, self.pos.getP(), self.dim, self.rotation)
    def update(self,keyboard):
        if keyboard.right:
            self.vel.add(Vector(self.speed,0))
        if keyboard.left:
            self.vel.add(Vector(-self.speed,0))
        if keyboard.up:
            self.vel.add(Vector(0,-self.speed))
        if keyboard.down:
            self.vel.add(Vector(0,self.speed))
        self.pos.add(self.vel)
        self.vel = self.vel.getNormalized() * min(self.vel.length(),self.maxSpeed) * 0.935

class Keyboard:
    def __init__(self):
        self.right = False
        self.left = False
        self.up = False
        self.down = False
        self.space = False

    def keyDown(self, key):
        if key == simplegui.KEY_MAP['right']:
            self.right = True
        if key == simplegui.KEY_MAP['left']:
            self.left = True
        if key == simplegui.KEY_MAP['up']:
            self.up = True
        if key == simplegui.KEY_MAP['down']:
            self.down = True
        if key == simplegui.KEY_MAP['space']:
            self.space = True

    def keyUp(self, key):
        if key == simplegui.KEY_MAP['right']:
            self.right = False
        if key == simplegui.KEY_MAP['left']:
            self.left = False
        if key == simplegui.KEY_MAP['up']:
            self.up = False
        if key == simplegui.KEY_MAP['down']:
            self.down = False
        if key == simplegui.KEY_MAP['space']:
            self.space = False
