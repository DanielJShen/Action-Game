from Classes.Enemy.Line import Line
from Classes.Vector import Vector
from Classes.Objects.Projectile import Projectile
import random

class EnemyInteractions:
    def __init__(self,player):
        self.player = player
        self.looking = False
        self.rotate = False
        self.rotation = 5
        # self.range = self.enemy.length*1.5

    def soundDistance(self,enemy):
        if enemy.soundRange >= self.getPlayerVector(enemy).length():
            enemy.found = True

    def stealthDistance(self,enemy):
        if enemy.stealthRange >= self.getPlayerVector(enemy).length() and self.getPlayerVector(enemy).length() > enemy.soundRange:
            return True
        return False

    def alertDistance(self):
        pass

    def stop(self,enemy):
        if (enemy.radius+self.player.radius)+20 >= self.getPlayerVector(enemy).length():
            enemy.direction = Vector(0,0)

    def attack(self,enemy):
        if (enemy.radius + self.player.radius) + 20 >= self.getPlayerVector(enemy).length():
            enemy.direction = Vector(0, 0)
            self.player.vel.add(self.player.vel.getNormalized()*20)
            self.player.health -= 10

    def updateLOS(self,enemy):
        enemy.losColour = 'rgba(255,0,0,0.6)'

    def follow(self,enemy):
        playertest = self.player.pos.copy().subtract(enemy.pos)
        enemy.direction = playertest

    def search(self,enemy):
        playerVector = self.getPlayerVector(enemy)
        vectorOfLeft = enemy.leftBoundary.pA - enemy.leftBoundary.pB
        Vectorleft = enemy.pos.copy().subtract(vectorOfLeft)
        Left = enemy.pos.copy().subtract(Vectorleft)

        angleLess = Left.getNormal().angle(playerVector.getNormal())
        vectorToNormal = (enemy.normalBoundary.pA - enemy.normalBoundary.pB)
        VectorNormal = enemy.pos.copy().subtract(vectorToNormal)
        normal = enemy.pos.copy().subtract(VectorNormal)

        tester = playerVector.getNormal().angle(normal.getNormal())

        if enemy.found:
            if round(angleLess,2) > round(tester,2):
                enemy.lineLeftGen.rotate(self.rotation)
                enemy.normalLine.rotate(self.rotation)
                enemy.lineRightGen.rotate(self.rotation)
            elif round(angleLess,2) < round(tester,2):
                enemy.lineLeftGen.rotate(-self.rotation)
                enemy.normalLine.rotate(-self.rotation)
                enemy.lineRightGen.rotate(-self.rotation)

    def distanceToEnemy(self,enemy1:Vector,enemy2:Vector):
        distance = enemy1.pos.copy().subtract(enemy2.pos)
        if distance.length() < 55:
            print("Test")

    def getPlayerVector(self,enemy):
        return enemy.pos.copy().subtract(self.player.pos)

    def LOS(self,enemy):
        leftVision:Vector = enemy.pos.copy().subtract(enemy.leftgen)
        rightVision:Vector = enemy.pos.copy().subtract(enemy.rightgen)
        playerVector = self.getPlayerVector(enemy)

        if enemy.length >= playerVector.length():
            if playerVector.angleToX() >= leftVision.angleToX() and playerVector.angleToX() <= rightVision.angleToX():
                enemy.found = True
                enemy.normalBoundary.color = "red"
        elif enemy.length*2 < playerVector.length():
            enemy.found = False

