from Classes.Vector import Vector
import math
class Wall:
    def __init__(self,vel,thickness,pos1,pos2):
        self.vel = vel
        self.thickness = thickness/2
        self.pos1 : Vector = pos1
        self.pos2 : Vector = pos2

        self.line = self.pos2.copy().subtract(self.pos1)

    def draw(self,canvas):
        canvas.draw_polyline([self.pos1.getIntP(), self.pos2.getIntP()], int(self.thickness*2), "white")
        # canvas.draw_circle(self.pos1.getP(), self.thickness-1, 1, "white", "white")
        # canvas.draw_circle(self.pos2.getP(), self.thickness-1, 1, "white", "white")
    def update(self):
        self.pos.add(self.vel)

    def bounce(self): #Checks if the projectile hits a wall
        pass

    def timer(self): #Used to end a projectile life
        pass

    def distanceTo(self,projectile): #Trigonometry to find the distance from the point to the line
        line1 = self.pos1.copy().subtract(projectile.pos)
        angle = line1.angle(self.line)
        return line1.length()*math.sin(angle)
    def inBounds(self,projectile): #Checks if projectile is past the end of the line
        return ((projectile.pos - self.pos1).dot(self.line.getNormalized()) >= 0 and
                (projectile.pos - self.pos2).dot(-self.line.getNormalized()) >= 0)
    def reflectEdge(self,projectile): #Checks if the projectile is colliding with the end of the line
        #End 1
        seperation = self.pos1.copy().subtract(projectile.pos)
        if (self.thickness) + projectile.radius >= seperation.length():
            incSelfPos = self.pos1.copy().add(self.vel.getNormalized()/5)
            incBallPos = projectile.pos.copy().add(projectile.vel.getNormalized()/5)
            newSeperation = incSelfPos.subtract(incBallPos)
            if newSeperation.length() <= seperation.length():
                projectile.vel.reflect(seperation.getNormalized())
        #End 2
        seperation = self.pos2.copy().subtract(projectile.pos)
        if (self.thickness) + projectile.radius >= seperation.length():
            incSelfPos = self.pos2.copy().add(self.vel.getNormalized()/5)
            incBallPos = projectile.pos.copy().add(projectile.vel.getNormalized()/5)
            newSeperation = incSelfPos.subtract(incBallPos)
            if newSeperation.length() <= seperation.length():
                projectile.vel.reflect(seperation.getNormalized())

    def reflect(self,projectile):
        if projectile.radius + self.thickness >= self.distanceTo(projectile):
            if self.inBounds(projectile):
                #Calculate how to free Object
                direction:Vector = projectile.vel.copy().negate().normalize()
                distance = ((projectile.radius+self.thickness)-self.distanceTo(projectile))*math.sin(self.line.angle(direction))

                #Reflect
                normal = self.pos1.copy().subtract(self.pos2).getNormal().normalize()
                projectile.vel.reflect(normal)

                #Free Object
                projectile.pos.add(direction.multiply(distance))#Going back by ammount overlapped
                projectile.pos.add(projectile.vel.copy().normalize()*distance)#Adding lost distance after
        else:
            self.reflectEdge(projectile)

#The projectile class is the object that is shot by the player e.g a bullet OR LASERS WHOOOOOOOOO
