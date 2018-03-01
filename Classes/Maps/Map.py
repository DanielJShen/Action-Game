try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Classes.Objects.Sprite import Sprite
from Classes.Vector import Vector
import math

class Map:
    def __init__(self):
        self.sprites = []

        #Load Images
        image_wall = simplegui.load_image('https://opengameart.org/sites/default/files/stone_wall02.png')
        image_spike = simplegui.load_image('https://opengameart.org/sites/default/files/Spike_Pixel_0.png')


        #All sprites
        self.sprites.append(Sprite( Vector(50,50) , image_wall , [50,50] ))
        self.sprites.append(Sprite( Vector(100,50) , image_wall , [50,50] ))
        self.sprites.append(Sprite( Vector(150,50) , image_wall, [50, 50], math.pi * 45 / 360))

    def draw(self,canvas):
        for sprite in self.sprites:
            sprite.draw(canvas)