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
        # canvas.draw_circle( self.pos1.getP(), self.thickness-1, 1, "white", "white")
        # canvas.draw_circle( self.pos2.getP(), self.thickness-1, 1, "white", "white")
    def update(self):
        self.pos.add(self.vel)

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
        seperation = self.pos1.copy().subtract(projectile.pos)
        seperation2 = self.pos2.copy().subtract(projectile.pos)
        radius = math.sqrt(self.thickness**2 + self.thickness**2)

        if (radius + projectile.radius) >= seperation.length():

            # Calculate how to free Object
            direction: Vector = projectile.vel.copy().negate().normalize()
            distance = ((projectile.radius + radius) - seperation.length()) / max(math.sin(self.line.getNormalized().getNormal().angle(direction)), 0.02)

            # Reflect
            projectile.vel.reflect(self.line.getNormalized())

            # Free Object
            projectile.pos.add(direction.copy().multiply(distance))  # Going back by ammount overlapped
            projectile.pos.add(projectile.vel.getNormalized() * distance)  # Adding lost distance after

        if (radius + projectile.radius) >= seperation2.length():
            # Calculate how to free Object
            direction: Vector = projectile.vel.copy().negate().normalize()
            distance = ((projectile.radius + radius) - seperation2.length()) / max(math.sin(self.line.getNormalized().getNormal().angle(direction)), 0.02)

            # Reflect
            projectile.vel.reflect(self.line.getNormalized())

            # Free Object
            projectile.pos.add(direction.copy().multiply(distance))  # Going back by ammount overlapped
            projectile.pos.add(projectile.vel.getNormalized() * distance)  # Adding lost distance after

    def reflect(self,projectile):
                #Calculate how to free Object
                direction:Vector = projectile.vel.copy().negate().normalize()
                distance = ((projectile.radius+self.thickness)-self.distanceTo(projectile))/max(math.sin(self.line.angle(direction)),0.02)

                #Reflect
                normal = self.pos1.copy().subtract(self.pos2).getNormal().normalize()
                projectile.vel.reflect(normal)


                #Free Object
                projectile.pos.add(direction.copy().multiply(distance))#Going back by ammount overlapped
                projectile.pos.add(projectile.vel.getNormalized()*distance)#Adding lost distance after

#The projectile class is the object that is shot by the player e.g a bullet OR LASERS WHOOOOOOOOO
