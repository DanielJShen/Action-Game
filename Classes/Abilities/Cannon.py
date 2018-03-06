from Classes.Objects.Projectile import Projectile
class Cannon():
    def __init__(self):
        self.sprite = object

        self.radius = 10
        self.colour = "#7a14ff"
        self.time = 0.5
        self.bounce = True
        self.baseDamage = 10


    def fire(self,toPos,projectiles,fromPos,owner):
        vel = toPos.copy().subtract(fromPos).getNormalized()*7
        projectiles.append( Projectile(vel,fromPos.copy(),self.radius,self.time,self.bounce,self.baseDamage,owner,self.colour) ) #TODO Fire type based on ability and powerups

