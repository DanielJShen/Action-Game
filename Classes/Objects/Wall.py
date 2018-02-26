from Classes.Vector import Vector
import math
class Wall:
    def __init__(self,vel,pos1,pos2):
        self.vel = vel
        self.pos1 : Vector = pos1
        self.pos2 : Vector = pos2

    def draw(self,canvas):
        canvas.draw_line(self.pos1.getP(), self.pos2.getP(), 2, "white")
    def update(self):
        self.pos.add(self.vel)

    def bounce(self): #Checks if the projectile hits a wall
        pass

    def timer(self): #Used to end a projectile life
        pass

    def reflect(self,projectile):
        #Trigonometry to find the distance from the point to the line
        line1 = self.pos1.copy().subtract(projectile.pos)
        line2 = self.pos2.copy().subtract(self.pos1)
        angle = line1.angle(line2)
        seperation = line1.length()*math.sin(angle)
        #Trig to see if the projectile is past the end of the line
        projectileProjected = projectile.pos.getProj(line2.getNormalized()).length() #projectile.pos.length()*math.cos(projectile.pos.copy().negate().angle(line2))
        point1Projected = self.pos1.getProj(line2.getNormalized()).length() #self.pos1.length()*math.cos(self.pos1.copy().negate().angle(line2))
        point2Projected = self.pos2.getProj(line2.getNormalized()).length() #self.pos2.length()*math.cos(self.pos2.angle(line2))
        option1 = projectileProjected >= point1Projected and projectileProjected <= point2Projected
        option2 = projectileProjected >= point2Projected and projectileProjected <=point1Projected
        if projectile.radius >= seperation and (option1 or option2):
            print('#################')
            #Calculate how to free Object
            direction:Vector = projectile.vel.copy().negate().normalize()
            distance = (projectile.radius-seperation)/math.sin(line2.angle(direction))

            #Reflect
            normal = self.pos1.copy().subtract(self.pos2).getNormal()
            projectile.vel.reflect(normal)

            #Free Object
            projectile.pos.add(direction.multiply(distance))#Going back by ammount overlapped
            projectile.pos.add(projectile.vel.copy().normalize()*distance)#Adding lost distance after
            return True;
        return False;

#The projectile class is the object that is shot by the player e.g a bullet OR LASERS WHOOOOOOOOO
