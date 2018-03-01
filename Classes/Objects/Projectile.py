from Classes.Vector import Vector
class Projectile:
    def __init__(self,vel,pos,radius,timer,bounceState,damage,owner): #rof is Rate of Fire
        self.vel:Vector = vel
        self.pos:Vector = pos
        self.radius = radius
        self.timer = timer #TODO use
        self.bounceState = bounceState #Whether an object bounces of the wall
        self.damage = damage #TODO use
        self.owner = owner #TODO use

    def draw(self,canvas):
        canvas.draw_circle(self.pos.getP(),self.radius,0.001,'green','green')
    def update(self):
        self.pos.add(self.vel)

    def bounce(self): #Checks if the projectile hits a wall
        return True

    def timer(self): #Used to end a projectile life
        pass


#The projectile class is the object that is shot by the player e.g a bullet OR LASERS WHOOOOOOOOO
