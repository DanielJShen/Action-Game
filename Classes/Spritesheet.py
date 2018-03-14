from Classes.Vector import Vector

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


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
        self.fr_idx = [-1, -1]
        self.animations = []
        self.currentAnimation = 0

    def addAnimation(self, start, end):
        self.animations.append(Animation(self, start, end))

    def draw(self, canvas):
        canvas.draw_image(self.img, (self.frameWidth * self.fr_idx[0] + self.frameCentreX,
                                     self.frameHeight * self.fr_idx[1] + self.frameCentreY),
                          (self.frameWidth * self.scale, self.frameHeight * self.scale),
                          self.pos.getP(),
                          (self.imgWidth * self.scale, self.imgHeight * self.scale))

    def update(self, pos, offset):
        self.pos = pos + offset
        self.fr_idx = self.animations[self.currentAnimation].nextFrame(self.fr_idx)


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
        if (self.start[0] > fr_idx[0] and self.start[1] >= fr_idx[1]) or (
                self.end[0] < fr_idx[0] and self.end[1] <= fr_idx[1]):
            fr_idx[0] = self.start[0]
            fr_idx[1] = self.start[1]
        return fr_idx
