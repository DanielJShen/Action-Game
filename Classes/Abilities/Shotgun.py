from Classes.Objects.Projectile import Projectile
from Classes.Vector import Vector

class Shotgun():
    def __init__(self):
        self.sprite = object
        self.radius = 7
        self.colour = "#ff5555"
        self.time = 0.3
        self.bounce = False
        self.baseDamage = 5
        self.speed = 5


    def fire(self,toPos,projectiles,fromPos,owner):
        vel:Vector = toPos.copy().subtract(fromPos).getNormalized()*self.speed
        vel.rotate(-10)
        for i in range(4):
            projectiles.append( Projectile(vel.copy().rotate(5*i),fromPos.copy(),self.radius,self.time,self.bounce,self.baseDamage,owner,self.colour) )

