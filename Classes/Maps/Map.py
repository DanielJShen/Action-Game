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

        self.zoom = 3
        self.mapSize = Vector(width*self.zoom,height*self.zoom)
        self.startPos = Vector(width,height)/2 + Vector(50,125)

        #Load Images
        image_background = simplegui._load_local_image('Resources/images/map.png')
        image_wall = simplegui._load_local_image('Resources/images/wall1.png')
        image_spike = simplegui.load_image('https://opengameart.org/sites/default/files/Spike_Pixel_0.png')

        #Background
        frame.set_canvas_background("#0170FE")
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
            spriteGroup.append(Sprite( Vector(695,460+wallWidth*i) , image_wall , [50,50] ))
        spriteGroup1 = SpriteGroup(spriteGroup)
        spriteGroup1.addTo(self.sprites)

        spriteGroup = []
        for i in range(0,7):
            spriteGroup.append(Sprite( Vector(695+wallWidth*i,460) , image_wall , [50,50] ))
        spriteGroup3 = SpriteGroup(spriteGroup)
        spriteGroup3.addTo(self.sprites)

        spriteGroup = []
        for i in range(0,7):
            spriteGroup.append(Sprite( Vector(695+wallWidth*i,760) , image_wall , [50,50] ))
        spriteGroup4 = SpriteGroup(spriteGroup)
        spriteGroup4.addTo(self.sprites)

        #All walls
        lineHalfWidth = 4
        WallBox(lineHalfWidth,spriteGroup4).addTo(self.walls)
        WallBox(lineHalfWidth,spriteGroup3).addTo(self.walls)
        WallBox(lineHalfWidth,spriteGroup2).addTo(self.walls)
        WallBox(lineHalfWidth,spriteGroup1).addTo(self.walls)

    def draw(self,canvas,offset):
        for sprite in self.sprites:
            sprite.draw(canvas,offset)