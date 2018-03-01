try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Classes.Objects.Projectile import Projectile
from Classes.Interactions import Interactions
from Classes.Objects.Wall import Wall
from Classes.Vector import Vector
from Classes.MainCharacter import Character
from Classes.MainCharacter import Keyboard

import random

CANVAS_HEIGHT=1000
CANVAS_WIDTH=1600

#Defining Objects
character_image = simplegui.load_image('http://blog.acamara.es/wp-content/uploads/2012/12/PJ-WalkDown1.png')
character = Character(Vector(0,0),Vector(CANVAS_WIDTH/2,CANVAS_HEIGHT/2),character_image,0)
keyboard = Keyboard()
projectiles = []
walls = []
for i in range(10):
    projectiles.append( Projectile(Vector(random.randint(2,22),random.randint(2,22)),Vector(random.randint(0,CANVAS_WIDTH),random.randint(0,CANVAS_HEIGHT)),20,-1,True,0,"none") )
    walls.append( Wall(Vector(0,0),8,Vector(random.randint(0,CANVAS_WIDTH),random.randint(0,CANVAS_HEIGHT)),Vector(random.randint(0,CANVAS_WIDTH),random.randint(0,CANVAS_HEIGHT))) )

# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text("Testing", [50,112], 48, "Red")

    #Interactions
    for wall in walls:
        for projectile in projectiles:
            Interactions().bounceBallOffWall(projectile,wall)


    #Drawing and Updates
    character.draw(canvas)
    character.update(keyboard)
    for wall in walls:
        wall.draw(canvas)
    for proj in projectiles:
        proj.draw(canvas)
        proj.update()
        proj.pos.x %= CANVAS_WIDTH
        proj.pos.y %= CANVAS_HEIGHT


def click(pos):
    character.fire(Vector(pos[0],pos[1]),projectiles)
def keyDown(key):
    keyboard.keyDown(key)
def keyUp(key):
    keyboard.keyUp(key)
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", CANVAS_WIDTH, CANVAS_HEIGHT)
frame.set_mouseclick_handler(click)
frame.set_keydown_handler(keyDown)
frame.set_keyup_handler(keyUp)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
