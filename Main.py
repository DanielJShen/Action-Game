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
i = 0
#Defining Objects
character_image = simplegui._load_local_image('Resources/images/Deku_Link.png')
frame = simplegui.create_frame("Action Game", CANVAS_WIDTH, CANVAS_HEIGHT)
keyboard = Keyboard()
map = Map(frame,CANVAS_WIDTH,CANVAS_HEIGHT)
character = Character(Vector(0,0),map.startPos,character_image,0,(64,64))
offset = -map.startPos+(Vector(CANVAS_WIDTH, CANVAS_HEIGHT)/2)
projectiles = []
walls = map.walls
enemies = [Enemy(Vector(900,1500),"Red",300,Line,"sniper"),Enemy(Vector(1200,1000),"Blue",300,Line,"malee")]
inter = EnemyInteractions(character)

# Handler to draw on canvas
def attack():
    for enemy in enemies:
        if enemy.found:
            inter.follow(enemy)
            inter.updateLOS(enemy)
            if enemy.type == "sniper":
                enemy.fire(character.pos, projectiles)
            elif enemy.type == "malee":
                inter.attack(enemy)
        if not enemy.found:
            enemy.losColour = 'rgba(255,255,0,0.6)'

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
        inter.LOS(enemy)
        enemy.drawLos(canvas,offset)
        inter.soundDistance(enemy)
        if enemy.found:
            inter.search(enemy)
            inter.stop(enemy)
            enemy.update(map.zoom)

    #Moving Screen
    View().moveScreen(offset,character.pos,CANVAS_WIDTH,CANVAS_HEIGHT)

    for proj in projectiles:
        proj.draw(canvas,offset)
        proj.update(projectiles,map.zoom)
        if projectiles.count(proj) == 0: pass
        Interactions().ballHitPlayer(proj,character,projectiles)
        proj.update(projectiles,map.zoom)
        for enemy in enemies:
            enemy.ballHitEnemy(proj,inter,projectiles,enemy,enemies)

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
