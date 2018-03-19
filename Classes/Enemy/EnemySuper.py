from Classes.Utilities.Line import Line
from Classes.Utilities.Vector import Vector
from Classes.Abilities.Cannon import Cannon
from Classes.Enemy.Enemy2IMG import Enemy2IMG
import math

class EnemySuper:

    def defineVariables(self,pos:Vector,color,type,image,length=300):
        self.pos = pos
        self.vel = Vector()
        self.radius = 30
        self.length = length
        self.normalLine = Vector(0, -self.length)
        self.lineLeftGen = Vector(-self.radius * 2, -self.length)
        self.lineRightGen = Vector(+self.radius * 2, -self.length)
        self.line = Line
        self.direction = Vector()
        self.looking = False
        self.rotation = 5
        self.losColour = 'rgba(255,255,0,0.6)'
        self.found = False
        self.type = type
        self.soundRange = 100
        self.stealthRange = 150
        self.color = color
        self.speed = 0.45
        self.health = 100
        self.ability = Cannon()
        self.enemyIMG = Enemy2IMG(self.pos, image, 530, 172, 9, 4, [0, 2], 150, 150, 0)
        self.stopDistance = 0
        self.updateLOS()

    def spriteUpdate(self,character,enemy):
        self.enemyIMG.updateDirection(character,enemy)
        self.enemyIMG.update(enemy)

    def fire(self,pos:Vector,projectiles:list,lasers:list):
        self.ability.fire(pos,projectiles,lasers,self.pos,"enemy")

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
        if self.found:
            self.vel.add(self.direction.getNormalized()*self.speed)
        self.pos.add(self.vel/zoom)

    def drawLos(self, canvas, offset):
        canvas.draw_polygon([((self.leftBoundary.pA.x + offset.x), (self.leftBoundary.pA.y + offset.y)),
                             ((self.leftBoundary.pB.x + offset.x), (self.leftBoundary.pB.y + offset.y)),
                             ((self.rightBoundary.pB.x + offset.x), (self.rightBoundary.pB.y + offset.y)), ], 0, "white",
                            self.losColour)

    def draw(self, canvas, offset):
        if not self.found:
            self.drawLos(canvas, offset)
        self.enemyIMG.draw(canvas, offset)

    def stealthDistance(self, player):
        if self.stealthRange >= (self.pos - player.pos).length() and (self.pos - player.pos).length() > self.soundRange:
            return True
        return False

    def alertDistance(self,enemy2):
        distanceVector = self.pos.copy().subtract(enemy2.pos)
        if distanceVector.length() <= (self.radius+enemy2.radius):
            enemy2.vel.x = -enemy2.vel.x
        elif distanceVector.length() < 520 and (enemy2.found or self.found):
            enemy2.found = True
            self.found = True

    def inLOS(self, player):
        leftVision: Vector = self.pos - self.leftgen
        rightVision: Vector = self.pos - self.rightgen
        playerVector = self.pos - player.pos

        # Debuging
        # losAngle = (self.leftgen - self.rightgen).angleToX()
        # canvas.draw_line((self.pos+offset).getP(), (self.pos+offset+Vector(1,0).rotateRad(playerVector.angleToX())).getP(), 9, "black")

        if self.length >= playerVector.length():
            if rightVision.angleToX() >= playerVector.angleToX() >= leftVision.angleToX() :
                self.found = True
                self.normalBoundary.color = 'rgba(255,0,0,1)'
            elif (rightVision.angleToX() < math.pi/2 and leftVision.angleToX() > 3*math.pi/2):
                if(rightVision.angleToX()+2*math.pi >= playerVector.angleToX() >= leftVision.angleToX() \
                    or rightVision.angleToX() >= playerVector.angleToX() >= leftVision.angleToX()-2*math.pi):
                    self.found = True
                    self.normalBoundary.color = 'rgba(255,0,0,1)'
        elif self.length * 2 < playerVector.length() and self.entity != "flameBat":
            self.found = False

    def updateSoundDistance(self, player):
        if self.soundRange >= (self.pos - player.pos).length():
            self.found = True

    def stop(self, player):
        if (self.radius + player.radius) + self.stopDistance >= (self.pos - player.pos).length():
            self.direction = Vector(0, 0)

    def follow(self, player):
        self.losColour = 'rgba(255,0,0,0.2)'
        playertest:Vector = player.pos.copy().subtract(self.pos)
        self.direction = playertest

    def search(self, player):
        playerVector = self.pos - player.pos
        vectorOfLeft = self.leftBoundary.pA - self.leftBoundary.pB
        Vectorleft = self.pos.copy().subtract(vectorOfLeft)
        Left = self.pos.copy().subtract(Vectorleft)

        angleLess = Left.getNormal().angle(playerVector.getNormal())
        vectorToNormal = (self.normalBoundary.pA - self.normalBoundary.pB)
        VectorNormal = self.pos.copy().subtract(vectorToNormal)
        normal = self.pos.copy().subtract(VectorNormal)

        tester = playerVector.getNormal().angle(normal.getNormal())

        playerToLOSAngle = (self.pos - player.pos).angle(self.pos-self.normalGen)*180/math.pi
        if playerToLOSAngle < self.rotation*3:
            rotation = playerToLOSAngle/7
        else:
            rotation = self.rotation

        if self.found:
            if round(angleLess, 2) > round(tester, 2):
                self.lineLeftGen.rotate(rotation)
                self.normalLine.rotate(rotation)
                self.lineRightGen.rotate(rotation)
            elif round(angleLess, 2) < round(tester, 2):
                self.lineLeftGen.rotate(-rotation)
                self.normalLine.rotate(-rotation)
                self.lineRightGen.rotate(-rotation)