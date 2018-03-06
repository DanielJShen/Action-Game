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
    def __init__(self):
        self.sprites = []
        self.walls = []

        #Load Images
        image_background = simplegui._load_local_image('SAND.jpg')
        image_wall = simplegui._load_local_image('Resources/images/wall1.png')
        image_spike = simplegui.load_image('https://opengameart.org/sites/default/files/Spike_Pixel_0.png')

        #Background
        self.sprites.append( Sprite( Vector(800,450),image_background, [1600*3,900*3] ) )

        #All sprites
        wallWidth = 50
        self.sprites.append(Sprite( Vector(50,50) , image_wall , [50,50] ))
        self.sprites.append(Sprite( Vector(100,50) , image_wall , [50,50] ))
        self.sprites.append(Sprite( Vector(150,50) , image_wall, [50, 50], math.pi * 45 / 360))

        spriteGroup = []
        for i in range(0,7):
            spriteGroup.append(Sprite( Vector(200+wallWidth*i,500) , image_wall , [50,50] ))
        spriteGroup1 = SpriteGroup(spriteGroup)
        spriteGroup1.addTo(self.sprites)

        #All walls
        lineHalfWidth = 15
        WallBox(lineHalfWidth,spriteGroup1).addTo(self.walls)

    def draw(self,canvas):
        for sprite in self.sprites:
            sprite.draw(canvas)