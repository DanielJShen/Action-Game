from Classes.Utilities.Vector import Vector
class Projectile:
    def __init__(self,vel,pos,radius,timer,bounceState,damage,owner,image="green"): #rof is Rate of Fire
        self.vel:Vector = vel
        self.pos:Vector = pos
        self.radius = radius
        self.image = image
        self.timer = round(timer*60) #TODO use
        self.bounceState = bounceState #Whether an object bounces of the wall
        self.damage = damage #TODO use
        self.owner = owner #TODO use

    def draw(self,canvas,offset):
        if self.image == "green":
            canvas.draw_circle((self.pos+offset).getP(),self.radius,0.001,self.image,self.image)
        else:
            rotation = self.vel.getNormalized().angleToX()
            canvas.draw_image(self.image, (self.image.get_width()/2,
                                         self.image.get_height()/2),
                              (self.image.get_width(), self.image.get_height()), ((self.pos + offset).getP()),
                              (self.radius*2, self.radius*2), rotation
                              )
    def update(self,projectiles:list,zoom):
        self.pos.add(self.vel/zoom)
        if self.incrementTimer() <= 0:
            projectiles.pop(projectiles.index(self))


    def bounce(self): #Checks if the projectile hits a wall
        return True

    def incrementTimer(self): #Used to end a projectile life
        self.timer = self.timer - 1
        return self.timer


#The projectile class is the object that is shot by the player e.g a bullet OR LASERS WHOOOOOOOOO
