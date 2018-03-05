from Classes.Vector import Vector
import math
class Wall:
    def __init__(self,halfThickness,pos1,pos2):
        self.halfThickness = halfThickness
        self.pos1 : Vector = pos1
        self.pos2 : Vector = pos2

        self.line = self.pos2.copy().subtract(self.pos1)

    def draw(self,canvas,offset):
        canvas.draw_polyline([(self.pos1+offset).getIntP(), (self.pos2+offset).getIntP()], int(self.halfThickness * 2), "white")
        canvas.draw_circle((self.pos1+offset).getP(), math.sqrt(self.halfThickness ** 2 + self.halfThickness ** 2), 0.01, "white", "white")
        canvas.draw_circle((self.pos2+offset).getP(), math.sqrt(self.halfThickness ** 2 + self.halfThickness ** 2), 0.01, "white", "white")
    def update(self):
        self.pos.add(self.vel)

    def timer(self): #Used to end a projectile life
        pass

    def distanceTo(self,projectile): #Trigonometry to find the distance from the point to the line
        line1 = self.pos1.copy().subtract(projectile.pos)
        angle = line1.angle(self.line)
        return line1.length()*math.sin(angle)
    def playerInBounds(self,player):
        width = player.size[0]-5
        height = player.size[1]-5
        positions = (player.pos-Vector(width/2,0),player.pos+Vector(width/2,0),player.pos-Vector(0,height/2),player.pos+Vector(0,height/2))
        for pos in positions:
            if ((pos - self.pos1).dot(self.line.getNormalized()) >= 0 and
                (pos - self.pos2).dot(-self.line.getNormalized()) >= 0):
                return True
        return False
    def inBounds(self,projectile): #Checks if projectile is past the end of the line
        return ((projectile.pos - self.pos1).dot(self.line.getNormalized()) >= 0 and
                (projectile.pos - self.pos2).dot(-self.line.getNormalized()) >= 0)
    def reflectEdge(self,projectile): #Checks if the projectile is colliding with the end of the line
        seperation = self.pos1.copy().subtract(projectile.pos)
        seperation2 = self.pos2.copy().subtract(projectile.pos)
        radius = math.sqrt(self.halfThickness ** 2 + self.halfThickness ** 2)

        if (radius + projectile.radius) >= seperation.length():
            if seperation.angle(projectile.vel) < math.pi/2 or seperation.angle(projectile.vel) > math.pi*3/2: #TODO Test to see if this is actually working
                # Reflect
                projectile.vel.reflect( seperation.getNormalized() )

        if (radius + projectile.radius) >= seperation2.length():
            if seperation2.angle(projectile.vel) < math.pi/2 or seperation2.angle(projectile.vel) > math.pi*3/2: #TODO Test to see if this is actually working
                # Reflect
                projectile.vel.reflect( seperation2.getNormalized() )

    def reflect(self,projectile):
                #Calculate how to free Object
                direction:Vector = projectile.vel.copy().negate().normalize()
                distance = ((projectile.radius + self.halfThickness) - self.distanceTo(projectile)) / max(math.sin(self.line.angle(direction)), 0.02)

                #Reflect
                normal = self.pos1.copy().subtract(self.pos2).getNormal().normalize()
                projectile.vel.reflect(normal)


                #Free Object
                projectile.pos.add(direction.copy().multiply(distance))#Going back by ammount overlapped
                projectile.pos.add(projectile.vel.getNormalized()*distance)#Adding lost distance after

# class WallBox:
#     def __init__(self,halfThickness,pos1,pos2,pos3,pos4):
#         self.wall1 = Wall(halfThickness,pos1)
class WallBox:
    def __init__(self,halfThickness,spriteGroup):
        corner1 = spriteGroup.cornerTopLeft
        corner2 = spriteGroup.cornerTopRight
        corner3 = spriteGroup.cornerBottomRight
        corner4 = spriteGroup.cornerBottomLeft

        self.wall1 = Wall(halfThickness, corner1+Vector(1,halfThickness), corner2+Vector(1,halfThickness)) #Top
        self.wall2 = Wall(halfThickness, corner2+Vector(-halfThickness,1), corner3+Vector(-halfThickness,1)) #Right
        self.wall3 = Wall(halfThickness, corner3+Vector(1,-halfThickness), corner4+Vector(1,-halfThickness)) #Bottom
        self.wall4 = Wall(halfThickness, corner4+Vector(halfThickness,1), corner1+Vector(halfThickness,1)) #Left

    def addTo(self,walls:list):
        walls.append(self.wall1)
        walls.append(self.wall2)
        walls.append(self.wall3)
        walls.append(self.wall4)