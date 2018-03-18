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
        self.pickups = []
        self.hearts = []
        self.defeated = False

        self.zoom = 3
        self.mapSize = Vector(4800,2700)
        self.startPos = Vector(400, 1100)

        #Load Images
        image_background = simplegui._load_local_image('Resources/images/mahadmap.png')
        Ganon = simplegui._load_local_image("Resources/images/GanonStand.png")
        GanonTrans = simplegui._load_local_image("Resources/images/GanonTrident.png")
        fadedGanon = simplegui._load_local_image("Resources/images/GanonStandFaded.png")
        death = simplegui._load_local_image("Resources/images/death.png")
        image_teleporter = simplegui._load_local_image('Resources/images/blue_power_up.png')

        #Background
        frame.set_canvas_background("#cf1020")
        self.sprites.append(Sprite(self.mapSize / 2, image_background, self.mapSize.getP()))

        #Teleporter

        if self.defeated:
            self.teleporter = Sprite(Vector(width * self.zoom / 2, height * self.zoom / 2) + Vector(1500, 0),
                                     image_teleporter, [150, 150])
            self.sprites.append(self.teleporter)

        #Enemies
        self.Boss = LynelBoss(Vector(3325,1250),Vector(0,0),Ganon,GanonTrans,fadedGanon,death)

        # Walls
        wallWidth = 50
        lineHalfWidth = 8
        wallPoints1 = [(267, 939), (540, 941), (540, 1111), (2245, 1111),(2246,219),(4349,219),(4349,2233),(2245,2233),(2245,1244),(540,1228),(540,1378),(268,1378),(267,939)]
        wallPoints = [wallPoints1]
        for wallPoint in wallPoints:
            for i in range(wallPoint.__len__() - 1):
                pos1 = Vector(wallPoint[i][0], wallPoint[i][1])
                pos2 = Vector(wallPoint[i + 1][0], wallPoint[i + 1][1])
                self.walls.append(Wall(lineHalfWidth, pos1, pos2))

    def draw(self,canvas,offset, character, inventory):
        for sprite in self.sprites:
            sprite.draw(canvas,offset)
        if not self.Boss.death:
            self.Boss.drawHealthBar(canvas, offset)
            canvas.draw_text("GANON", [390,30], 30, "white")