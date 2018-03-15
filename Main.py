try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from Classes.Interactions import Interactions
from Classes.Vector import Vector
from Classes.MainCharacter import Character
from Classes.MainCharacter import Keyboard
from Classes.Maps.Map import Map
from Classes.View import View
from Classes.Spritesheet import Spritesheet
from Classes.Inventory import Inventory
from Classes.Enemy.Line import Line
from Classes.healthIMG import HealthIMG
from Classes.Health import Health
import pygame
import random

CANVAS_HEIGHT=900
CANVAS_WIDTH=1600
offset = Vector(0,0)
mousePos = (0,0)

#Defining Objects
character_image = simplegui._load_local_image('Resources/images/Deku_Link.png')
heart1 = simplegui._load_local_image('Resources/images/Health.png')
player = simplegui._load_local_image('Resources/images/player.png')

frame = simplegui.create_frame("Action Game", CANVAS_WIDTH, CANVAS_HEIGHT)
keyboard = Keyboard()
map = Map(frame,CANVAS_WIDTH,CANVAS_HEIGHT)
offset = -map.startPos+(Vector(CANVAS_WIDTH, CANVAS_HEIGHT)/2)
spritesheet = Spritesheet(player, 10, 8, 1/10)
spritesheet.addAnimation([0, 0], [2, 0])
spritesheet.addAnimation([0, 1], [2, 1])
spritesheet.addAnimation([0, 2], [0, 2])
spritesheet.addAnimation([0, 3], [2, 3])
spritesheet.addAnimation([0, 4], [7, 4])
spritesheet.addAnimation([0, 5], [7, 5])
spritesheet.addAnimation([0, 6], [7, 6])
spritesheet.addAnimation([0, 7], [7, 7])
character = Character(Vector(0,0),map.startPos,spritesheet,0,(64,64))
inventory = Inventory(CANVAS_WIDTH, CANVAS_HEIGHT,character)
projectiles = []
walls = map.walls
enemies = map.enemies
heart1OB = HealthIMG(Vector(50,50),heart1)
heart2OB = HealthIMG(Vector(100,50),heart1)
heart3OB = HealthIMG(Vector(150,50),heart1)
healthOB = [heart1OB,heart2OB,heart3OB]
health = Health(heart1OB,heart2OB,heart3OB)
incrementalTimer = 0

# Handler to draw on canvas
def attack():
    for enemy in enemies:
        if enemy.found:
            enemy.spriteUpdate(character, enemy)
            if enemy.type == "Sniper":
                enemy.fire(character.pos, projectiles)
            elif enemy.type == "Malee":
                enemy.attack(character,health)
        if not enemy.found:
            enemy.losColour = 'rgba(255,255,0,0.6)'

def draw(canvas):
    #Updating Mouse Position
    mousePos = (pygame.mouse.get_pos()[0]-frame._canvas_x_offset,pygame.mouse.get_pos()[1]-frame._canvas_y_offset)
    global incrementalTimer
    i = 0
    while i < enemies.__len__()-1:
        k = enemies.__len__()-1
        while k > i:
            enemies[i].alertDistance(enemies[k])
            k -= 1
        i += 1

    #Interactions
    for wall in walls:
        for projectile in projectiles:
            Interactions().bounceBallOffWall(projectile,wall,projectiles)

    #Drawing and Updates
    map.draw(canvas,offset)
    character.draw(canvas,offset)
    character.update(keyboard,map.zoom, mousePos, offset)

    canvas.draw_circle(mousePos,10,1,"darkblue","darkblue")
    for enemy in enemies:
        enemy.draw(canvas,offset,enemy,character)
        enemy.update(map.zoom,character)
        if enemy.found:
            enemy.follow(character)
            enemy.search(character)
            enemy.stop(character)
        elif not enemy.found:
            enemy.vel = Vector(0,0)

    #Moving Screen
    View().moveScreen(offset,character.pos,CANVAS_WIDTH,CANVAS_HEIGHT)
    for proj in projectiles:
        proj.draw(canvas,offset)
        proj.update(projectiles,map.zoom)
        Interactions().ballHitPlayer(proj,character,projectiles,health)

        for enemy in enemies:
            Interactions().ballHitEnemy(proj,projectiles,enemy,enemies)

    for wall in walls:
        Interactions().playerHitWall(wall,character)
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
    if inventory.isOpen:
        inventory.select(character)
    else:
        character.fire(Vector(pos[0], pos[1])-offset, projectiles)


def keyDown(key):
    keyboard.keyDown(key)

def keyUp(key):
    keyboard.keyUp(key)

# Assign callbacks to event handlers
frame.set_mouseclick_handler(click)
frame.set_keydown_handler(keyDown)
frame.set_keyup_handler(keyUp)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(500, attack)
timer.start()
# Start the frame animation
frame.start()
