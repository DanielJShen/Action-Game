try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Classes.Objects.Projectile import Projectile
class Cannon():
    def __init__(self):
        self.sprite = object
        self.radius = 10
        self.colour = "#7a14ff"
        self.time = 1.5
        self.bounce = True
        self.baseDamage = 10
        self.image = simplegui._load_local_image("Resources/images/Cannon.png")


    def fire(self,toPos,projectiles,lasers,fromPos,owner,image):
        vel = toPos.copy().subtract(fromPos).getNormalized()*30
        projectiles.append( Projectile(vel,fromPos.copy(),self.radius,self.time,self.bounce,self.baseDamage,owner,image) )

