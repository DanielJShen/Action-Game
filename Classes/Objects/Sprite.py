try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Classes.Vector import Vector

class Sprite:
    def __init__(self,pos,image,size=(0,0),rotation=0):
        self.pos:Vector = pos
        self.image:simplegui.Image = image
        self.rotation = rotation
        self.dim = ( self.image.get_width() , self.image.get_height() )
        self.center = ( self.image.get_width()/2 , self.image.get_height()/2 )
        if size == 0:
            self.size = self.dim
        else:
            self.size = size

    def draw(self,canvas):
        canvas.draw_image(self.image, self.center, self.dim, self.pos.getP(), self.size, self.rotation)
    def update(self):
        self.pos.add(self.vel)