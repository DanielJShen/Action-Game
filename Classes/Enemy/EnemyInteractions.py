from Classes.Enemy.Line import Line
from Classes.Vector import Vector
from Classes.Objects.Projectile import Projectile
import random

class EnemyInteractions:
    def __init__(self,player,enemy,kbd):
        self.player = player
        self.enemy = enemy
        self.keyboard = kbd
        self.found = False
        self.looking = False
        self.rotate = False
        self.rotation = 4

    def updateLOS(self):
        self.enemy.losColour = 'rgba(' + str(255) + ',' + str(0) + ',' + str(0) + ',' + str(0.6) + ')'

    def follow(self):
        playertest = self.player.pos.copy().subtract(self.enemy.pos)
        self.enemy.direction = playertest

    def playerAngle(self):
        centerVector = self.enemy.pos.copy().subtract(self.enemy.normalGen)
        playerVector = self.enemy.pos.copy().subtract(self.player.pos)
        return playerVector.getNormalized().angle(centerVector.getNormalized())

    def search(self,canvas):
        playerVector = self.getPlayerVector()
        vectorOfLeft = self.enemy.leftBoundary.pA - self.enemy.leftBoundary.pB
        Vectorleft = self.enemy.pos.copy().subtract(vectorOfLeft)
        Left = self.enemy.pos.copy().subtract(Vectorleft)

        angleLess = Left.getNormal().angle(playerVector.getNormal())
        normal = self.getVectorToCentreFromPlayer()

        tester = playerVector.getNormal().angle(normal.getNormal())

        if self.looking:
            if round(angleLess,2) > round(tester,2):
                self.enemy.lineLeftGen.rotate(self.rotation)
                self.enemy.normalLine.rotate(self.rotation)
                self.enemy.lineRightGen.rotate(self.rotation)
            elif round(angleLess,2) < round(tester,2):
                self.enemy.lineLeftGen.rotate(-self.rotation)
                self.enemy.normalLine.rotate(-self.rotation)
                self.enemy.lineRightGen.rotate(-self.rotation)


    def getPlayerVector(self):
        return self.enemy.pos.copy().subtract(self.player.pos)

    def getVectorToCentreFromPlayer(self):
        vectorToNormal = (self.enemy.normalBoundary.pA - self.enemy.normalBoundary.pB)
        VectorNormal = self.enemy.pos.copy().subtract(vectorToNormal)
        return self.enemy.pos.copy().subtract(VectorNormal)

    def passive(self):
        self.enemy.direction = Vector(random.randrange(-5,5),random.randrange(-5,5))
        if self.rotate:
            rotate = random.randrange(0,270)
            self.enemy.lineLeftGen.rotate(rotate)
            self.enemy.normalLine.rotate(rotate)
            self.enemy.lineRightGen.rotate(rotate)
            self.rotate = False
        else:
            self.rotate = True

    def LOS(self,canvas):
        FromPointAtoB = self.enemy.pos.copy().subtract(self.player.pos)
        actualPoint = self.enemy.pos.copy().subtract(FromPointAtoB)
        self.line2 = Line(self.enemy.pos, actualPoint,"yellow")
        leftVision:Vector = self.enemy.pos.copy().subtract(self.enemy.leftgen)
        rightVision:Vector = self.enemy.pos.copy().subtract(self.enemy.rightgen)

        playerVector = self.getPlayerVector()
        testerNormal = self.getVectorToCentreFromPlayer().angleToX()
        tester = playerVector.angleToX()

        angleBtwPlayerAndNormal = abs(testerNormal - tester)

        if self.enemy.length >= playerVector.length():
            if playerVector.angleToX() >= leftVision.angleToX() and playerVector.angleToX() <= rightVision.angleToX():
                self.found = True
                self.line2.color = "red"
                self.enemy.normalBoundary.color = "red"
                # if round(angleBtwPlayerAndNormal,3) < 0.09:
                self.looking = False
            else:
                self.looking = True
                self.line2.color = "yellow"
        elif self.enemy.length < playerVector.length():
            self.found = False
            self.looking = False
        else:
            self.line2.color = "yellow"

