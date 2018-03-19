try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Classes.Utilities.Vector import Vector
import math

class Spritesheet:
    def __init__(self, img, columns, rows, scale):
        self.img = img
        self.columns = columns
        self.rows = rows
        self.scale = scale

        self.pos = Vector(0, 0)
        self.imgWidth = self.img.get_width()
        self.imgHeight = self.img.get_height()
        self.frameWidth = self.imgWidth / self.columns
        self.frameHeight = self.imgHeight / self.rows
        self.frameCentreX = self.frameWidth / 2
        self.frameCentreY = self.frameHeight / 2
        self.fr_idx = [0,0]
        self.incrementalTimer = 0
        self.animations = []
        self.currentAnimation = 0
        self.counter = 0

    def addAnimation(self, start, end):
        self.animations.append(Animation(self, start, end))

    def draw(self,canvas,offset,pos,width=None,height=None):
        if width==None and height==None:
            canvas.draw_image(self.img, (self.frameWidth * self.fr_idx[0] + self.frameCentreX,
                                         self.frameHeight * self.fr_idx[1] + self.frameCentreY),
                              (self.frameWidth, self.frameHeight),
                              (self.pos+offset).getP(),
                              (self.imgWidth * self.scale, self.imgHeight * self.scale))
        else:
            canvas.draw_image(self.img, (self.frameWidth * self.fr_idx[0] + self.frameCentreX,
                                         self.frameHeight * self.fr_idx[1] + self.frameCentreY),
                              (self.frameWidth, self.frameHeight),
                              (pos+offset).getP(),
                              (width,height))


    def update(self):
        if self.incrementalTimer % 12 == 0:
            self.fr_idx[0] = (self.fr_idx[0] + 1) % self.columns
            if self.fr_idx[0] == 0:
                self.fr_idx[1] = (self.fr_idx[1] + 1) % self.rows
            if self.fr_idx[1] == self.rows-1 and self.fr_idx[0] >= self.columns:
                self.fr_idx[0] = 0
                self.fr_idx[1] = 0
            self.incrementalTimer = 0
        self.incrementalTimer += 1

    def updatePlayer(self, player):
        self.pos = player.pos
        self.counter -= 1

        update = False
        if not player.running:
            if self.counter%5 == 0:
                update = True
        else:
            if self.counter%2 == 0:
                update = True

        if update:
            if player.vel.length() >= player.speed/2:
                angleToX = player.vel.angleToX()*180/math.pi
                if 315 <= angleToX or angleToX <= 45:
                    self.currentAnimation = 7
                elif 45 <= angleToX <= 135:
                    self.currentAnimation = 4
                elif 135 <= angleToX <= 225:
                    self.currentAnimation = 5
                elif 225 <= angleToX <= 315:
                    self.currentAnimation = 6
                self.fr_idx = self.animations[self.currentAnimation].nextFrame(self.fr_idx)
            else:
                if not self.currentAnimation == 0:
                    self.currentAnimation = 0
                    self.fr_idx = self.animations[self.currentAnimation].nextFrame(self.fr_idx)
                if self.counter <= 0:
                    self.fr_idx = self.animations[self.currentAnimation].nextFrame(self.fr_idx)
                    if self.fr_idx == [0,0]:
                        self.counter = 50


class Animation:

    def __init__(self, spritesheet, start, end):
        self.ss = spritesheet
        self.rows = self.ss.rows
        self.columns = self.ss.columns
        self.start = start
        self.end = end

    def nextFrame(self, fr_idx):
        fr_idx[0] = (fr_idx[0] + 1) % self.columns
        if fr_idx[0] == 0:
            fr_idx[1] = (fr_idx[1] + 1) % self.rows
        if fr_idx[0] < self.start[0] or fr_idx[0] > self.end[0] or fr_idx[1] < self.start[1] or fr_idx[1] > self.end[1]:
            fr_idx[0] = self.start[0]
            fr_idx[1] = self.start[1]
        return fr_idx
