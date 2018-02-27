try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Classes.Objects.Projectile import Projectile
from Classes.Interactions import Interactions
from Classes.Objects.Wall import Wall
from Classes.Vector import Vector

import random

CANVAS_HEIGHT=1000
CANVAS_WIDTH=1600

projectiles = []
walls = []

def click():pass

for i in range(50):
    projectiles.append( Projectile(Vector(random.randint(2,12),random.randint(2,12)),Vector(random.randint(0,CANVAS_WIDTH),random.randint(0,CANVAS_HEIGHT)),20,-1,True,0) )
walls.append( Wall(Vector(0,0),50,Vector(200,500),Vector(500,300)) )
interaction = Interactions()


# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text("Testing", [50,112], 48, "Red")


    interaction.bounceBallOffWall(projectiles,walls)

    for wall in walls:
        wall.draw(canvas)

    for proj in projectiles:
        proj.draw(canvas)
        proj.update()
        proj.pos.x %= CANVAS_WIDTH
        proj.pos.y %= CANVAS_HEIGHT


# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", CANVAS_WIDTH, CANVAS_HEIGHT)
frame.add_button("Click me", click)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
