from Classes.Enemy.Line import Line
from Classes.Vector import Vector
from Classes.Abilities.Cannon import Cannon
from Classes.Enemy.EnemySuper import EnemySuper
from Classes.Enemy.Enemy2IMG import Enemy2IMG

class Bat(EnemySuper):
    def __init__(self,pos:Vector,color,type,image,rotation=0):

        self.defineVariables(pos,color,type,image)

        self.soundRange = 100
        self.stealthRange = 150
        self.speed = 0.6
        self.health = 100
        self.ability = Cannon()
        self.enemyIMG = Enemy2IMG(self.pos, image,330,232,9,4,[0,2],100,100,0)

        self.lineLeftGen.rotate(rotation)
        self.normalLine.rotate(rotation)
        self.lineRightGen.rotate(rotation)

        self.updateLOS()

    def attack(self,player,health):
        if (self.radius + player.radius) + 20 >= (self.pos-player.pos).length():
            self.direction = Vector(0, 0)
            health.damageTaken()
            self.vel.add(self.vel.getNormalized().negate()*12)
            player.health -= 10

    def draw(self,canvas,offset,enemy,player):
        if not self.found:
            self.drawLos(canvas, offset)
        self.enemyIMG.draw(canvas, offset)