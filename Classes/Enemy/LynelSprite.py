class LynelSprite:
    def __init__(self, pos, IMG, width, height, column, row, frameIndex,
                 sIMG, swidth, sheight, scolumn, srow, sframeIndex,tIMG, twidth, theight, tcolumn, trow, tframeIndex,
                 dIMG, dwidth, dheight, dcolumn, drow, dframeIndex, rotate):

        self.start( pos, IMG, width, height, column, row, frameIndex,
                 sIMG, swidth, sheight, scolumn, srow, sframeIndex,tIMG, twidth, theight, tcolumn, trow, tframeIndex,
                    dIMG, dwidth, dheight, dcolumn, drow, dframeIndex, rotate)

    def start(self, pos, IMG, width, height, column, row, frameIndex,
                 sIMG, swidth, sheight, scolumn, srow, sframeIndex, tIMG, twidth, theight, tcolumn, trow, tframeIndex,
              dIMG, dwidth, dheight, dcolumn, drow, dframeIndex, rotate):
        self.pos = pos

        self.trident = sIMG
        self.IMG = IMG
        self.sprites = [IMG,sIMG,tIMG,dIMG]
        self.incrementalTimer1 = 0
        width = width
        height = height
        sWidth = swidth
        sHeight = sheight
        tWidth = twidth
        tHeight = theight
        dWidth = dwidth
        dHeight = dheight

        self.frameIndexD = frameIndex
        self.frameIndexT = sframeIndex
        self.frameIndex = [self.frameIndexD,self.frameIndexT,tframeIndex,dframeIndex]

        self.column = column
        self.rows = row

        self.sColumn = scolumn
        self.sRows = srow

        self.tColumn = tcolumn
        self.tRows = trow

        self.dColumn = dcolumn
        self.dRows = drow

        self.frameWidth = width / self.column
        self.frameHeight = height / self.rows
        self.frameCentreX = self.frameWidth / 2
        self.frameCentreY = self.frameHeight / 2

        self.sframeWidth = sWidth / self.sColumn
        self.sframeHeight = sHeight / self.sRows
        self.sframeCentreX = self.sframeWidth / 2
        self.sframeCentreY = self.sframeHeight / 2
        self.sRadius = self.sframeWidth/2

        self.tframeWidth = tWidth / self.tColumn
        self.tframeHeight = tHeight / self.tRows
        self.tframeCentreX = self.tframeWidth / 2
        self.tframeCentreY = self.tframeHeight / 2
        self.tRadius = self.tframeWidth / 2

        self.dframeWidth = dWidth / self.dColumn
        self.dframeHeight = dHeight / self.dRows
        self.dframeCentreX = self.dframeWidth / 2
        self.dframeCentreY = self.dframeHeight / 2
        self.dRadius = self.dframeWidth / 2

        self.frameWidthL = [self.frameWidth,self.sframeWidth,self.tframeWidth,self.dframeWidth]
        self.frameHeightL = [self.frameHeight,self.sframeHeight,self.tframeHeight,self.dframeHeight]
        self.frameCentreXL = [self.frameCentreX,self.sframeCentreX,self.tframeCentreX,self.dframeCentreX]
        self.frameCentreYL = [self.frameCentreY,self.sframeCentreY,self.tframeCentreY,self.dframeCentreY]

        self.current = 0
        self.scaleX = width/self.column*6
        self.scaleY = height/self.rows*6
        self.scaleXA = width / self.column * 4
        self.scaleYA = height / self.rows * 4

        self.scaleXL = [self.scaleXA,self.scaleX,self.scaleXA,dwidth / self.dColumn * 4]
        self.scaleYL = [self.scaleYA,self.scaleY,self.scaleYA,dwidth / self.dColumn * 4]
        self.rotate = rotate
        self.incrementalTimer = 0

    def updateDirection(self,player,boundary,spawn,boss):
        if boss.death and self.frameIndex[3][0] != self.dColumn:
            if self.incrementalTimer1 % 20 == 0:
                print("test")
                self.current = 3
                self.frameIndex[self.current][0] = (self.frameIndex[self.current][0] + 1)
                self.incrementalTimer1 = 0
            self.incrementalTimer1 += 1
        elif not boss.death:
            if boundary and not spawn:
                if (player.pos.y > self.pos.y) and (player.pos.x > self.pos.x - (self.sRadius+20)) and (player.pos.x < self.pos.x + (self.sRadius+20)):
                    self.current = 1
                    self.frameIndexT[1] = 1
                    self.frameIndexT[0] = 4
                elif (player.pos.y < self.pos.y) and (player.pos.x > self.pos.x - (self.sRadius + 20)) and (
                        player.pos.x < self.pos.x + (self.sRadius + 20)):
                    self.current = 1
                    self.frameIndexT[1] = 0
                    self.frameIndexT[0] = 0
                elif (player.pos.y > self.pos.y - (self.sRadius+20)) and (player.pos.y < self.pos.y + (self.sRadius+20)) and (player.pos.x > self.pos.x):
                    self.current = 1
                    self.frameIndexT[1] = 1
                    self.frameIndexT[0] = 2
                elif (player.pos.y > self.pos.y - (self.sRadius+20)) and (player.pos.y < self.pos.y + (self.sRadius+20)) and (player.pos.x < self.pos.x):
                    self.current = 1
                    self.frameIndexT[1] = 1
                    self.frameIndexT[0] = 6

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
            elif spawn:
                self.current = 1
                self.frameIndexT[1] = 1
                if self.incrementalTimer % 10 == 0:
                    self.frameIndexT[0] = (self.frameIndexT[0] + 1) % self.sColumn
                    self.incrementalTimer = 0
                self.incrementalTimer += 1
            else:
                self.current = 0
                self.frameIndexT[1] = 0
                self.frameIndexT[0] = 3

    def draw(self, canvas, offset,positions,spawn,boss):
        if not spawn:
            boss.fireEnabled = False
            for pos in positions:
                canvas.draw_image(self.sprites[2], (
                self.frameWidthL[2] * self.frameIndex[2][0] + self.frameCentreXL[2],
                self.frameHeightL[2] * self.frameIndex[2][1] + self.frameCentreYL[2]),
                                (self.frameWidthL[2], self.frameHeightL[2]),
                                ((pos + offset).getP()),
                                (self.scaleXL[self.current], self.scaleYL[self.current]), self.rotate
                                )

        canvas.draw_image(self.sprites[self.current], (self.frameWidthL[self.current] * self.frameIndex[self.current][0] + self.frameCentreXL[self.current],
                                     self.frameHeightL[self.current] * self.frameIndex[self.current][1] + self.frameCentreYL[self.current]),
                          (self.frameWidthL[self.current], self.frameHeightL[self.current]), ((self.pos + offset).getP()),
                          (self.scaleXL[self.current], self.scaleYL[self.current]), self.rotate
                          )


