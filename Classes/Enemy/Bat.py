from Classes.Enemy.Line import Line
from Classes.Vector import Vector
from Classes.Abilities.Cannon import Cannon
from Classes.Enemy.EnemySuper import EnemySuper
from Classes.Enemy.Enemy2IMG import Enemy2IMG

class Bat(EnemySuper):
    def __init__(self,pos:Vector,color,type,image):

        self.defineVariables(pos,color,type,image)

        self.pos = pos
        self.vel = Vector()
        self.radius = 30
        self.length = 300
        self.normalLine = Vector(0,-self.length)
        self.lineLeftGen = Vector(-self.radius*2 ,-self.length)
        self.lineRightGen = Vector(+self.radius*2, -self.length)
        self.direction = Vector()
        self.rotate = False
        self.rotation = 5
        self.losColour = 'rgba(255,255,0,0.6)'
        self.found = False
        self.type = type
        self.soundRange = 100
        self.stealthRange = 150
        self.color = color
        self.speed = 0.6
        self.health = 100
        self.ability = Cannon()
        self.enemyIMG = Enemy2IMG(self.pos, image,330,232,9,4,[0,2],100,100,0)
        self.updateLOS()
        self.stopDistance = 0

    def attack(self,player,health):
        if (self.radius + player.radius) + 20 >= (self.pos-player.pos).length():
            self.direction = Vector(0, 0)
            health.damageTaken()
            player.vel.add(player.vel.getNormalized()*20)
            player.health -= 10
