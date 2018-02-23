class Projectile:
    def __init__(self,velocity,rof,timer,bounceState,damage): #rof is Rate of Fire
        self.velocity = velocity
        self.rof = rof
        self.timer = timer
        self.bounceState = bounceState #Whether an object bounces of the wall
        self.damage = damage

    def bounce(self): #Checks if the projectile hits a wall
        pass

    def timer(self): #Used to end a projectile life
        pass

#The projectile class is the object which is shot by the player e.g a bullet OR LASERS WHOOOOOOOOO
