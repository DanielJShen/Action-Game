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
from Classes.Enemy.FireEnemy import FireEnemy
from Classes.Enemy.Bat import Bat

class Map:
    def __init__(self,frame:simplegui.Frame,width,height):
        self.sprites = []
        self.walls = []
        self.enemies = []

        self.zoom = 3
        self.mapSize = Vector(width*self.zoom,height*self.zoom)
        self.startPos = Vector(1500,1900) + Vector(50,125)

        #Load Images
        image_background = simplegui._load_local_image('Resources/images/MAP.png')
        image_wall = simplegui._load_local_image('Resources/images/Blank.png')
        image_Bat = simplegui._load_local_image('Resources/images/Bat.png')
        image_FireEnemy = simplegui._load_local_image('Resources/images/FireEnemy.png')

        #Background
        frame.set_canvas_background("#0170FE")
        self.sprites.append( Sprite( self.mapSize/2,image_background, self.mapSize.getP()))

        #Enemies
        self.enemies.append(FireEnemy(Vector(2620, 1910), "Red", "Sniper", image_FireEnemy,270))
        self.enemies.append(FireEnemy(Vector(900, 1600), "Red", "Sniper", image_FireEnemy))
        self.enemies.append(Bat(Vector(1200, 1000), "Blue", "Malee", image_Bat))

        #All sprites
        wallWidth = 50

        spriteGroup = []
        spriteGroup.append(Sprite(Vector(470, 1350), image_wall, [100, 1900]))
        # spriteGroup.append(Sprite(Vector(100,50) , image_wall , [50,50] ))
        # spriteGroup.append(Sprite(Vector(150,50) , image_wall, [50, 50], math.pi * 45 / 360))

        spriteGroup2 = SpriteGroup(spriteGroup)
        spriteGroup2.addTo(self.sprites)

        spriteGroup = []
        spriteGroup.append(Sprite(Vector(4350, 1350), image_wall, [100, 1900]))
        # spriteGroup.append(Sprite(Vector(100,50) , image_wall , [50,50] ))
        # spriteGroup.append(Sprite(Vector(150,50) , image_wall, [50, 50], math.pi * 45 / 360))

        spriteGroup4 = SpriteGroup(spriteGroup)
        spriteGroup4.addTo(self.sprites)

        # spriteGroup = []
        # for i in range(0,7):
        #     spriteGroup.append(Sprite( Vector(695,460+wallWidth*i) , image_wall , [50,50] ))
        # spriteGroup1 = SpriteGroup(spriteGroup)
        # spriteGroup1.addTo(self.sprites)
        #
        spriteGroup = []
        spriteGroup.append(Sprite( Vector(2400,440) , image_wall , [3900,100] ))
        spriteGroup3 = SpriteGroup(spriteGroup)
        spriteGroup3.addTo(self.sprites)

        spriteGroup = []
        spriteGroup.append(Sprite(Vector(2400, 2250), image_wall, [3900, 100]))
        spriteGroup5 = SpriteGroup(spriteGroup)
        spriteGroup5.addTo(self.sprites)

        spriteGroup = []
        spriteGroup.append(Sprite(Vector(1300, 700), image_wall, [870, 100]))
        spriteGroup6 = SpriteGroup(spriteGroup)
        spriteGroup6.addTo(self.sprites)

        spriteGroup = []
        spriteGroup.append(Sprite(Vector(2300, 620), image_wall, [1200, 80]))
        spriteGroup9 = SpriteGroup(spriteGroup)
        spriteGroup9.addTo(self.sprites)

        spriteGroup = []
        spriteGroup.append(Sprite(Vector(840, 900), image_wall, [80, 500]))
        spriteGroup7 = SpriteGroup(spriteGroup)
        spriteGroup7.addTo(self.sprites)

        spriteGroup = []
        spriteGroup.append(Sprite(Vector(1690, 900), image_wall, [80, 500]))
        spriteGroup12 = SpriteGroup(spriteGroup)
        spriteGroup12.addTo(self.sprites)

        spriteGroup = []
        spriteGroup.append(Sprite(Vector(680, 1200), image_wall, [400, 100]))
        spriteGroup8 = SpriteGroup(spriteGroup)
        spriteGroup8.addTo(self.sprites)

        spriteGroup = []
        spriteGroup.append(Sprite(Vector(1940, 1200), image_wall, [600, 100]))
        spriteGroup11 = SpriteGroup(spriteGroup)
        spriteGroup11.addTo(self.sprites)

        spriteGroup = []
        spriteGroup.append(Sprite(Vector(1380, 1500), image_wall, [1700, 100]))
        spriteGroup10 = SpriteGroup(spriteGroup)
        spriteGroup10.addTo(self.sprites)

        spriteGroup = []
        spriteGroup.append(Sprite(Vector(2240, 1770), image_wall, [1700, 100]))
        spriteGroup13 = SpriteGroup(spriteGroup)
        spriteGroup13.addTo(self.sprites)

        spriteGroup = []
        spriteGroup.append(Sprite(Vector(1500, 2130), image_wall, [2000, 100]))
        spriteGroup14 = SpriteGroup(spriteGroup)
        spriteGroup14.addTo(self.sprites)

        spriteGroup = []
        spriteGroup.append(Sprite(Vector(1430, 1970), image_wall, [80, 300]))
        spriteGroup15 = SpriteGroup(spriteGroup)
        spriteGroup15.addTo(self.sprites)

        spriteGroup = []
        spriteGroup.append(Sprite(Vector(2455, 2050), image_wall, [80, 100]))
        spriteGroup16 = SpriteGroup(spriteGroup)
        spriteGroup16.addTo(self.sprites)

        spriteGroup = []
        spriteGroup.append(Sprite(Vector(3400, 1850), image_wall, [80, 700]))
        spriteGroup17 = SpriteGroup(spriteGroup)
        spriteGroup17.addTo(self.sprites)

        spriteGroup = []
        spriteGroup.append(Sprite(Vector(3400, 850), image_wall, [80, 750]))
        spriteGroup18 = SpriteGroup(spriteGroup)
        spriteGroup18.addTo(self.sprites)

        spriteGroup = []
        spriteGroup.append(Sprite(Vector(2430, 1150), image_wall, [80, 750]))
        spriteGroup19 = SpriteGroup(spriteGroup)
        spriteGroup19.addTo(self.sprites)

        spriteGroup = []
        spriteGroup.append(Sprite(Vector(2890, 900), image_wall, [80, 500]))
        spriteGroup20 = SpriteGroup(spriteGroup)
        spriteGroup20.addTo(self.sprites)

        spriteGroup = []
        spriteGroup.append(Sprite(Vector(2950, 1500), image_wall, [900, 100]))
        spriteGroup21 = SpriteGroup(spriteGroup)
        spriteGroup21.addTo(self.sprites)

        spriteGroup = []
        spriteGroup.append(Sprite(Vector(2550, 1200), image_wall, [300, 100]))
        spriteGroup26 = SpriteGroup(spriteGroup)
        spriteGroup26.addTo(self.sprites)

        spriteGroup = []
        spriteGroup.append(Sprite(Vector(3100, 1200), image_wall, [500, 100]))
        spriteGroup22 = SpriteGroup(spriteGroup)
        spriteGroup22.addTo(self.sprites)

        spriteGroup = []
        spriteGroup.append(Sprite(Vector(3850, 800), image_wall, [800, 100]))
        spriteGroup23 = SpriteGroup(spriteGroup)
        spriteGroup23.addTo(self.sprites)

        spriteGroup = []
        spriteGroup.append(Sprite(Vector(3850, 1900), image_wall, [800, 100]))
        spriteGroup24 = SpriteGroup(spriteGroup)
        spriteGroup24.addTo(self.sprites)

        spriteGroup = []
        spriteGroup.append(Sprite(Vector(4200, 1400), image_wall, [80, 1000]))
        spriteGroup25 = SpriteGroup(spriteGroup)
        spriteGroup25.addTo(self.sprites)

        # spriteGroup = []
        # for i in range(0, 7):
        #     spriteGroup.append(Sprite(Vector(695 + wallWidth * i, 460), image_wall, [50, 50]))
        # spriteGroup3 = SpriteGroup(spriteGroup)
        # spriteGroup3.addTo(self.sprites)
        #
        # spriteGroup = []
        # for i in range(0,7):
        #     spriteGroup.append(Sprite( Vector(695+wallWidth*i,760) , image_wall , [50,50] ))
        # spriteGroup4 = SpriteGroup(spriteGroup)
        # spriteGroup4.addTo(self.sprites)

        #All walls
        lineHalfWidth = 4
        WallBox(lineHalfWidth,spriteGroup4).addTo(self.walls)
        WallBox(lineHalfWidth, spriteGroup13).addTo(self.walls)
        WallBox(lineHalfWidth, spriteGroup14).addTo(self.walls)
        WallBox(lineHalfWidth, spriteGroup15).addTo(self.walls)
        WallBox(lineHalfWidth, spriteGroup16).addTo(self.walls)
        WallBox(lineHalfWidth, spriteGroup17).addTo(self.walls)
        WallBox(lineHalfWidth, spriteGroup18).addTo(self.walls)

        WallBox(lineHalfWidth, spriteGroup19).addTo(self.walls)
        WallBox(lineHalfWidth, spriteGroup20).addTo(self.walls)
        WallBox(lineHalfWidth, spriteGroup21).addTo(self.walls)
        WallBox(lineHalfWidth, spriteGroup22).addTo(self.walls)
        WallBox(lineHalfWidth, spriteGroup23).addTo(self.walls)

        WallBox(lineHalfWidth, spriteGroup24).addTo(self.walls)
        WallBox(lineHalfWidth, spriteGroup25).addTo(self.walls)
        WallBox(lineHalfWidth, spriteGroup26).addTo(self.walls)


        WallBox(lineHalfWidth, spriteGroup12).addTo(self.walls)
        WallBox(lineHalfWidth, spriteGroup11).addTo(self.walls)
        WallBox(lineHalfWidth, spriteGroup10).addTo(self.walls)
        WallBox(lineHalfWidth, spriteGroup9).addTo(self.walls)
        WallBox(lineHalfWidth, spriteGroup8).addTo(self.walls)
        WallBox(lineHalfWidth,spriteGroup3).addTo(self.walls)
        WallBox(lineHalfWidth, spriteGroup7).addTo(self.walls)
        WallBox(lineHalfWidth, spriteGroup4).addTo(self.walls)
        WallBox(lineHalfWidth, spriteGroup5).addTo(self.walls)
        WallBox(lineHalfWidth,spriteGroup2).addTo(self.walls)
        WallBox(lineHalfWidth, spriteGroup6).addTo(self.walls)
        # WallBox(lineHalfWidth,spriteGroup1).addTo(self.walls)

    def draw(self,canvas,offset):
        for sprite in self.sprites:
            sprite.draw(canvas,offset)