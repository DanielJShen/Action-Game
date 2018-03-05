try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Classes.Vector import Vector
from Classes.Objects.Projectile import Projectile
import math
class Character:
    def __init__(self,vel,pos,image,rotation,size=0):
        self.vel:Vector = vel
        self.pos:Vector = pos

        self.speed = 0.7
        self.maxSpeed = 3
        self.health = 100

        self.image:simplegui.Image = image
        self.rotation = rotation
        self.dim = ( self.image.get_width() , self.image.get_height() )
        self.center = ( self.image.get_width()/2 , self.image.get_height()/2 )
        self.radius = max(size[0],size[1])

        if size == 0:
            self.size = self.dim
        else:
            self.size = size

    def fire(self,pos:Vector,projectiles:list):
        vel = pos.copy().subtract(self.pos).getNormalized()*7
        projectiles.append( Projectile(vel,self.pos.copy(),10,0.5,True,10,"player") ) #TODO Fire type based on ability and powerups

    def draw(self,canvas,offset):
        canvas.draw_image(self.image, self.center, self.dim, (self.pos+offset).getP(), self.size, self.rotation)
    def update(self,keyboard,zoom):
        if keyboard.right:
            self.vel.add(Vector(self.speed,0))
        if keyboard.left:
            self.vel.add(Vector(-self.speed,0))
        if keyboard.up:
            self.vel.add(Vector(0,-self.speed))
        if keyboard.down:
            self.vel.add(Vector(0,self.speed))
        self.pos.add(self.vel*zoom)
        self.vel = self.vel.getNormalized() * min(self.vel.length(),self.maxSpeed) * 0.935

class Keyboard:
    def __init__(self):
        self.right = False
        self.left = False
        self.up = False
        self.down = False
        self.space = False

    def keyDown(self, key):
        if key == simplegui.KEY_MAP['d']:
            self.right = True
        if key == simplegui.KEY_MAP['a']:
            self.left = True
        if key == simplegui.KEY_MAP['w']:
            self.up = True
        if key == simplegui.KEY_MAP['s']:
            self.down = True
        if key == simplegui.KEY_MAP['space']:
            self.space = True

    def keyUp(self, key):
        if key == simplegui.KEY_MAP['d']:
            self.right = False
        if key == simplegui.KEY_MAP['a']:
            self.left = False
        if key == simplegui.KEY_MAP['w']:
            self.up = False
        if key == simplegui.KEY_MAP['s']:
            self.down = False
        if key == simplegui.KEY_MAP['space']:
            self.space = False
