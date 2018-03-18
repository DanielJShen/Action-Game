class heart:
    def __init__(self,pos):
        self.pos = pos
        self.radius = 10

    def draw(self,canvas,offset):
        canvas.draw_circle((self.pos + offset).getP(), self.radius, self.radius, "red","red")

    def updateHearts(self):
        pass