from Classes.Enemy.Line import Line
from Classes.Vector import Vector
from Classes.Objects.Projectile import Projectile

class Enemy:
    def __init__(self,pos:Vector,vel:Vector,length,Line,direction):
        self.pos = pos
        self.vel = Vector()
        self.radius = 20
        self.length = length
        self.normalLine = Vector(0,-self.length)
        self.lineLeftGen = Vector(-self.radius*2 ,-self.length)
        self.lineRightGen = Vector(+self.radius*2, -self.length)
        self.line = Line
        self.direction = Vector()
        self.speed = 0.3
        self.health = 100
        self.losColour = 'rgba(' + str(255) + ',' + str(255) + ',' + str(0) + ',' + str(0.6) + ')'

    def fire(self,pos:Vector,projectiles:list):
        vel = self.pos.copy().subtract(pos)
        newVel = self.pos.copy().subtract(vel).getNormalized()*10
        projectiles.append(Projectile(newVel,self.pos.copy(),10,1,True,10,"enemy"))

    def drawLos(self,canvas,offset):
        canvas.draw_polygon([((self.leftBoundary.pA.x+offset.x), (self.leftBoundary.pA.y+offset.y)),
                             ((self.leftBoundary.pB.x+offset.x), (self.leftBoundary.pB.y+offset.y)),
                             ((self.rightBoundary.pB.x+offset.x), (self.rightBoundary.pB.y+offset.y)), ], 0, "white",
                            self.losColour)
    def update(self):
        self.vel.multiply(0.90)
        self.vel.add(self.direction.getNormalized()*self.speed)
        self.pos.add(self.vel)

    def draw(self,canvas,offset):
        canvas.draw_circle((self.pos+offset).getP(), self.radius, 1, "Red", "Red")

    def healthBar(self):
        self.healthbar = Line(Vector(self.pos.x-20,self.pos.y),Vector(self.pos.x+self.health,self.pos.y),"Red")
        self.healthBack = Line(Vector(self.pos.x-20,self.pos.y),Vector(self.pos.x+100,self.pos.y),"white")

    def drawLOS(self,canvas):
        self.normalGen = Vector((self.pos.x + self.normalLine.x), (self.pos.y + self.normalLine.y))
        self.normalBoundary = Line(self.pos, self.normalGen, "blue")

        self.leftgen = Vector((self.pos.x + self.lineLeftGen.x), (self.pos.y + self.lineLeftGen.y))
        self.leftBoundary = Line(self.pos,self.leftgen,"white")

        self.rightgen = Vector((self.pos.x + self.lineRightGen.x), (self.pos.y + self.lineRightGen.y))
        self.rightBoundary = Line(self.pos, self.rightgen, "white")

    def ballHitEnemy(self,projectile,player,projectiles,enemies):
        seperation = self.pos-projectile.pos
        if projectile.owner == "player":
            if projectile.radius + player.size[0] >= seperation.x and projectile.radius + player.size[1] >= seperation.y:
                self.health -= projectile.damage
                print(self.health)
                projectiles.pop(projectiles.index(projectile))


    #Add a mirror which will reflect the line of sight
