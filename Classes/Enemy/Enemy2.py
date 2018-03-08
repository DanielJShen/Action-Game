from Classes.Enemy.Line import Line
from Classes.Vector import Vector
from Classes.Abilities.Cannon import Cannon
from Classes.Enemy.EnemySuper import EnemySuper
from Classes.Enemy.Enemy2IMG import Enemy2IMG

class Enemy2(EnemySuper):
    def __init__(self,pos:Vector,color,type,bat):
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
        self.enemyIMG = Enemy2IMG(self.pos, bat,330,232,9,4,[0,2],100,100,0)
        self.updateLOS()

    def spriteUpdate(self,character,enemy):
        self.enemyIMG.updateDirection(character,enemy)
        self.enemyIMG.update()

    def updateLOS(self):
        self.normalGen = Vector((self.pos.x + self.normalLine.x), (self.pos.y + self.normalLine.y))
        self.normalBoundary = Line(self.pos, self.normalGen, "blue")

        self.leftgen = Vector((self.pos.x + self.lineLeftGen.x), (self.pos.y + self.lineLeftGen.y))
        self.leftBoundary = Line(self.pos,self.leftgen,"white")

        self.rightgen = Vector((self.pos.x + self.lineRightGen.x), (self.pos.y + self.lineRightGen.y))
        self.rightBoundary = Line(self.pos, self.rightgen, "white")


    def update(self,zoom,player):
        self.updateLOS()
        self.inLOS(player)
        self.updateSoundDistance(player)

        self.vel.multiply(0.90)
        self.vel.add(self.direction.getNormalized()*self.speed)
        self.pos.add(self.vel*zoom)

    def drawLos(self, canvas, offset):
        canvas.draw_polygon([((self.leftBoundary.pA.x + offset.x), ((self.leftBoundary.pA.y-25) + offset.y)),
                             ((self.leftBoundary.pB.x + offset.x), (self.leftBoundary.pB.y + offset.y)),
                             ((self.rightBoundary.pB.x + offset.x), (self.rightBoundary.pB.y + offset.y)), ], 0, "white",
                            self.losColour)

    def draw(self,canvas,offset,bat,enemy,player):
        self.drawLos(canvas,offset)
        self.enemyIMG.draw(canvas,offset)
        # canvas.draw_circle((self.pos+offset).getP(), self.radius, 1, self.color, self.color)

    def attack(self,player,health):
        if (self.radius + player.radius) + 20 >= (self.pos-player.pos).length():
            self.direction = Vector(0, 0)
            health.damageTaken()
            player.vel.add(player.vel.getNormalized()*20)
            player.health -= 10
