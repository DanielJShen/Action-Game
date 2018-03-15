try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Classes.Utilities.Vector import Vector

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

    def draw(self,canvas,offset):
        canvas.draw_image(self.image, self.center, self.dim, (self.pos+offset).getP(), self.size, self.rotation)

class SpriteGroup:
    def __init__(self,sprites):
        self.sprites = sprites

        maxX=sprites[0].pos.x
        minX=sprites[0].pos.x
        maxY=sprites[0].pos.y
        minY=sprites[0].pos.y
        for sprite in sprites:
            maxX = max(sprite.pos.x, maxX)
            minX = min(sprite.pos.x, minX)
            maxY = max(sprite.pos.y, maxY)
            minY = min(sprite.pos.y, minY)

        imageHalfWidth = sprites[0].size[0]/2
        imageHalfHeight = sprites[0].size[1]/2
        self.cornerTopLeft = Vector(minX-imageHalfWidth,minY-imageHalfHeight)
        self.cornerTopRight = Vector(maxX+imageHalfWidth,minY-imageHalfHeight)
        self.cornerBottomRight = Vector(maxX+imageHalfWidth,maxY+imageHalfHeight)
        self.cornerBottomLeft = Vector(minX-imageHalfWidth,maxY+imageHalfHeight)

    def addTo(self,sprites):
        for sprite in self.sprites:
            sprites.append(sprite)