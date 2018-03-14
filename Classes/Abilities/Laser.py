try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Classes.Utilities.LinePosDir import LinePosDir
class Laser():
    def __init__(self):
        self.sprite = object
        self.radius = 10
        self.colour = "#7a14ff"
        self.time = 0.5
        self.bounce = True
        self.baseDamage = 1
        self.image = image_background = simplegui._load_local_image("Resources/images/Laser.png")


    def fire(self,toPos,projectiles,lasers,fromPos,owner):
        lasers.append( LinePosDir(fromPos.copy(),(toPos.copy()-fromPos.copy()).getNormalized(), "red") )

