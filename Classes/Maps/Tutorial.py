try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import SimpleGUICS2Pygame.simplegui_lib_draw
from Classes.Objects.Sprite import Sprite
from Classes.Objects.Sprite import SpriteGroup
from Classes.Objects.Wall import WallBox
from Classes.Utilities.Vector import Vector
from Classes.Enemy.FireEnemy import FireEnemy
from Classes.Enemy.Bat import Bat
from Classes.Pickup import Pickup
from Classes.Objects.heart import heart

class Tutorial:
    def start(self,frame,width,height):
        self.width = width
        self.height = height

        self.sprites = []
        self.walls = []
        self.enemies = []
        self.pickups = []
        self.hearts = []
        self.zoom = 3
        self.mapSize = Vector(width*self.zoom,height*self.zoom)
        self.startPos = Vector(width/2-1200,height/2)

        self.changedAbility = False

        #Load Images
        image_wall = simplegui._load_local_image('Resources/images/wall1.png')
        image_wall2 = simplegui._load_local_image('Resources/images/wall2.png')
        image_teleporter = simplegui._load_local_image('Resources/images/blue_power_up.png')
        image_Bat = simplegui._load_local_image('Resources/images/bat.png')
        image_FireEnemy = simplegui._load_local_image('Resources/images/FireEnemy.png')
        image_laser = simplegui._load_local_image("Resources/images/Laser.png")
        image_speed = simplegui._load_local_image("Resources/images/speed.png")
        image_damage = simplegui._load_local_image("Resources/images/damage.png")
        image_stamina = simplegui._load_local_image("Resources/images/stamina.png")
        image_shotgun = simplegui._load_local_image("Resources/images/Shotgun.png")
        hearts = simplegui._load_local_image("Resources/images/heartsprite.png")

        #Background
        frame.set_canvas_background("#c5ccd8")

        #Pickups
        self.pickups.append(Pickup(Vector(width/2,height/2)+Vector(-1200,-200),image_shotgun,1,1,"Ability","Shotgun"))
        self.pickups.append(Pickup(Vector(width/2,height/2)+Vector(-1200,200),image_shotgun,1,1,"Ability","Shotgun"))
        self.pickups.append(Pickup(Vector(width/2,height/2)+Vector(500,0),image_laser,1,1,"Ability","Laser"))
        self.pickups.append(Pickup(Vector(400,400), image_speed, 1, 1, "powerup", "speed"))
        self.pickups.append(Pickup(Vector(400, 600), image_damage, 1, 1, "powerup", "damage"))
        self.pickups.append(Pickup(Vector(400, 700), image_stamina, 1, 1, "powerup", "stamina"))
        self.pickups.append(Pickup(Vector(500, 700), image_stamina, 1, 1, "powerup", "stamina"))
        self.pickups.append(Pickup(Vector(600, 700), image_stamina, 1, 1, "powerup", "stamina"))
        self.pickups.append(Pickup(Vector(300, 500), hearts, 4, 1, "powerup", "heart"))
        self.pickups.append(Pickup(Vector(500, 500), hearts, 4, 1, "powerup", "heart"))

        #Enemies
        self.enemies.append(FireEnemy(Vector(width/2,height/2)+Vector(400,0), "Red", "Sniper", image_FireEnemy,[0,0],270))
        self.enemies.append(FireEnemy(Vector(width/2,height/2)+Vector(300,250), "Red", "Sniper", image_FireEnemy,[0,1],300))
        self.enemies.append(FireEnemy(Vector(width/2,height/2)+Vector(300,-250), "Red", "Sniper", image_FireEnemy,[0,2],240))
        self.enemies.append(Bat(Vector(width/2,height/2)+Vector(-600,0), "Blue", "Malee", image_Bat,[0,3],270))
        self.enemies.append(Bat(Vector(width/2,height/2)+Vector(1100,0), "Blue", "Malee", image_Bat, [0, 3], 270))
        self.enemies.append(Bat(Vector(width/2,height/2)+Vector(1100,150), "Blue", "Malee", image_Bat, [0, 3], 270))
        self.enemies.append(Bat(Vector(width/2,height/2)+Vector(1100,-150), "Blue", "Malee", image_Bat, [0, 1], 270))

        #All sprites
        wallWidth = 100
        borderLength = 4

        self.teleporter = Sprite(Vector(width / 2, height / 2) + Vector(1350, 0), image_teleporter, [150, 150])
        self.sprites.append(self.teleporter)

        #Border Walls
        spriteGroup = []
        for i in range(0, borderLength*2*4 +1):
            spriteGroup.append(Sprite(Vector(width/2,height/2)+Vector(-wallWidth*borderLength*4 + wallWidth * i, wallWidth*borderLength), image_wall, [100, 100]))
        spriteGroup1 = SpriteGroup(spriteGroup)
        spriteGroup1.addTo(self.sprites)
        spriteGroup = []
        for i in range(0, borderLength*2*4 +1):
            spriteGroup.append(Sprite(Vector(width / 2, height / 2) + Vector(-wallWidth * borderLength*4 + wallWidth * i, -wallWidth*borderLength), image_wall, [100, 100]))
        spriteGroup2 = SpriteGroup(spriteGroup)
        spriteGroup2.addTo(self.sprites)
        spriteGroup = []
        for i in range(0, borderLength*2 +1):
            spriteGroup.append(Sprite(Vector(width / 2, height / 2) + Vector(wallWidth*borderLength*4,-wallWidth * borderLength + wallWidth * i), image_wall, [100, 100]))
        spriteGroup3 = SpriteGroup(spriteGroup)
        spriteGroup3.addTo(self.sprites)
        spriteGroup = []
        for i in range(0, borderLength*2 +1):
            spriteGroup.append(Sprite(Vector(width / 2, height / 2) + Vector(-wallWidth*borderLength*4,-wallWidth * borderLength + wallWidth * i), image_wall, [100, 100]))
        spriteGroup4 = SpriteGroup(spriteGroup)
        spriteGroup4.addTo(self.sprites)

        wallWidth = 50
        wallLength = 5
        # spriteGroup = []
        # for i in range(0, wallLength*2 +1):
        #     spriteGroup.append(Sprite(Vector(width / 2-375, height / 2) + Vector(-wallWidth*wallLength + wallWidth * i, -wallWidth*wallLength), image_wall2, [50, 50]))
        # spriteGroup5 = SpriteGroup(spriteGroup)
        # spriteGroup5.addTo(self.sprites)
        # spriteGroup = []
        # for i in range(0, wallLength*2 +1):
        #     spriteGroup.append(Sprite(Vector(width / 2-375, height / 2) + Vector(-wallWidth*wallLength + wallWidth * i, wallWidth*wallLength), image_wall2, [50, 50]))
        # spriteGroup6 = SpriteGroup(spriteGroup)
        # spriteGroup6.addTo(self.sprites)

        #All walls
        lineHalfWidth = 12
        WallBox(lineHalfWidth,spriteGroup1).addTo(self.walls)
        WallBox(lineHalfWidth,spriteGroup2).addTo(self.walls)
        WallBox(lineHalfWidth,spriteGroup3).addTo(self.walls)
        WallBox(lineHalfWidth,spriteGroup4).addTo(self.walls)
        # WallBox(lineHalfWidth,spriteGroup5).addTo(self.walls)
        # WallBox(lineHalfWidth,spriteGroup6).addTo(self.walls)

    def draw(self,canvas,offset,player,inventory):
        for sprite in self.sprites:
            sprite.draw(canvas,offset)

        if inventory.activeAbility.__class__.__name__ == "Cannon" and not self.changedAbility and player.pos.x < -150:
            canvas.draw_text("Pickup a weapon, then press 'I'",(player.pos.x + offset.x - 600, player.pos.y+offset.y),40,"black")
        elif not inventory.activeAbility.__class__.__name__ == "Cannon":
            self.changedAbility = True

        canvas.draw_text("Walking too close to an Enemy",(self.width/2 - 1000 + offset.x, self.height/2 -150 + offset.y),40,"black")
        canvas.draw_text("will cause them to attack", (self.width / 2 - 960 + offset.x, self.height / 2 - 110 + offset.y), 40, "black")
        canvas.draw_text("Press 'Shift' to Sprint",(self.width/2 - 400 + offset.x, self.height/2  + offset.y),40,"black")