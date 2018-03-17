from Classes.Enemy.EnemySuper import EnemySuper
from Classes.Utilities.Vector import Vector
from Classes.Enemy.LynelSprite import LynelSprite
from Classes.MainCharacter import Character
from Classes.Abilities.Cannon import Cannon
from Classes.Enemy.Bat import Bat

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

class LynelBoss(LynelSprite):
    def __init__(self,pos,vel,baseimage,image,fadedBase,death):
        self.trident = False
        self.pos = pos
        self.vel = vel
        self.health = 100
        self.detectedRadius = 500
        self.followRadius = 800
        self.speed = 60
        self.direction = Vector()
        self.ability = Cannon()
        self.incrementalTimer = 0
        self.incrementalTimer2 = 0
        self.incrementalTimer3 = 0
        self.incrementalTimer4 = 0
        self.inBoundary = False
        self.positions = []
        self.enemies = []
        self.health = 1000
        self.radius = 50
        self.spawn = False
        self.boss = LynelSprite(self.pos, baseimage, 175, 300, 3, 6, [0, 2],image, 608, 130, 8, 2, [1, 1], fadedBase, 175, 300, 3, 6, [0, 2],death, 270, 50, 6, 1, [0, 0],0)
        self.start(self.pos, baseimage, 175, 300, 3, 6, [0.2],
                   image, 608, 130, 8  , 2, [1,1], fadedBase, 175, 300, 3, 6, [0, 2],death, 270, 50, 6, 1, [0, 0],0)
        self.moving = False
        self.generator = Vector(0,-200)
        self.draw = False
        self.fireOrb = simplegui._load_local_image('Resources/images/fireOrb.png')
        self.fire = simplegui._load_local_image('Resources/images/fireBall.png')
        self.fireEnabled = False
        self.death = False


    def drawHealthBar(self,canvas,offset):
        canvas.draw_line((390, 50), (1390, 50), 25, "black")
        canvas.draw_line((390, 50), (390+self.health, 50), 25, "Red")

    def updateSprite(self,canvas,offset,player):
        self.boss.updateDirection(player,self.inBoundary,self.spawn,self)
        self.boss.draw(canvas,offset,self.positions,self.spawn,self)

    def spawnBats(self):
        self.spawn = True

    def update(self):
        self.vel.multiply(0.85)
        self.pos.add(self.vel)


    def fireTridents(self,player,projectiles,lasers,trident):
        self.ability.fire(player.pos, projectiles, lasers, self.pos, "enemy",1.5,True,trident)


    def detectionArea(self,player:Character):
        if not self.spawn:
            distanceToPlayer = player.pos.copy().subtract(self.pos)
            if distanceToPlayer.length() >= self.detectedRadius+player.radius:
                self.inBoundary = False
                if self.incrementalTimer2 % 1 == 0:
                    self.positions.append(self.pos.copy())
                    if self.positions.__len__() == 10:
                        self.positions.pop(0)
                    self.incrementalTimer2 = 0
                self.incrementalTimer2 += 1

                if self.incrementalTimer % 30 == 0 and not self.moving:
                    self.moving = True
                    self.vel = distanceToPlayer.getNormalized()*self.speed
                    self.incrementalTimer = 0
                self.incrementalTimer += 1
                self.trident = False

            if self.vel.length() < 5:
                self.moving = False
                self.inBoundary = True
                self.positions = []
                self.vel = Vector(0,0)
                if not distanceToPlayer.length() >= self.detectedRadius+player.radius:
                    self.trident = True

    def drawDetectionArea(self,canvas,offset):
        canvas.draw_circle((self.pos + offset).getP(), self.detectedRadius, 1, "red")
        canvas.draw_circle((self.pos + offset).getP(), self.followRadius, 1, "white")

    def fireBombard(self):
        angle = 360 / 9
        gen = self.generator
        self.vertices = []
        for i in range(9):
            self.vertices.append(self.pos + gen)
            gen.rotate(angle)

    def drawFire(self,canvas,offset,player,projectiles,lasers):
        if not self.fireEnabled:
            self.fireBombard()
            self.fireEnabled = True
        for i in range(9):
            canvas.draw_image(self.fireOrb, (self.fireOrb.get_width() / 2,
                                             self.fireOrb.get_height() / 2),
                              (self.fireOrb.get_width(), self.fireOrb.get_height()), ((self.vertices[i] + offset).getP()),
                              (self.fireOrb.get_width() * 6, self.fireOrb.get_height() * 6), 0
                              )

            if self.incrementalTimer3 % 50 == 0:
                self.ability.fire(player.pos, projectiles, lasers, self.vertices[i], "enemy", 0.5, True, self.fire)
                self.incrementalTimer3 = 0

            self.incrementalTimer3 += 1
