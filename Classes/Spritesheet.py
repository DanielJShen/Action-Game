from Classes.Utilities.Vector import Vector

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

class Spritesheet:
    def __init__(self,newImg,columns,rows,endOffset):
        self.img = newImg;
        self.columns = columns
        self.rows = rows
        self.endOffset = endOffset

        self.pos = Vector(0,0)
        self.frameWidth = self.img.get_width()/self.columns
        self.frameHeight = self.img.get_height()/self.rows
        self.frameCentreX = self.frameWidth/2
        self.frameCentreY = self.frameHeight/2
        self.fr_idx = [0,0]


    def draw(self,canvas,offset,pos,width,height):
        self.pos = pos
        self.imgWidth = width
        self.imgHeight = height
        canvas.draw_image(self.img, (self.frameWidth*self.fr_idx[0]+self.frameCentreX, self.frameHeight*self.fr_idx[1]+self.frameCentreY),
                                    (self.frameWidth, self.frameHeight),
                                    (self.pos+offset).getP(),
                                    (self.imgWidth, self.imgHeight))
    def update(self):
        self.fr_idx[0] = (self.fr_idx[0] + 1) % self.columns
        if self.fr_idx[0] == 0:
            self.fr_idx[1] = (self.fr_idx[1] + 1) % self.rows
        if self.fr_idx[1] == self.rows-1 and self.fr_idx[0] >= self.columns-(self.endOffset-1):
            self.fr_idx[0] = 0
            self.fr_idx[1] = 0