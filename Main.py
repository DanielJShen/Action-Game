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
from Classes.Enemy.EnemyInteractions import EnemyInteractions
from Classes.Enemy.Enemy import Enemy
from Classes.Enemy.Line import Line


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
enemies = [Enemy(Vector(900,600),Vector(0,0),300,Line,Vector(0,0))]
inter = EnemyInteractions(character,enemies[0],keyboard)

# Handler to draw on canvas
def attack():
    if inter.found:
        inter.follow()
        inter.updateLOS()
        enemies[0].fire(character.pos, projectiles)
    if not inter.found:
        enemies[0].losColour = 'rgba(' + str(255) + ',' + str(255) + ',' + str(0) + ',' + str(0.6) + ')'
def draw(canvas):
    #Interactions
    for wall in walls:
        for projectile in projectiles:
            Interactions().bounceBallOffWall(projectile,wall)

    #Drawing and Updates
    map.draw(canvas,offset)
    character.draw(canvas,offset)
    character.update(keyboard,map.zoom)


    for enemy in enemies:
        enemy.draw(canvas,offset)
        enemy.drawLOS(canvas)
    # inter.movement()
        inter.LOS(canvas)
        enemy.drawLos(canvas,offset)
        if inter.found:
            inter.search(canvas)
    # inter.line2.draw(canvas)
        if inter.found:
            enemy.update(map.zoom)
    # inter.line3.draw(canvas)

    #Moving Screen
    View().moveScreen(offset,character.pos,CANVAS_WIDTH,CANVAS_HEIGHT)

    for proj in projectiles:
        proj.draw(canvas,offset)
        Interactions().ballHitPlayer(proj,character,projectiles)
        proj.update(projectiles,map.zoom)
        enemies[0].ballHitEnemy(proj,character,projectiles,enemies)

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
timer = simplegui.create_timer(1000, attack)
timer.start()
# Start the frame animation
frame.start()
