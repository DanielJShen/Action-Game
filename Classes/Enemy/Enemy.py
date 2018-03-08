from Classes.Enemy.Line import Line
from Classes.Vector import Vector
from Classes.Abilities.Cannon import Cannon
from Classes.Enemy.EnemySuper import EnemySuper
from Classes.Enemy.Enemy2IMG import Enemy2IMG

class Enemy(EnemySuper):
    def __init__(self,pos:Vector,color,type,FireEnemy):
        self.pos = pos
        self.vel = Vector()
        self.radius = 30
        self.length = 300
        self.normalLine = Vector(0,-self.length)
        self.lineLeftGen = Vector(-self.radius*2 ,-self.length)
        self.lineRightGen = Vector(+self.radius*2, -self.length)
        self.line = Line
        self.direction = Vector()
        self.looking = False
        self.rotate = False
        self.rotation = 5
        self.losColour = 'rgba(255,255,0,0.6)'
        self.found = False
        self.type = type
        self.soundRange = 100
        self.stealthRange = 150
        self.color = color
        self.speed = 0.3
        self.health = 100
        self.ability = Cannon()
        self.enemyIMG = Enemy2IMG(self.pos, FireEnemy, 530, 172, 9, 4, [0, 2],150,150,0)
        self.updateLOS()

    def spriteUpdate(self,character,enemy):
        self.enemyIMG.updateDirection(character,enemy)
        self.enemyIMG.update()

    def fire(self,pos:Vector,projectiles:list):
        self.ability.fire(pos,projectiles,self.pos,"enemy")

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
        canvas.draw_polygon([((self.leftBoundary.pA.x + offset.x), (self.leftBoundary.pA.y + offset.y)),
                             ((self.leftBoundary.pB.x + offset.x), (self.leftBoundary.pB.y + offset.y)),
                             ((self.rightBoundary.pB.x + offset.x), (self.rightBoundary.pB.y + offset.y)), ], 0, "white",
                            self.losColour)

    def draw(self,canvas,offset,bat,enemy,player):
        self.drawLos(canvas, offset)
        self.enemyIMG.draw(canvas, offset)
        # canvas.draw_circle((self.pos+offset).getP(), self.radius, 1, self.color, self.color)

    # def healthBar(self,canvas):
    #     line1 = Line(Vector(self.pos.x,self.pos.y-100),Vector(self.pos.x+self.health,self.pos.y),"Red")
    #     line2 = Line(Vector(self.pos.x,self.pos.y-100),Vector(self.pos.x+100,self.pos.y),"white")
    #     line1.draw(canvas)
    #     line2.draw(canvas)


