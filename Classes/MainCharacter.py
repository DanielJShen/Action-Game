try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Classes.Utilities.Vector import Vector
from Classes.Abilities.Cannon import Cannon
import math
class Character:
    def __init__(self,vel,pos,image,rotation,size=0):
        self.vel:Vector = vel
        self.pos:Vector = pos
        self.speed = 5
        self.maxSpeed = 6
        self.health = 100
        self.activeAbility = Cannon()
        self.image = image
        self.rotation = rotation
        self.directions = ["UP", "LEFT", "DOWN", "RIGHT"]
        self.direction = ""
        self.stamina = 0
        self.staminaColor = "green"
        self.rest = False
        self.staminaReg = 0.5
        self.running = False
        #GodMode for testing
        self.god = True

        if size == 0:
            self.size = self.dim
        else:
            self.size = size

        self.radius = max(size[0]/2,size[1]/2)

    def healthStart(self,healthList, noHearts):
        self.noHearts = noHearts
        self.hearts: list = healthList
        self.heartList = []
        for i in range(0, self.hearts.__len__() + 1):
            self.heart = 1
            self.heartList.append(self.heart)
        self.lastHeart = noHearts
        self.last = noHearts

    def healthInit(self,HealthIMG,heart1):
        noHearts = 3
        self.previous = 50
        self.healthListInit = []
        for i in range(0,noHearts):
            self.healthListInit.append(HealthIMG(Vector(self.previous, 50), heart1))
            self.previous += 50

        self.healthOB = []
        for i in range(0, noHearts):
            self.healthOB.append(self.healthListInit[i])

    def damageTaken(self):
        if self.last > 0:
            if self.heartList[self.last] == 1:
                self.heartList[self.last] = 2
                self.hearts[self.last - 1].frameIndex = [1, 0]
            elif self.heartList[self.last] == 2:
                self.heartList[self.last] = 3
                self.hearts[self.last - 1].frameIndex = [2, 0]
            elif self.heartList[self.last] == 3:
                self.heartList[self.last] = 4
                self.hearts[self.last - 1].frameIndex = [3, 0]
            elif self.heartList[self.last] == 4:
                self.hearts[self.last - 1].frameIndex = [4, 0]
                self.last -= 1
        else:
            print("DEAD")

    def fire(self,pos:Vector,projectiles:list,lasers:list):
        self.activeAbility.fire(pos,projectiles,lasers,self.pos,"player")

    def pickup(self,pickup,inventory):
        if pickup.type == "Ability":
            inventory.enableAbility(pickup.value)

    def draw(self,canvas,offset):
        # canvas.draw_image(self.image, self.center, self.dim, (self.pos+offset).getP(), self.size, self.rotation)
        self.image.draw(canvas,offset,self.pos)

    def update(self,keyboard,zoom, mousePos, offset,frame,timer):
        self.image.updatePlayer(self)
        angle = math.atan2((self.pos + offset).getP()[0] - mousePos[0],
                           (self.pos + offset).getP()[1] - mousePos[1])
        for i in range(len(self.directions)):
            if ((i - 0.5) / len(self.directions) * 2 * math.pi) <= angle <= (
                    (i + 0.5) / len(self.directions) * 2 * math.pi):
                self.direction = self.directions[i]
                #  Split for clarity
            elif ((i - 0.5 - len(self.directions)) / len(self.directions) * 2 * math.pi) <= angle <= (
                    (i + 0.5 - len(self.directions)) / len(self.directions) * 2 * math.pi):
                self.direction = self.directions[i]

        if self.last == 0 and not self.god:
            frame.stop()
            timer.stop()
            import runpy
            file_globals = runpy.run_path("Classes/PyGamesGameOver.py")

        if keyboard.shift:
            if self.rest and self.stamina > 0:
                self.stamina -= self.staminaReg
                self.staminaColor = "red"
                self.running = False
            elif self.rest and self.stamina <= 0:
                self.rest = False

            speed = self.speed
            if self.stamina <= 144 and not self.rest:
                speed = self.speed*2.5
                self.running = True
                self.stamina += 0.5
                self.staminaColor = "green"
            elif not self.rest:
                self.rest = True
                speed = self.speed
                self.running = False
        else:
            self.running = False
            if self.stamina > 0:
                self.stamina -= self.staminaReg
            else:
                self.staminaColor = "green"
                self.rest = False

            speed = self.speed
        if keyboard.right:
            self.vel.add(Vector(speed,0))
        if keyboard.left:
            self.vel.add(Vector(-speed,0))
        if keyboard.up:
            self.vel.add(Vector(0,-speed))
        if keyboard.down:
            self.vel.add(Vector(0,speed))
        self.pos.add(self.vel/zoom)
        self.vel = self.vel.getNormalized() * min(self.vel.length(),self.maxSpeed) * 0.935

class Keyboard:
    def __init__(self):
        self.right = False
        self.left = False
        self.up = False
        self.down = False
        self.space = False
        self.i = False
        self.shift = False

    def keyDown(self, key):
        if key == simplegui.KEY_MAP['d']:
            self.right = True
        if key == simplegui.KEY_MAP['a']:
            self.left = True
        if key == simplegui.KEY_MAP['w']:
            self.up = True
        if key == simplegui.KEY_MAP['s']:
            self.down = True
        if key == simplegui.KEY_MAP['space']:
            self.space = True
        if key == simplegui.KEY_MAP['i']:
            self.i = True
        if key == 17:
            self.shift = True

    def keyUp(self, key):
        if key == simplegui.KEY_MAP['d']:
            self.right = False
        if key == simplegui.KEY_MAP['a']:
            self.left = False
        if key == simplegui.KEY_MAP['w']:
            self.up = False
        if key == simplegui.KEY_MAP['s']:
            self.down = False
        if key == simplegui.KEY_MAP['space']:
            self.space = False
        if key == simplegui.KEY_MAP['i']:
            self.i = False
        if key == 17:
            self.shift = False
