from Classes.Utilities.LinePosDir import LinePosDir
class Laser():
    def __init__(self):
        self.sprite = object
        self.radius = 10
        self.colour = "#7a14ff"
        self.time = 0.5
        self.bounce = True
        self.baseDamage = 10


    def fire(self,toPos,projectiles,lasers,fromPos,owner):
        lasers.append( LinePosDir(fromPos.copy(),(toPos.copy()-fromPos.copy()).getNormalized(), "red") )

