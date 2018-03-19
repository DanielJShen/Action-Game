try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Classes.Objects.Projectile import Projectile
from Classes.Utilities.Vector import Vector

class Shotgun():
    def __init__(self):
        self.sprite = object
        self.radius = 4
        self.time = 0.9
        self.bounce = False
        self.resetDamage = 5
        self.baseDamage = 5
        self.speed = 15
        self.image = simplegui._load_local_image("Resources/images/Shotgun.png")


    def fire(self,toPos,projectiles,lasers,fromPos,owner,timer=0.9,scaleState=False,image=None):
        vel:Vector = toPos.copy().subtract(fromPos).getNormalized()*self.speed
        vel.rotate(-10)
        for i in range(4):
            projectiles.append( Projectile(vel.copy().rotate(5*i),fromPos.copy(),self.radius,self.time,self.bounce,self.baseDamage,owner,scaleState,image) )

