from Classes.Enemy.EnemySuper import EnemySuper
from Classes.Utilities.Vector import Vector
from Classes.Enemy.LynelSprite import LynelSprite
from Classes.MainCharacter import Character
from Classes.Abilities.Cannon import Cannon

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

class LynelBoss(LynelSprite):
    def __init__(self,pos,vel,baseimage,image):
        self.trident = False
        self.pos = pos
        self.vel = vel
        self.health = 100
        self.detectedRadius = 500
        self.followRadius = 800
        self.speed = 20
        self.direction = Vector()
        self.ability = Cannon()
        self.incrementalTimer = 0
        self.incrementalTimer2 = 0
        self.positions = []
        self.boss = LynelSprite(self.pos, baseimage, 175, 300, 3, 6, [0, 2],image, 608, 130, 8, 2, [1, 1], 0)
        self.start(self.pos, baseimage, 175, 300, 3, 6, [0.2],
                   image, 608, 130, 8  , 2, [1,1], 0)

    def drawHealthBar(self,canvas,offset):
        canvas.draw_line((390, 50), (1410, 50), 50, "black")
        canvas.draw_line((400, 50), (1400, 50), 25, "Red")

    def updateSprite(self,canvas,offset,player):
        self.boss.updateDirection(player)
        self.drawDupes(canvas, offset)
        self.boss.draw(canvas,offset)


    def update(self):
        self.vel.multiply(0.85)
        self.pos.add(self.vel)


    def fireTridents(self,player,projectiles,lasers,trident):
        self.ability.fire(player.pos, projectiles, lasers, self.pos, "enemy",trident)


    def detectionArea(self,player:Character,canvas,offset):
        distanceToPlayer = player.pos.copy().subtract(self.pos)
        if distanceToPlayer.length() >= self.detectedRadius+player.radius:
            if self.incrementalTimer2 % 5 == 0:
                self.positions.append(self.pos.copy())
                if self.positions.__len__() == 10:
                    self.positions.pop(0)
                print("----------------")

                self.incrementalTimer2 = 0
            self.incrementalTimer2 += 1
            if self.incrementalTimer % 40 == 0:
                self.vel = distanceToPlayer.getNormalized()*self.speed
                self.incrementalTimer = 0
            self.incrementalTimer += 1
            self.trident = False


        else:
            self.positions = []
            self.trident = True
            self.vel = Vector(0,0)

    def drawDupes(self,canvas,offset):
        for pos in self.positions:
            print(pos)
            canvas.draw_image(self.sprites[self.current], (
                self.frameWidthL[self.current] * self.frameIndex[self.current][0] + self.frameCentreXL[self.current],
                self.frameHeightL[self.current] * self.frameIndex[self.current][1] + self.frameCentreYL[self.current]),
                              (self.frameWidthL[self.current], self.frameHeightL[self.current]),
                              ((pos + offset).getP()),
                              (self.scaleX, self.scaleY), self.rotate
                              )

    def drawDetectionArea(self,canvas,offset):
        canvas.draw_circle((self.pos + offset).getP(), self.detectedRadius, 1, "red")
        canvas.draw_circle((self.pos + offset).getP(), self.followRadius, 1, "white")