try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Classes.Objects.Sprite import Sprite
from Classes.Objects.Wall import Wall
from Classes.Utilities.Vector import Vector
from Classes.Enemy.FireEnemy import FireEnemy
from Classes.Enemy.CannonMob import CannonMob
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
        image_Bat = simplegui._load_local_image('Resources/images/bat.png')
        image_FireEnemy = simplegui._load_local_image('Resources/images/FireEnemy.png')
        image_laser = simplegui._load_local_image("Resources/images/Laser.png")
        image_teleporter = simplegui._load_local_image('Resources/images/blue_power_up.png')
        image_CannonMob = simplegui._load_local_image('Resources/images/CannonMob.png')
        image_speed = simplegui._load_local_image("Resources/images/speed.png")
        image_damage = simplegui._load_local_image("Resources/images/damage.png")
        image_stamina = simplegui._load_local_image("Resources/images/stamina.png")
        image_shotgun = simplegui._load_local_image("Resources/images/Shotgun.png")
        hearts = simplegui._load_local_image("Resources/images/heartsprite.png")
        heartcontainers = simplegui._load_local_image("Resources/images/heartcontainerSprite.png")

        #Background
        frame.set_canvas_background("#0170FE")
        self.sprites.append( Sprite( self.mapSize/2,image_background, self.mapSize.getP()))

        #Teleporter
        self.teleporter = Sprite(Vector(274,2100), image_teleporter, [150, 150])
        self.sprites.append(self.teleporter)

    #Pickups
        #Side Area
        self.pickups.append(Pickup(Vector(width/2,height/2)+Vector(-50,500),image_laser,1,1,"Ability","Laser"))
        self.pickups.append(Pickup(Vector(width/2,height/2)+Vector(1450, -300), image_speed, 1, 1, "powerup", "speed"))
        self.pickups.append(Pickup(Vector(width/2,height/2)+Vector(1450, -150), image_damage, 1, 1, "powerup", "damage"))
        self.pickups.append(Pickup(Vector(width/2,height/2)+Vector(1450, 0), image_speed, 1, 1, "powerup", "speed"))
        self.pickups.append(Pickup(Vector(width/2,height/2)+Vector(2800, -300), image_damage, 1, 1, "powerup", "damage"))
        self.pickups.append(Pickup(Vector(width/2,height/2)+Vector(2800, -150), image_speed, 1, 1, "powerup", "speed"))
        self.pickups.append(Pickup(Vector(width/2,height/2)+Vector(2800, 0), image_damage, 1, 1, "powerup", "damage"))
        self.pickups.append(Pickup(Vector(width/2,height/2)+Vector(2800, 150), hearts, 4, 1, "powerup", "heart",True))

        #Pathway
        self.pickups.append(Pickup(Vector(width/2,height/2)+Vector(-460,1300),image_shotgun,1,1,"Ability","Shotgun"))

        self.pickups.append(Pickup(Vector(width/2,height/2)+Vector(115, -250), image_stamina, 1, 1, "powerup", "stamina"))

        self.pickups.append(Pickup(Vector(width/2,height/2)+Vector(900, -155), image_stamina, 1, 1, "powerup", "stamina"))
        self.pickups.append(Pickup(Vector(width/2,height/2)+Vector(950, -155), image_stamina, 1, 1, "powerup", "stamina"))
        self.pickups.append(Pickup(Vector(width/2,height/2)+Vector(1000, -155), image_stamina, 1, 1, "powerup", "stamina"))

        self.pickups.append(Pickup(Vector(width/2,height/2)+Vector(2100, -50), image_stamina, 1, 1, "powerup", "stamina"))
        self.pickups.append(Pickup(Vector(width/2,height/2)+Vector(2100, -200), image_stamina, 1, 1, "powerup", "stamina"))


        self.pickups.append(Pickup(Vector(width/2,height/2)+Vector(1900, 450), image_stamina, 1, 1, "powerup", "stamina"))
        self.pickups.append(Pickup(Vector(width/2,height/2)+Vector(1700, 450), image_stamina, 1, 1, "powerup", "stamina"))
        self.pickups.append(Pickup(Vector(width/2,height/2)+Vector(1400, 450), image_stamina, 1, 1, "powerup", "stamina"))
        self.pickups.append(Pickup(Vector(width/2,height/2)+Vector(1200, 450), image_stamina, 1, 1, "powerup", "stamina"))
        self.pickups.append(Pickup(Vector(width/2,height/2)+Vector(1000, 450), image_stamina, 1, 1, "powerup", "stamina"))

        #Pathway2
        self.pickups.append(Pickup(Vector(width/2,height/2)+Vector(1100, 1150), image_speed, 1, 1, "powerup", "speed"))
        self.pickups.append(Pickup(Vector(width/2,height/2)+Vector(1150, 1150), image_damage, 1, 1, "powerup", "damage"))
        self.pickups.append(Pickup(Vector(width/2,height/2)+Vector(1200, 1150), hearts, 4, 1, "powerup", "heart",True))
        self.pickups.append(Pickup(Vector(width/2,height/2)+Vector(1250, 1150), image_speed, 1, 1, "powerup", "speed"))
        self.pickups.append(Pickup(Vector(width/2,height/2)+Vector(1300, 1150), image_damage, 1, 1, "powerup", "damage"))
        self.pickups.append(Pickup(Vector(width/2,height/2)+Vector(1350, 1150), hearts, 4, 1, "powerup", "heart",True))

    #Enemies
        #Beginning
        self.enemies.append(FireEnemy(Vector(640, 110), "Red", "Sniper", image_FireEnemy,[0,1],230))
        self.enemies.append(CannonMob(Vector(width / 2, height / 2) + Vector(400, 10), "Blue", "Sniper", image_CannonMob, [0, 0],0))
        #Side Area
        self.enemies.append(FireEnemy(Vector(width/2,height/2)+Vector(1600, -300), "Red", "Sniper", image_FireEnemy,[0,1],95))
        self.enemies.append(FireEnemy(Vector(width/2,height/2)+Vector(1600, -150), "Red", "Sniper", image_FireEnemy,[0,1],100))
        self.enemies.append(FireEnemy(Vector(width/2,height/2)+Vector(1600, 0), "Red", "Sniper", image_FireEnemy,[0,2],60))
        self.enemies.append(Bat(Vector(width/2,height/2)+Vector(2600, -300), "Blue", "Melee", image_Bat,[0,3],250))
        self.enemies.append(Bat(Vector(width/2,height/2)+Vector(2600, -150), "Blue", "Melee", image_Bat, [0, 3], 280))
        self.enemies.append(Bat(Vector(width/2,height/2)+Vector(2600, 0), "Blue", "Melee", image_Bat, [0, 1], 275))
        #Guarding Laser
        self.enemies.append(Bat(Vector(width/2,height/2)+Vector(100, 375), "Blue", "Melee", image_Bat,[0,3],100))
        self.enemies.append(Bat(Vector(width/2,height/2)+Vector(100, 475), "Blue", "Melee", image_Bat, [0, 3], 80))
        self.enemies.append(Bat(Vector(width/2,height/2)+Vector(100, 575), "Blue", "Melee", image_Bat, [0, 1], 90))
        #Pathwaysprites
        self.enemies.append(FireEnemy(Vector(width / 2, height / 2)+Vector(-50, 750), "Red", "Sniper", image_FireEnemy,[0,2],120))
        self.enemies.append(Bat(Vector(4040, 1080), "Blue", "Melee", image_Bat, [0, 3], 160))
        self.enemies.append(Bat(Vector(3900, 1420), "Blue", "Melee", image_Bat, [0, 1], 260))
        #Pathway2
        self.enemies.append(FireEnemy(Vector(width/2,height/2)+Vector(-200, 1150), "Red", "Sniper", image_FireEnemy,[0,1],270))
        self.enemies.append(FireEnemy(Vector(width/2,height/2)+Vector(100, 1150), "Red", "Sniper", image_FireEnemy,[0,2],250))
        self.enemies.append(Bat(Vector(width/2,height/2)+Vector(1000, 1150), "Blue", "Melee", image_Bat, [0, 3], 120))
        self.enemies.append(Bat(Vector(width/2,height/2)+Vector(1500, 1150), "Blue", "Melee", image_Bat, [0, 1], 200))
        self.enemies.append(FireEnemy(Vector(2620, 1810), "Red", "Sniper", image_FireEnemy,[0,1],270))

        self.enemies.append(FireEnemy(Vector(width/2,height/2)+Vector(1800, 1650), "Red", "Sniper", image_FireEnemy,[0,1],180))
        self.enemies.append(FireEnemy(Vector(width/2,height/2)+Vector(2000, 1650), "Red", "Sniper", image_FireEnemy,[0,1],180))
        self.enemies.append(FireEnemy(Vector(width/2,height/2)+Vector(2200, 1650), "Red", "Sniper", image_FireEnemy,[0,1],180))
        self.enemies.append(FireEnemy(Vector(width/2,height/2)+Vector(2400, 1650), "Red", "Sniper", image_FireEnemy,[0,1],180))
        self.enemies.append(Bat(Vector(width/2,height/2)+Vector(1550, 2050), "Blue", "Melee", image_Bat, [0, 3], 0))
        self.enemies.append(Bat(Vector(width/2,height/2)+Vector(1650, 2050), "Blue", "Melee", image_Bat, [0, 1], 0))




        #Walls
        wallWidth = 50
        lineHalfWidth = 8
        wallPoints1 = [(90, 70), (4740, 70), (4740, 2630), (90, 2630), (90, 70)]
        wallPoints2 = [(90, 670), (570, 670), (570, 290), (650, 290), (650, 320), (1130, 320), (1130, 725), (4170, 725)]
        wallPoints3 = [(1638, 154), (1638, 379), (1855, 379), (1855, 154),(1638, 154)]
        wallPoints4 = [(2169, 72), (2169, 537), (2809, 537)]
        wallPoints5 = [(3039, 518), (3770, 518), (3770, 71)]
        wallPoints6 = [(3770, 501), (4587, 501), (4587, 1328),(395, 1328),(395,1474),(4160,1474),(4160,1705),(3001,1712)]
        wallPoints7 = [(4086, 834), (4086, 1080),(2992,1080),(2992, 834),(4086, 834)]
        wallPoints8 = [(2913, 737), (2913, 1100),(1783,1100)]
        wallPoints9 = [(1485, 1095), (636, 1095), (636, 752),(1116,752)]
        wallPoints10 = [(634, 1095), (296, 1095), (296, 949), (92, 949)]
        wallPoints11 = [(1638, 1694), (2737, 1694)]
        wallPoints12 = [(89, 1937), (4091, 1937)]
        wallPoints13 = [(4159, 1706), (4313, 1706),(4313,2510),(85,2510)]
        wallPoints14 = [(983, 2329), (2080, 2329)]
        wallPoints15 = [(2558, 2329), (4068, 2329)]
        wallPoints16 = [(1983,310),(2115,310),(2115,427),(1983,427),(1983,310)]
        wallPoints17 = [(1517, 310), (1377, 310), (1377, 430), (1517, 430), (1517, 310)]

        wallPoints = [wallPoints1,wallPoints2,wallPoints3,wallPoints4,wallPoints5,wallPoints6,wallPoints7,
                      wallPoints8,wallPoints9,wallPoints10,wallPoints11,wallPoints12,wallPoints13,
                      wallPoints14,wallPoints15,wallPoints16,wallPoints17]
        for wallPoint in wallPoints:
            for i in range(wallPoint.__len__()-1):
                pos1 = Vector(wallPoint[i][0],wallPoint[i][1])
                pos2 = Vector(wallPoint[i+1][0],wallPoint[i+1][1])
                self.walls.append(Wall(lineHalfWidth, pos1,pos2))

    def draw(self,canvas,offset,character,inventory):
        for sprite in self.sprites:
            sprite.draw(canvas,offset)