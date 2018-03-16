try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Classes.Objects.Sprite import Sprite
from Classes.Objects.Sprite import SpriteGroup
from Classes.Objects.Wall import Wall
from Classes.Objects.Wall import WallBox
from Classes.Utilities.Vector import Vector
import math
from Classes.Enemy.LynelBoss import LynelBoss
from Classes.Enemy.FireEnemy import FireEnemy
from Classes.Enemy.Bat import Bat
from Classes.Enemy.Enemy2IMG import Enemy2IMG

class LynelMap:
    def start(self,frame:simplegui.Frame,width,height):
        self.sprites = []
        self.walls = []
        self.enemies = []

        self.zoom = 3
        self.mapSize = Vector(width*self.zoom,height*self.zoom)
        self.startPos = Vector(300,450)

        #Load Images
        Ganon = simplegui._load_local_image("Resources/images/GanonStand.png")
        GanonTrans = simplegui._load_local_image("Resources/images/GanonTrident.png")
        image_background = simplegui._load_local_image('Resources/images/Blank.png')

        #Background
        frame.set_canvas_background("#0170FE")
        self.sprites.append( Sprite( self.mapSize/2,image_background, self.mapSize.getP()))

        #Enemies
        self.Boss = LynelBoss(Vector(500,500),Vector(0,0),Ganon,GanonTrans)

        #Walls
        wallWidth = 50
        lineHalfWidth = 8
        wallPoints1 = [(90,70),(2740,70),(2740,1630),(90,1630),(90,70)]
        # wallPoints2 = [(165,680),(580,670),(570,290),(1120,320),(1130,710),(4170,725)]
        wallPoints = [wallPoints1]
        for wallPoint in wallPoints:
            for i in range(wallPoint.__len__()-1):
                pos1 = Vector(wallPoint[i][0],wallPoint[i][1])
                pos2 = Vector(wallPoint[i+1][0],wallPoint[i+1][1])
                self.walls.append(Wall(lineHalfWidth, pos1,pos2))

    def draw(self,canvas,offset):
        self.Boss.drawHealthBar(canvas,offset)
        for sprite in self.sprites:
            sprite.draw(canvas,offset)