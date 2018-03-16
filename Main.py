try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from Classes.Interactions import Interactions
from Classes.Utilities.Vector import Vector
from Classes.MainCharacter import Character
from Classes.MainCharacter import Keyboard
from Classes.Maps.Map import Map
from Classes.Maps.Mand import ManMap
from Classes.Maps.Tutorial import Tutorial
from Classes.View import View
from Classes.Inventory import Inventory
from Classes.healthIMG import HealthIMG
from Classes.Health import Health
from Classes.Enemy.LynelBoss import LynelBoss
from Classes.Maps.LynelBoss import LynelMap

import pygame

CANVAS_HEIGHT=900
CANVAS_WIDTH=1600
offset = Vector(0,0)
mousePos = (0,0)

#Defining Objects
character_image = simplegui._load_local_image('Resources/images/Deku_Link.png')
heart1 = simplegui._load_local_image('Resources/images/Health.png')

frame = simplegui.create_frame("Action Game", CANVAS_WIDTH, CANVAS_HEIGHT)
keyboard = Keyboard()
currentMap = 0
map = [Tutorial(),ManMap(),Map(),LynelMap()]
map[currentMap].start(frame,CANVAS_WIDTH,CANVAS_HEIGHT)
character = Character(Vector(0,0), map[currentMap].startPos, character_image, 0, (64, 64))
offset = -map[currentMap].startPos + (Vector(CANVAS_WIDTH, CANVAS_HEIGHT) / 2)
interactions = Interactions()
inventory = Inventory(CANVAS_WIDTH, CANVAS_HEIGHT,character)
projectiles = []
lasers = []
if currentMap == 3:
    boss = map[currentMap].Boss
else:
    boss = None
teleporter = map[currentMap].teleporter
walls = map[currentMap].walls
enemies = map[currentMap].enemies
pickups = map[currentMap].pickups
heart1OB = HealthIMG(Vector(50,50),heart1)
heart2OB = HealthIMG(Vector(100,50),heart1)
heart3OB = HealthIMG(Vector(150,50),heart1)
healthOB = [heart1OB,heart2OB,heart3OB]
health = Health(heart1OB,heart2OB,heart3OB)
trident = simplegui._load_local_image('Resources/images/Trident.png')
incrementalTimer = 0
cooldownAbility = 0



# Handler to draw on canvas
def attack():
    global incrementalTimer
    incrementalTimer += 1
    if boss != None:
        if boss.trident and incrementalTimer % 3 == 0:
            boss.fireTridents(character,projectiles,lasers,trident)
            incrementalTimer = 0
    for enemy in enemies:
        if enemy.found:
            enemy.spriteUpdate(character, enemy)
            if enemy.type == "Sniper":
                enemy.fire(character.pos, projectiles,lasers)
            elif enemy.type == "Malee":
                enemy.attack(character,health)
        if not enemy.found:
            enemy.losColour = 'rgba(255,255,0,0.6)'

def draw(canvas):
    #Updating Mouse Position
    mousePos = (pygame.mouse.get_pos()[0]-frame._canvas_x_offset,pygame.mouse.get_pos()[1]-frame._canvas_y_offset)
    global incrementalTimer, cooldownAbility

    if not character.activeAbility.__class__.__name__ == "Laser":
        if cooldownAbility == 0:
            cooldownAbility = 20
            if not inventory.isOpen and pygame.mouse.get_pressed()[0]:
                character.fire(Vector(mousePos[0], mousePos[1]) - offset, projectiles, lasers)
        cooldownAbility -= 1
    else:
        if not inventory.isOpen and pygame.mouse.get_pressed()[0]:
            character.fire(Vector(mousePos[0], mousePos[1]) - offset, projectiles, lasers)

    i = 0
    while i < enemies.__len__()-1:
        k = enemies.__len__()-1
        while k > i:
            enemies[i].alertDistance(enemies[k])
            k -= 1
        i += 1
    if currentMap == 3:
        boss.detectionArea(character,canvas,offset)
        boss.drawDetectionArea(canvas,offset)
        boss.updateSprite(canvas,offset,character)
        boss.update()

    #Interactions
    for wall in walls:
        interactions.playerHitWall(wall,character)
        for projectile in projectiles:
            interactions.bounceBallOffWall(projectile,wall,projectiles)

    for pickup in pickups:
        interactions.playerTouchPickup(pickup,pickups,character,inventory)

    interactions.playerTouchTeleporter(teleporter,character,nextMap)

    #Drawing and Updates
    map[currentMap].draw(canvas, offset, character, inventory)
    character.draw(canvas,offset)
    character.update(keyboard, map[currentMap].zoom, mousePos, offset)

    canvas.draw_circle(mousePos,10,1,"darkblue","darkblue")
    for enemy in enemies:
        enemy.draw(canvas,offset)
        enemy.update(map[currentMap].zoom, character)
        if enemy.found:
            enemy.follow(character)
            enemy.search(character)
            enemy.stop(character)
        elif not enemy.found:
            enemy.vel = Vector(0,0)

    for pickup in pickups:
        pickup.draw(canvas,offset)

    #Moving Screen
    View().moveScreen(offset,character.pos,CANVAS_WIDTH,CANVAS_HEIGHT)
    for proj in projectiles:
        proj.draw(canvas,offset)
        proj.update(projectiles, map[currentMap].zoom)
        Interactions().ballHitPlayer(proj,character,projectiles,health)
        for enemy in enemies:
            interactions.ballHitEnemy(proj,projectiles,enemy,enemies)

    for laser in lasers:
        if not lasers.count(laser) > 0: continue
        laser.draw(canvas,offset)
        for enemy in enemies:
            interactions.laserHitEnemy(laser,lasers,enemy,enemies)
        lasers.pop(lasers.index(laser))

    # for wall in walls:
        #To see collision walls
        # wall.draw(canvas,offset)
    inventory.draw(canvas)
    inventory.update(keyboard, (character.pos+offset).getP(), mousePos)

    #Draw HUD
    i = healthOB.__len__()-1
    while i >= 0:
        healthOB[i].draw(canvas, offset)
        i -= 1
    # canvas.draw_text("Testing", [50,112], 48, "white")
    # canvas.draw_text("Health: "+str(character.health), [50, 200], 48, "Red")

def click(pos):
    print(Vector(pos[0],pos[1])-offset)
    if inventory.isOpen:
        inventory.select(character)

def keyDown(key):
    keyboard.keyDown(key)

def keyUp(key):
    keyboard.keyUp(key)

def nextMap():
    global currentMap,offset,projectiles,lasers,teleporter,walls,enemies,pickups,inventory,character
    currentMap += 1
    if map[currentMap] != None:
        map[currentMap].start(frame,CANVAS_WIDTH,CANVAS_HEIGHT)
        offset = -map[currentMap].startPos + (Vector(CANVAS_WIDTH, CANVAS_HEIGHT) / 2)
        projectiles = []
        lasers = []
        teleporter = map[currentMap].teleporter
        walls = map[currentMap].walls
        enemies = map[currentMap].enemies
        pickups = map[currentMap].pickups
        inventory = Inventory(CANVAS_WIDTH, CANVAS_HEIGHT,character)
        character.pos = map[currentMap].startPos


# Assign callbacks to event handlers
frame.set_mouseclick_handler(click)
frame.set_keydown_handler(keyDown)
frame.set_keyup_handler(keyUp)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(300, attack)
timer.start()
# Start the frame animation
frame.start()
