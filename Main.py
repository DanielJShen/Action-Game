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
from Classes.Maps.Map import Map
from Classes.Inventory import Inventory

import random

CANVAS_HEIGHT = 900
CANVAS_WIDTH = 1600

# Defining Objects
character_image = simplegui._load_local_image('Resources/images/Deku_Link.png')
character = Character(Vector(0, 0), Vector(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2), character_image, 0, (64, 64))
keyboard = Keyboard()
inventory = Inventory(CANVAS_WIDTH, CANVAS_HEIGHT)
map = Map()
projectiles = []
walls = map.walls


# for i in range(100):
#     projectiles.append( Projectile(Vector(random.randint(2,22),random.randint(2,22)),Vector(random.randint(0,CANVAS_WIDTH),random.randint(0,CANVAS_HEIGHT)),10,-1,True,0,"none") )
#     walls.append( Wall(4,Vector(random.randint(0,CANVAS_WIDTH),random.randint(0,CANVAS_HEIGHT)),Vector(random.randint(0,CANVAS_WIDTH),random.randint(0,CANVAS_HEIGHT))) )

# Handler to draw on canvas
def draw(canvas):
    # Interactions
    for wall in walls:
        for projectile in projectiles:
            Interactions().bounceBallOffWall(projectile, wall)

    # Drawing and Updates
    map.draw(canvas)
    canvas.draw_text("Testing", [50, 112], 48, "Red")
    character.draw(canvas)
    character.update(keyboard)
    character.pos.x %= CANVAS_WIDTH
    character.pos.y %= CANVAS_HEIGHT

    for proj in projectiles:
        proj.draw(canvas)
        proj.update(projectiles)
        proj.pos.x %= CANVAS_WIDTH
        proj.pos.y %= CANVAS_HEIGHT

    # To see collision walls
    # for wall in walls:
    #     wall.draw(canvas)

    inventory.draw(canvas)
    inventory.update(keyboard, character.pos.getP())


def click(pos):
    if inventory.isOpen:
        inventory.select()
    else:
        character.fire(Vector(pos[0], pos[1]), projectiles)


def drag(pos):
    if inventory.isOpen:
        inventory.drag(pos)


def keyDown(key):
    keyboard.keyDown(key)


def keyUp(key):
    keyboard.keyUp(key)


# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Action Game", CANVAS_WIDTH, CANVAS_HEIGHT)
frame.set_mouseclick_handler(click)
frame.set_mousedrag_handler(drag)
frame.set_keydown_handler(keyDown)
frame.set_keyup_handler(keyUp)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
