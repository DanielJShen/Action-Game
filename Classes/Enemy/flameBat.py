from Classes.Utilities.Vector import Vector
from Classes.Abilities.Cannon import Cannon
from Classes.Enemy.EnemySuper import EnemySuper
from Classes.Enemy.Enemy2IMG import Enemy2IMG

class flameBat(EnemySuper):
    def __init__(self,pos:Vector,color,type,image,FrameIndex,rotation=0):
        self.defineVariables(pos,color,type,image)
        self.soundRange = 100
        self.stealthRange = 150
        self.speed = 2
        self.health = 50
        self.ability = Cannon()
        self.enemyIMG = Enemy2IMG(self.pos, image,170,20,5,1,FrameIndex,100,100,0)
        self.lineLeftGen.rotate(rotation)
        self.normalLine.rotate(rotation)
        self.lineRightGen.rotate(rotation)
        self.updateLOS()
        self.found = True
        self.entity = "flameBat"

    def attack(self,player,health):
        if (self.radius + player.radius) + 20 >= (self.pos-player.pos).length():
            self.direction = Vector(0, 0)
            health.damageTaken()
            self.vel.add(self.vel.getNormalized().negate()*55)
            player.health -= 10
