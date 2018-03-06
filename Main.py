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
from Classes.View import View

import random

CANVAS_HEIGHT=900
CANVAS_WIDTH=1600
offset = Vector(0,0)

#Defining Objects
character_image = simplegui._load_local_image('Resources/images/Deku_Link.png')
frame = simplegui.create_frame("Action Game", CANVAS_WIDTH, CANVAS_HEIGHT)
keyboard = Keyboard()
map = Map(frame,CANVAS_WIDTH,CANVAS_HEIGHT)
character = Character(Vector(0,0),map.startPos,character_image,0,(64,64))
offset = -map.startPos+(Vector(CANVAS_WIDTH, CANVAS_HEIGHT)/2)
projectiles = []
walls = map.walls
# for i in range(100):
#     projectiles.append( Projectile(Vector(random.randint(2,22),random.randint(2,22)),Vector(random.randint(0,CANVAS_WIDTH),random.randint(0,CANVAS_HEIGHT)),10,-1,True,0,"none") )
#     walls.append( Wall(4,Vector(random.randint(0,CANVAS_WIDTH),random.randint(0,CANVAS_HEIGHT)),Vector(random.randint(0,CANVAS_WIDTH),random.randint(0,CANVAS_HEIGHT))) )

# Handler to draw on canvas
def draw(canvas):
    #Interactions
    for wall in walls:
        for projectile in projectiles:
            Interactions().bounceBallOffWall(projectile,wall)

    #Drawing and Updates
    map.draw(canvas,offset)
    character.draw(canvas,offset)
    character.update(keyboard,map.zoom)

    #Moving Screen
    View().moveScreen(offset,character.pos,CANVAS_WIDTH,CANVAS_HEIGHT)

    for proj in projectiles:
        proj.draw(canvas,offset)
        Interactions().ballHitPlayer(proj,character,projectiles)
        proj.update(projectiles,map.zoom)

    for wall in walls:
        Interactions().playerHitWall(wall,character)
        #To see collision walls
        # wall.draw(canvas,offset)

    #Draw HUD
    canvas.draw_text("Testing", [50,112], 48, "white")
    canvas.draw_text("Health: "+str(character.health), [50, 200], 48, "Red")

def click(pos):
    character.fire(Vector(pos[0],pos[1])-offset,projectiles)
def keyDown(key):
    keyboard.keyDown(key)
def keyUp(key):
    keyboard.keyUp(key)
# Assign callbacks to event handlers
frame.set_mouseclick_handler(click)
frame.set_keydown_handler(keyDown)
frame.set_keyup_handler(keyUp)
frame.set_draw_handler(draw)


# Start the frame animation
frame.start()
