try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


class HealthIMG:
    def __init__(self, pos, health: list):
        self.pos = pos
        self.health = health
        width = 80
        height = 16
        self.frameIndex = [0, 0]
        self.pos = pos
        self.column = 5
        self.rows = 1
        self.frameWidth = width / self.column
        self.frameHeight = height / self.rows
        self.frameCentreX = self.frameWidth / 2
        self.frameCentreY = self.frameHeight / 2
        self.scaleX = 50
        self.scaleY = 50

    def draw(self, canvas,offset):
        canvas.draw_image(self.health, (self.frameWidth * self.frameIndex[0] + self.frameCentreX,
                                           self.frameHeight * self.frameIndex[1] + self.frameCentreY),
                          (self.frameWidth, self.frameHeight), ((self.pos).getP()),
                          (self.scaleX, self.scaleY)
                          )

