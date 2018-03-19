from Classes.Utilities.Vector import Vector
from Classes.Abilities.Shotgun import Shotgun
from Classes.Enemy.EnemySuper import EnemySuper
from Classes.Enemy.Enemy2IMG import Enemy2IMG
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

class CannonMob(EnemySuper):
    def __init__(self,pos:Vector,color,type,img,FrameIndex,rotation=0):
        self.defineVariables(pos,color,type,img,600)

        #Specific to this enemy
        self.speed = 0
        self.health = 100
        self.ability = Shotgun()
        self.enemyIMG = Enemy2IMG(self.pos, img, 77, 50, 3, 2, FrameIndex, 50, 50, 0)
        self.stopDistance = 200
        self.lineLeftGen.rotate(rotation)
        self.normalLine.rotate(rotation)
        self.lineRightGen.rotate(rotation)
        self.updateLOS()
        self.entity = "Cannon"
        self.image_cannon = simplegui._load_local_image('Resources/images/CannonFire.png')

    def fire(self,pos:Vector,projectiles:list,lasers:list):
        self.ability.fire(pos,projectiles,lasers,self.pos,"enemy",1.5,False,self.image_cannon)

    # def healthBar(self,canvas):
    #     line1 = Line(Vector(self.pos.x,self.pos.y-100),Vector(self.pos.x+self.health,self.pos.y),"Red")
    #     line2 = Line(Vector(self.pos.x,self.pos.y-100),Vector(self.pos.x+100,self.pos.y),"white")
    #     line1.draw(canvas)
    #     line2.draw(canvas)


