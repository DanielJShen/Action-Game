try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Classes.Utilities.Vector import Vector
from Classes.Abilities.Cannon import Cannon
import math
class Character:
    def __init__(self,vel,pos,image,rotation,size=0):
        self.vel:Vector = vel
        self.pos:Vector = pos
        self.speed = 5
        self.maxSpeed = 6
        self.health = 100
        self.activeAbility = Cannon()
        self.image:simplegui.Image = image
        self.rotation = rotation
        self.dim = ( self.image.get_width(), self.image.get_height())
        self.center = ( self.image.get_width()/2, self.image.get_height()/2)
        self.directions = ["UP", "LEFT", "DOWN", "RIGHT"]
        self.direction = ""

        if size == 0:
            self.size = self.dim
        else:
            self.size = size

        self.radius = max(size[0]/2,size[1]/2)

    def fire(self,pos:Vector,projectiles:list,lasers:list):
        self.activeAbility.fire(pos,projectiles,lasers,self.pos,"player")

    def draw(self,canvas,offset):
        canvas.draw_image(self.image, self.center, self.dim, (self.pos+offset).getP(), self.size, self.rotation)

    def update(self,keyboard,zoom, mousePos, offset):
        angle = math.atan2((self.pos + offset).getP()[0] - mousePos[0],
                           (self.pos + offset).getP()[1] - mousePos[1])
        for i in range(len(self.directions)):
            if ((i - 0.5) / len(self.directions) * 2 * math.pi) <= angle <= (
                    (i + 0.5) / len(self.directions) * 2 * math.pi):
                self.direction = self.directions[i]
                #  Split for clarity
            elif ((i - 0.5 - len(self.directions)) / len(self.directions) * 2 * math.pi) <= angle <= (
                    (i + 0.5 - len(self.directions)) / len(self.directions) * 2 * math.pi):
                self.direction = self.directions[i]

        if keyboard.right:
            self.vel.add(Vector(self.speed,0))
        if keyboard.left:
            self.vel.add(Vector(-self.speed,0))
        if keyboard.up:
            self.vel.add(Vector(0,-self.speed))
        if keyboard.down:
            self.vel.add(Vector(0,self.speed))
        self.pos.add(self.vel/zoom)
        self.vel = self.vel.getNormalized() * min(self.vel.length(),self.maxSpeed) * 0.935

class Keyboard:
    def __init__(self):
        self.right = False
        self.left = False
        self.up = False
        self.down = False
        self.space = False
        self.i = False

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
        if key == simplegui.KEY_MAP['i']:
            self.i = True

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
        if key == simplegui.KEY_MAP['i']:
            self.i = False
