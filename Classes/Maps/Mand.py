try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Classes.Objects.Sprite import Sprite
from Classes.Objects.Wall import Wall
from Classes.Utilities.Vector import Vector
from Classes.Enemy.FireEnemy import FireEnemy
from Classes.Enemy.Bat import Bat
from Classes.Pickup import Pickup

class ManMap:
    def start(self,frame,width,height):
        self.sprites = []
        self.walls = []
        self.enemies = []
        self.pickups = []
        self.hearts = []
        self.zoom = 3
        self.mapSize = Vector(4800,2700)
        self.startPos = Vector(300,450)

        #Load Images
        image_background = simplegui._load_local_image('Resources/images/cal.png')
        image_wall = simplegui._load_local_image('Resources/images/Blank.png')
        image_Bat = simplegui._load_local_image('Resources/images/bat.png')
        image_FireEnemy = simplegui._load_local_image('Resources/images/FireEnemy.png')
        image_laser = simplegui._load_local_image("Resources/images/Laser.png")
        image_teleporter = simplegui._load_local_image('Resources/images/blue_power_up.png')

        #Background
        frame.set_canvas_background("#0170FE")
        self.sprites.append( Sprite( self.mapSize/2,image_background, self.mapSize.getP()))

        #Teleporter
        self.teleporter = Sprite(Vector(4800,2700) - Vector(300, 300), image_teleporter, [150, 150])
        self.sprites.append(self.teleporter)

        #Pickups
        self.pickups.append(Pickup(Vector(300,300),image_laser,1,1,"Ability","Laser"))

        #Enemies
        self.enemies.append(FireEnemy(Vector(640, 110), "Red", "Sniper", image_FireEnemy,[0,0],230))
        self.enemies.append(FireEnemy(Vector(2620, 1910), "Red", "Sniper", image_FireEnemy,[0,1],270))
        self.enemies.append(FireEnemy(Vector(900, 1600), "Red", "Sniper", image_FireEnemy,[0,2]))
        self.enemies.append(Bat(Vector(1200, 950), "Blue", "Malee", image_Bat,[0,3],160))
        self.enemies.append(Bat(Vector(4040, 1080), "Blue", "Malee", image_Bat, [0, 3], 160))
        self.enemies.append(Bat(Vector(3900, 1480), "Blue", "Malee", image_Bat, [0, 1], 260))

        #Walls
        wallWidth = 50
        lineHalfWidth = 8
        wallPoints1 = [(90,70),(4740,70),(4740,2630),(90,2630),(90,70)]
        wallPoints2 = [(165,680),(580,670),(570,290),(1120,320),(1130,710),(4170,725)]
        wallPoints = [wallPoints1,wallPoints2]
        for wallPoint in wallPoints:
            for i in range(wallPoint.__len__()-1):
                pos1 = Vector(wallPoint[i][0],wallPoint[i][1])
                pos2 = Vector(wallPoint[i+1][0],wallPoint[i+1][1])
                self.walls.append(Wall(lineHalfWidth, pos1,pos2))

    def draw(self,canvas,offset,character,inventory):
        for sprite in self.sprites:
            sprite.draw(canvas,offset)