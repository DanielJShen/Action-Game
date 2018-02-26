try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Classes.Objects.Projectile import Projectile
from Classes.Interactions import Interactions
from Classes.Objects.Wall import Wall
from Classes.Vector import Vector

CANVAS_HEIGHT=1000
CANVAS_WIDTH=1600

def click():pass

projectile = Projectile(Vector(10,8),Vector(50,50),20,-1,True,0)
wall = Wall(Vector(0,0),Vector(200,500),Vector(500,300))
interaction = Interactions()

# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text("Testing", [50,112], 48, "Red")
    projectile.draw(canvas)
    projectile.update()
    wall.draw(canvas)


    projectiles = [projectile]
    walls = [wall]
    interaction.bounceBallOffWall(projectiles,walls)

    for proj in projectiles:
        proj.pos.x %= CANVAS_WIDTH
        proj.pos.y %= CANVAS_HEIGHT


# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", CANVAS_WIDTH, CANVAS_HEIGHT)
frame.add_button("Click me", click)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
