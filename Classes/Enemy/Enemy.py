from Classes.Enemy.Line import Line
from Classes.Vector import Vector
from Classes.Abilities.Cannon import Cannon
from Classes.Objects.Projectile import Projectile

class Enemy:
    def __init__(self,pos:Vector,color,length,Line,type):
        self.pos = pos
        self.vel = Vector()
        self.radius = 30
        self.length = length
        self.normalLine = Vector(0,-self.length)
        self.lineLeftGen = Vector(-self.radius*2 ,-self.length)
        self.lineRightGen = Vector(+self.radius*2, -self.length)
        self.line = Line
        self.direction = Vector()
        self.speed = 0.3
        self.health = 100
        self.ability = Cannon()
        self.losColour = 'rgba(255,255,0,0.6)'
        self.found = False
        self.type = type
        self.soundRange = 100
        self.stealthRange = 150
        self.color = color

    def fire(self,pos:Vector,projectiles:list):
        self.ability.fire(pos,projectiles,self.pos,"enemy")

    def drawLos(self,canvas,offset):
        canvas.draw_polygon([((self.leftBoundary.pA.x+offset.x), (self.leftBoundary.pA.y+offset.y)),
                             ((self.leftBoundary.pB.x+offset.x), (self.leftBoundary.pB.y+offset.y)),
                             ((self.rightBoundary.pB.x+offset.x), (self.rightBoundary.pB.y+offset.y)), ], 0, "white",
                            self.losColour)
    def update(self,zoom):
        self.vel.multiply(0.90)
        self.vel.add(self.direction.getNormalized()*self.speed)
        self.pos.add(self.vel*zoom)

    def draw(self,canvas,offset):
        canvas.draw_circle((self.pos+offset).getP(), self.radius, 1, self.color, self.color)

    def healthBar(self,canvas):
        line1 = Line(Vector(self.pos.x,self.pos.y-100),Vector(self.pos.x+self.health,self.pos.y),"Red")
        line2 = Line(Vector(self.pos.x,self.pos.y-100),Vector(self.pos.x+100,self.pos.y),"white")
        line1.draw(canvas)
        line2.draw(canvas)


    def drawLOS(self,canvas):
        self.normalGen = Vector((self.pos.x + self.normalLine.x), (self.pos.y + self.normalLine.y))
        self.normalBoundary = Line(self.pos, self.normalGen, "blue")

        self.leftgen = Vector((self.pos.x + self.lineLeftGen.x), (self.pos.y + self.lineLeftGen.y))
        self.leftBoundary = Line(self.pos,self.leftgen,"white")

        self.rightgen = Vector((self.pos.x + self.lineRightGen.x), (self.pos.y + self.lineRightGen.y))
        self.rightBoundary = Line(self.pos, self.rightgen, "white")

    def ballHitEnemy(self,projectile,inter,projectiles,enemy,enemylist):
        seperation = self.pos-projectile.pos
        if projectile.owner == "player":
            if projectile.radius + self.radius >= seperation.length():
                if not enemy.found and inter.stealthDistance(enemy):
                    self.health -= 100
                elif not enemy.found:
                    enemy.found = True
                    self.health -= projectile.damage
                else:
                    self.health -= projectile.damage
                print(self.health)
                projectiles.pop(projectiles.index(projectile))
                if self.health <= 0:
                    enemylist.pop(enemylist.index(enemy))



    #Add a mirror which will reflect the line of sight
