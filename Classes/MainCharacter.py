from Classes.Vector import Vector
import math
class Character:
    def __init__(self,vel,pos):
        self.vel = vel
        self.pos:Vector = pos

    def draw(self,canvas):
        canvas.draw_image()
    def update(self):
        self.pos.add(self.vel)

class Keyboard:
    def __init__(self):
        pass