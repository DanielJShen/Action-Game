from Classes.Vector import Vector
import math
class LinePosDir:
    def __init__(self, point, direction,color):
        self.length = 500
        self.pA = point
        self.direction = direction
        self.pB = self.pA+(direction*self.length)
        self.color = color
        self.thickness = 4

        self.line = self.direction*self.length

    def draw(self, canvas, offset):
        canvas.draw_line((self.pA+offset).getP(), (self.pB+offset).getP(), self.thickness, self.color)

    def distanceTo(self,enemy):
        line1 = self.pA.copy().subtract(enemy.pos)
        angle = line1.angle(self.line)
        return line1.length()*math.sin(angle)