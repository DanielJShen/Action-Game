class LynelSprite:
    def __init__(self, pos, IMG, width, height, column, row, frameIndex,
                 sIMG, swidth, sheight, scolumn, srow, sframeIndex, rotate):

        self.start( pos, IMG, width, height, column, row, frameIndex,
                 sIMG, swidth, sheight, scolumn, srow, sframeIndex, rotate)

    def start(self, pos, IMG, width, height, column, row, frameIndex,
                 sIMG, swidth, sheight, scolumn, srow, sframeIndex, rotate):
        self.pos = pos

        self.trident = sIMG
        self.IMG = IMG
        self.sprites = [IMG,sIMG]

        width = width
        height = height
        sWidth = swidth
        sHeight = sheight

        self.frameIndexD = frameIndex
        self.frameIndexT = sframeIndex
        self.frameIndex = [self.frameIndexD,self.frameIndexT]

        self.column = column
        self.rows = row

        self.sColumn = scolumn
        self.sRows = srow

        self.frameWidth = width / self.column
        self.frameHeight = height / self.rows
        self.frameCentreX = self.frameWidth / 2
        self.frameCentreY = self.frameHeight / 2

        self.sframeWidth = sWidth / self.sColumn
        self.sframeHeight = sHeight / self.sRows
        self.sframeCentreX = self.sframeWidth / 2
        self.sframeCentreY = self.sframeHeight / 2
        self.sRadius = self.sframeWidth/2

        self.frameWidthL = [self.frameWidth,self.sframeWidth]
        self.frameHeightL = [self.frameHeight,self.sframeHeight]
        self.frameCentreXL = [self.frameCentreX,self.sframeCentreX]
        self.frameCentreYL = [self.frameCentreY,self.sframeCentreY]

        self.current = 1
        self.scaleX = width/self.column*6
        self.scaleY = height/self.rows*6

        self.rotate = rotate

    def updateDirection(self,player):
        if (player.pos.y > self.pos.y) and (player.pos.x > self.pos.x - (self.sRadius+10)) and (player.pos.x < self.pos.x + (self.sRadius+10)):
            self.current = 1
            self.frameIndexT[1] = 1
            self.frameIndexT[0] = 4
        elif (player.pos.x > self.pos.x) and (player.pos.y < self.pos.y):
            # print("top-right")
            self.current = 1
            self.frameIndexT[1] = 0
            self.frameIndexT[0] = 1
        elif (player.pos.y > self.pos.y) and (player.pos.x < self.pos.x):
            # print("bottom-left")
            self.current = 1
            self.frameIndexT[1] = 1
            self.frameIndexT[0] = 5
        elif (player.pos.x < self.pos.x) and (player.pos.y < self.pos.y):
            # print("top-left")
            self.current = 1
            self.frameIndexT[1] = 0
            self.frameIndexT[0] = 7
        elif (player.pos.y > self.pos.y) and (player.pos.x > self.pos.x):
            # print("bottom-right")
            self.current = 1
            self.frameIndexT[1] = 1
            self.frameIndexT[0] = 3


    def draw(self, canvas, offset):
        # i = 0
        # while i < self.positions.__len__():
        #     print(self.pos)
        #     canvas.draw_image(self.sprites[self.current], (
        #     self.frameWidthL[self.current] * self.frameIndex[self.current][0] + self.frameCentreXL[self.current],
        #     self.frameHeightL[self.current] * self.frameIndex[self.current][1] + self.frameCentreYL[self.current]),
        #                       (self.frameWidthL[self.current], self.frameHeightL[self.current]),
        #                       ((self.positions[i] + offset).getP()),
        #                       (self.scaleX, self.scaleY), self.rotate
        #                       )
        #     i += 1
        canvas.draw_image(self.sprites[self.current], (self.frameWidthL[self.current] * self.frameIndex[self.current][0] + self.frameCentreXL[self.current],
                                     self.frameHeightL[self.current] * self.frameIndex[self.current][1] + self.frameCentreYL[self.current]),
                          (self.frameWidthL[self.current], self.frameHeightL[self.current]), ((self.pos + offset).getP()),
                          (self.scaleX, self.scaleY), self.rotate
                          )

