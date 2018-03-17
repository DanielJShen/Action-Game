from Classes.Utilities.Vector import Vector
from Classes.Abilities.Cannon import Cannon
from Classes.Enemy.EnemySuper import EnemySuper
from Classes.Enemy.Enemy2IMG import Enemy2IMG

class FireEnemy(EnemySuper):
    def __init__(self,pos:Vector,color,type,FireEnemy,FrameIndex,rotation=0):
        self.defineVariables(pos,color,type,FireEnemy)

        #Specific to this enemy
        self.speed = 1.5
        self.health = 100
        self.ability = Cannon()
        self.enemyIMG = Enemy2IMG(self.pos, FireEnemy, 530, 172, 9, 4, FrameIndex, 150, 150, 0)
        self.stopDistance = 200
        self.lineLeftGen.rotate(rotation)
        self.normalLine.rotate(rotation)
        self.lineRightGen.rotate(rotation)
        self.updateLOS()
        self.entity = "fireEnemy"

    # def healthBar(self,canvas):
    #     line1 = Line(Vector(self.pos.x,self.pos.y-100),Vector(self.pos.x+self.health,self.pos.y),"Red")
    #     line2 = Line(Vector(self.pos.x,self.pos.y-100),Vector(self.pos.x+100,self.pos.y),"white")
    #     line1.draw(canvas)
    #     line2.draw(canvas)


