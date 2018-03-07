from Classes.Enemy.Line import Line
from Classes.Vector import Vector
from Classes.Abilities.Cannon import Cannon
from Classes.Objects.Projectile import Projectile

class Enemy2:
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

        self.updateLOS()

    def fire(self,pos:Vector,projectiles:list):
        self.ability.fire(pos,projectiles,self.pos,"enemy")


    def inLOS(self,player):
        leftVision:Vector = self.pos.copy().subtract(self.leftgen)
        rightVision:Vector = self.pos.copy().subtract(self.rightgen)
        playerVector = self.pos-player.pos

        if self.length >= playerVector.length():
            if playerVector.angleToX() >= leftVision.angleToX() and playerVector.angleToX() <= rightVision.angleToX():
                self.found = True
                self.normalBoundary.color = "red"
        elif self.length*2 < playerVector.length():
            self.found = False

    def updateLOS(self):
        self.normalGen = Vector((self.pos.x + self.normalLine.x), (self.pos.y + self.normalLine.y))
        self.normalBoundary = Line(self.pos, self.normalGen, "blue")

        self.leftgen = Vector((self.pos.x + self.lineLeftGen.x), (self.pos.y + self.lineLeftGen.y))
        self.leftBoundary = Line(self.pos,self.leftgen,"white")

        self.rightgen = Vector((self.pos.x + self.lineRightGen.x), (self.pos.y + self.lineRightGen.y))
        self.rightBoundary = Line(self.pos, self.rightgen, "white")

    def updateSoundDistance(self,player):
        if self.soundRange >= (self.pos-player.pos).length():
            self.found = True

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

    def draw(self,canvas,offset):
        self.drawLos(canvas,offset)
        canvas.draw_circle((self.pos+offset).getP(), self.radius, 1, self.color, self.color)

    def healthBar(self,canvas):
        line1 = Line(Vector(self.pos.x,self.pos.y-100),Vector(self.pos.x+self.health,self.pos.y),"Red")
        line2 = Line(Vector(self.pos.x,self.pos.y-100),Vector(self.pos.x+100,self.pos.y),"white")
        line1.draw(canvas)
        line2.draw(canvas)

    def stealthDistance(self,player):
        if self.stealthRange >= (self.pos-player.pos).length() and (self.pos-player.pos).length() > self.soundRange:
            return True
        return False

    def alertDistance(self):
        pass

    def stop(self,player):
        if (self.radius+player.radius)+20 >= (self.pos-player.pos).length():
            self.direction = Vector(0,0)

    def attack(self,player):
        if (self.radius + player.radius) + 20 >= (self.pos-player.pos).length():
            self.direction = Vector(0, 0)
            player.vel.add(player.vel.getNormalized()*20)
            player.health -= 10

    def follow(self,player):
        self.losColour = 'rgba(255,0,0,0.6)'
        playertest = player.pos.copy().subtract(self.pos)
        self.direction = playertest

    def search(self,player):
        playerVector = self.pos-player.pos
        vectorOfLeft = self.leftBoundary.pA - self.leftBoundary.pB
        Vectorleft = self.pos.copy().subtract(vectorOfLeft)
        Left = self.pos.copy().subtract(Vectorleft)

        angleLess = Left.getNormal().angle(playerVector.getNormal())
        vectorToNormal = (self.normalBoundary.pA - self.normalBoundary.pB)
        VectorNormal = self.pos.copy().subtract(vectorToNormal)
        normal = self.pos.copy().subtract(VectorNormal)

        tester = playerVector.getNormal().angle(normal.getNormal())

        if self.found:
            if round(angleLess,2) > round(tester,2):
                self.lineLeftGen.rotate(self.rotation)
                self.normalLine.rotate(self.rotation)
                self.lineRightGen.rotate(self.rotation)
            elif round(angleLess,2) < round(tester,2):
                self.lineLeftGen.rotate(-self.rotation)
                self.normalLine.rotate(-self.rotation)
                self.lineRightGen.rotate(-self.rotation)

    def distanceToEnemy(self,enemy1:Vector,enemy2:Vector):
        distance = enemy1.pos.copy().subtract(enemy2.pos)
        if distance.length() < 55:
            print("Test")

    #Add a mirror which will reflect the line of sight
