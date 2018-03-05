from Classes.Vector import Vector
class Projectile:
    def __init__(self,vel,pos,radius,timer,bounceState,damage,owner): #rof is Rate of Fire
        self.vel:Vector = vel
        self.pos:Vector = pos
        self.radius = radius
        self.timer = timer*60 #TODO use
        self.bounceState = bounceState #Whether an object bounces of the wall
        self.damage = damage #TODO use
        self.owner = owner #TODO use

    def draw(self,canvas,offset):
        canvas.draw_circle((self.pos+offset).getP(),self.radius,0.001,'green','green')
    def update(self,projectiles:list,zoom):
        self.pos.add(self.vel*zoom)
        if self.incrementTimer() <= 0:
            projectiles.pop(projectiles.index(self))

    def bounce(self): #Checks if the projectile hits a wall
        return True

    def incrementTimer(self): #Used to end a projectile life
        self.timer = self.timer - 1
        return self.timer


#The projectile class is the object that is shot by the player e.g a bullet OR LASERS WHOOOOOOOOO
