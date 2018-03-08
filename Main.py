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
from Classes.Enemy.Enemy import Enemy
from Classes.Enemy.Enemy2 import Enemy2
from Classes.Inventory import Inventory
from Classes.Enemy.Line import Line
from Classes.healthIMG import HealthIMG
from Classes.Health import Health

CANVAS_HEIGHT=900
CANVAS_WIDTH=1600
offset = Vector(0,0)
i = 0
#Defining Objects
character_image = simplegui._load_local_image('Resources/images/Deku_Link.png')
heart1 = simplegui._load_local_image('Resources/images/Health.png')
Bat = simplegui._load_local_image('Resources/images/Bat.png')
FireEnemy = simplegui._load_local_image('Resources/images/FireEnemy.png')

frame = simplegui.create_frame("Action Game", CANVAS_WIDTH, CANVAS_HEIGHT)
keyboard = Keyboard()
map = Map(frame,CANVAS_WIDTH,CANVAS_HEIGHT)
character = Character(Vector(0,0),map.startPos,character_image,0,(64,64))
offset = -map.startPos+(Vector(CANVAS_WIDTH, CANVAS_HEIGHT)/2)
inventory = Inventory(CANVAS_WIDTH, CANVAS_HEIGHT)
projectiles = []
walls = map.walls
enemies = [Enemy(Vector(900,1600),"Red","Sniper",FireEnemy),Enemy2(Vector(1200,1000),"Blue","Malee",Bat)]
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
            enemy.follow(character)
            if enemy.type == "Sniper":
                enemy.fire(character.pos, projectiles)
            elif enemy.type == "Malee":
                enemy.attack(character,health)
        if not enemy.found:
            enemy.losColour = 'rgba(255,255,0,0.6)'

def draw(canvas):
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
    character.update(keyboard,map.zoom)

    for enemy in enemies:
        enemy.draw(canvas,offset,Bat,enemy,character)
        enemy.update(map.zoom,character)
        if enemy.found:
            if incrementalTimer%5 == 0:
                enemy.spriteUpdate(character, enemy)
            incrementalTimer += 1
            enemy.search(character)
            enemy.stop(character)
        elif not enemy.found:
            enemy.direction = Vector(0,0)

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
    inventory.update(keyboard, (character.pos+offset).getP())

    #Draw HUD
    i = healthOB.__len__()-1
    while i >= 0:
        healthOB[i].draw(canvas, offset)
        i -= 1
    # canvas.draw_text("Testing", [50,112], 48, "white")
    # canvas.draw_text("Health: "+str(character.health), [50, 200], 48, "Red")

def click(pos):
    if inventory.isOpen:
        inventory.select()
    else:
        character.fire(Vector(pos[0], pos[1])-offset, projectiles)


def drag(pos):
    if inventory.isOpen:
        inventory.drag(pos)


def keyDown(key):
    keyboard.keyDown(key)

def keyUp(key):
    keyboard.keyUp(key)

# Assign callbacks to event handlers
frame.set_mouseclick_handler(click)
frame.set_mousedrag_handler(drag)
frame.set_keydown_handler(keyDown)
frame.set_keyup_handler(keyUp)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(500, attack)
timer.start()
# Start the frame animation
frame.start()
