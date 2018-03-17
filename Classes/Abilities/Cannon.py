try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Classes.Objects.Projectile import Projectile
class Cannon():
    def __init__(self):
        self.sprite = object
        self.radius = 10
        self.projectileImage = simplegui._load_local_image("Resources/images/Laser.png")
        self.time = 1.5
        self.bounce = True
        self.baseDamage = 10
        self.image = simplegui._load_local_image("Resources/images/Cannon.png")


    def fire(self,toPos,projectiles,lasers,fromPos,owner,timer=1.5,scaleState=False,image=None):
        if image==None: image=self.projectileImage
        vel = toPos.copy().subtract(fromPos).getNormalized()*30
        projectiles.append( Projectile(vel,fromPos.copy(),self.radius,timer,self.bounce,self.baseDamage,owner,scaleState,image))

