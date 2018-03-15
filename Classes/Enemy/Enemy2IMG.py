try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


class Enemy2IMG:
    def __init__(self, pos, IMG,width,height,column,row,frameIndex,scaleX,scaleY,rotate):
        self.pos = pos
        self.IMG = IMG
        width = width
        height = height
        self.frameIndex = frameIndex
        self.pos = pos
        self.column = column
        self.rows = row
        self.frameWidth = width / self.column
        self.frameHeight = height / self.rows
        self.frameCentreX = self.frameWidth / 2
        self.frameCentreY = self.frameHeight / 2
        self.scaleX = scaleX
        self.scaleY = scaleY
        self.rotate = rotate

    def draw(self, canvas,offset):
        canvas.draw_image(self.IMG, (self.frameWidth * self.frameIndex[0] + self.frameCentreX,
                                           self.frameHeight * self.frameIndex[1] + self.frameCentreY),
                          (self.frameWidth, self.frameHeight), ((self.pos+offset).getP()),
                          (self.scaleX, self.scaleY),self.rotate
                          )

    def updateDirection(self,player,enemy):
        if (player.pos.x > enemy.pos.x) and (player.pos.y < enemy.pos.y):
            self.frameIndex[1] = 2
        elif (player.pos.y > enemy.pos.y) and (player.pos.x < enemy.pos.x):
            self.frameIndex[1] = 1
        elif (player.pos.x < enemy.pos.x) and (player.pos.y < enemy.pos.y):
            self.frameIndex[1] = 2
        elif (player.pos.y > enemy.pos.y) and (player.pos.x > enemy.pos.x):
            self.frameIndex[1] = 3


    def update(self):
        self.frameIndex[0] = (self.frameIndex[0] + 1) % self.column