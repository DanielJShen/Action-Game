try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Classes.Objects.Sprite import Sprite
from Classes.Objects.Sprite import SpriteGroup
from Classes.Objects.Wall import Wall
from Classes.Objects.Wall import WallBox
from Classes.Vector import Vector
import math

class Map:
    def __init__(self,frame:simplegui.Frame,width,height):
        self.sprites = []
        self.walls = []

        self.mapSize = Vector(width*2,height*2)
        self.startPos = self.mapSize/2

        #Load Images
        image_background = simplegui._load_local_image('Resources/images/grass.jpeg')
        image_wall = simplegui._load_local_image('Resources/images/wall1.png')
        image_spike = simplegui.load_image('https://opengameart.org/sites/default/files/Spike_Pixel_0.png')

        #Background
        frame.set_canvas_background("#2222FF")
        self.sprites.append( Sprite( self.mapSize/2,image_background, self.mapSize.getP() ) )

        #All sprites
        wallWidth = 50

        spriteGroup = []
        spriteGroup.append(Sprite( Vector(50,50) , image_wall , [50,50] ))
        spriteGroup.append(Sprite( Vector(100,50) , image_wall , [50,50] ))
        spriteGroup.append(Sprite( Vector(150,50) , image_wall, [50, 50], math.pi * 45 / 360))

        spriteGroup2 = SpriteGroup(spriteGroup)
        spriteGroup2.addTo(self.sprites)


        spriteGroup = []
        for i in range(0,7):
            spriteGroup.append(Sprite( Vector(200+wallWidth*i,500) , image_wall , [50,50] ))
        spriteGroup1 = SpriteGroup(spriteGroup)
        spriteGroup1.addTo(self.sprites)

        #All walls
        lineHalfWidth = 4
        WallBox(lineHalfWidth,spriteGroup2).addTo(self.walls)
        WallBox(lineHalfWidth,spriteGroup1).addTo(self.walls)

    def draw(self,canvas,offset):
        for sprite in self.sprites:
            sprite.draw(canvas,offset)