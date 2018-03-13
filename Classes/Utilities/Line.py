from Classes.Vector import Vector


class Line:
    def __init__(self, point1, point2, color):
        self.pA = point1
        self.pB = point2
        self.color = color
        self.thickness = 4
        self.length = self.pB - self.pA

    def draw(self, canvas, offset):
        canvas.draw_line((self.pA + offset).getP(), (self.pB + offset).getP(), self.thickness, self.color)