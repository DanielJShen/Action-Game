try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import SimpleGUICS2Pygame.simplegui_lib_fps
from Classes.Interactions import Interactions
from Classes.Utilities.Vector import Vector
from Classes.MainCharacter import Character
from Classes.MainCharacter import Keyboard
from Classes.Maps.Mand import ManMap
from Classes.Maps.Tutorial import Tutorial
from Classes.View import View
from Classes.Spritesheet import Spritesheet
from Classes.Inventory import Inventory
from Classes.healthIMG import HealthIMG
from Classes.Abilities.Cannon import Cannon
from Classes.Abilities.Laser import Laser
from Classes.Abilities.Shotgun import Shotgun
from Classes.Enemy.flameBat import flameBat
from Classes.Maps.LynelBoss import LynelMap

import pygame
heart1 = simplegui._load_local_image('Resources/images/Health.png')
class game():

    def __init__(self,resolution,drawWalls1):
        global frame,pygame,simplegui,drawWalls,fps,pickups

        drawWalls = drawWalls1

        CANVAS_HEIGHT=resolution[1] #900
        CANVAS_WIDTH=resolution[0] #1600
        offset = Vector(0,0)
        mousePos = (0,0)

        #Defining Objects
        character_image = simplegui._load_local_image('Resources/images/player.png')

        image_Bat = simplegui._load_local_image('Resources/images/hellBat.png')

        if not globals().__contains__("frame"):
            frame = simplegui.create_frame("Zelda Game", CANVAS_WIDTH, CANVAS_HEIGHT,0)

        keyboard = Keyboard()
        currentMap = 0
        map = [Tutorial(),ManMap(),LynelMap()]
        map[currentMap].start(frame,CANVAS_WIDTH,CANVAS_HEIGHT)
        
        spritesheet = Spritesheet(character_image, 10, 8, 1/10)
        spritesheet.addAnimation([0, 0], [2, 0])
        spritesheet.addAnimation([0, 1], [2, 1])
        spritesheet.addAnimation([0, 2], [0, 2])
        spritesheet.addAnimation([0, 3], [2, 3])
        spritesheet.addAnimation([0, 4], [7, 4])
        spritesheet.addAnimation([0, 5], [7, 5])
        spritesheet.addAnimation([0, 6], [7, 6])
        spritesheet.addAnimation([0, 7], [7, 7])

        global noHearts

        # health = Health(healthOB, noHearts)

        character = Character(Vector(0,0),map[currentMap].startPos,spritesheet,0,(64,64))
        character.healthInit(HealthIMG,heart1)
        character.healthStart(character.healthOB,3)
        offset = -map[currentMap].startPos + (Vector(CANVAS_WIDTH, CANVAS_HEIGHT) / 2)
        interactions = Interactions()
        inventory = Inventory(CANVAS_WIDTH, CANVAS_HEIGHT,character)
        projectiles = []
        lasers = []
        teleporter = map[currentMap].teleporter
        walls = map[currentMap].walls
        enemies = map[currentMap].enemies
        pickups = map[currentMap].pickups
        hearts = map[currentMap].hearts
        boss = None

        trident = simplegui._load_local_image('Resources/images/Trident.png')
        incrementalTimer = 0
        batTimer = 0
        cooldownAbility = 0
        detect = False

        fps = SimpleGUICS2Pygame.simplegui_lib_fps.FPS(x=CANVAS_WIDTH-50, y=10, font_color='Red', font_size=40)
        fps.start()

        # Assign callbacks to event handlers
        frame.set_mouseclick_handler(self.click)
        frame.set_keydown_handler(self.keyDown)
        frame.set_keyup_handler(self.keyUp)
        frame.set_draw_handler(self.draw)
        timer = simplegui.create_timer(300, self.attack)

        globals().update(locals())

        timer.start()
        # Start the frame animation
        frame.start()


    # Handler to draw on canvas
    def attack(self):
        global incrementalTimer,trident
        incrementalTimer += 1
        if boss != None and not boss.death and detect:
            if boss.health > 800 or boss.health < 500 and boss.health > 300:
                if boss.trident and incrementalTimer % 3 == 0:
                    boss.fireTridents(character,projectiles,lasers,trident)
                    incrementalTimer = 0
            elif boss.health <= 800 and boss.health > 700 or boss.health < 300 and boss.health > 200:
                boss.spawn = True
            else:
                boss.spawn = False

        for enemy in enemies:
            if enemy.found:
                enemy.spriteUpdate(character, enemy)
                if enemy.type == "Sniper":
                    enemy.fire(character.pos, projectiles,lasers)
                elif enemy.type == "Melee":
                    enemy.attack(character)
            if not enemy.found:
                enemy.losColour = 'rgb(255,255,0)'

    def draw(self,canvas):
        global noHearts,interactions,health,previous,healthList,heart1,frame,keyboard,CANVAS_WIDTH,CANVAS_HEIGHT,healthOB,image_Bat,timer,pygame,frame,simplegui,drawWalls,fps
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


        #Interactions
        for wall in walls:
            interactions.playerHitWall(wall,character)
            for projectile in projectiles:
                interactions.bounceBallOffWall(projectile,wall,projectiles)


        interactions.playerTouchTeleporter(teleporter,character,self.nextMap)

        #Drawing and Updates
        map[currentMap].draw(canvas, offset, character, inventory)
        character.draw(canvas,offset)
        character.update(keyboard, map[currentMap].zoom, mousePos, offset,frame,timer)

        canvas.draw_circle(mousePos,10,1,"black","black")
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
            if interactions.playerTouchPickup(pickup, pickups, character, inventory):
                if character.heartList[character.last] > 1:
                    character.heartList[character.last] = 1
                    character.hearts[character.last - 1].frameIndex = [0, 0]
                elif character.last < character.noHearts:
                    character.last += 1
                    character.heartList[character.last] = 1
                    character.hearts[character.last - 1].frameIndex = [0, 0]
                else:
                    character.noHearts += 1
                    character.healthListInit.append(HealthIMG(Vector(character.previous, 50), heart1))
                    character.previous += 50
                    character.hearts.append(character.healthListInit[character.noHearts - 1])
                    character.heartList.append(1)
                    character.last += 1

        for pickup in pickups:
            pickup.draw(canvas, offset)

        #Moving Screen
        View().moveScreen(offset,character.pos,CANVAS_WIDTH,CANVAS_HEIGHT)
        for proj in projectiles:
            proj.draw(canvas,offset)
            proj.update(projectiles, map[currentMap].zoom)
            Interactions().ballHitPlayer(proj,character,projectiles)
            for enemy in enemies:
                interactions.ballHitEnemy(proj,projectiles,enemy,enemies)
            if currentMap == 2:
                interactions.ballHitBoss(proj,projectiles,boss)

        for laser in lasers:
            if not lasers.count(laser) > 0: continue
            laser.draw(canvas,offset)
            for enemy in enemies:
                interactions.laserHitEnemy(laser,lasers,enemy,enemies)
            if currentMap == 2:
                interactions.laserHitBoss(laser, lasers,boss)
            lasers.pop(lasers.index(laser))

        if drawWalls:
            for wall in walls:
                #To see collision walls
                wall.draw(canvas,offset)
        inventory.draw(canvas)
        inventory.update(keyboard, (character.pos+offset).getP(), mousePos)


        if currentMap == 2:
            global detect
            if character.pos.x >= 2881 or boss.health != 1000:
                detect = True
                if map[2].trap:
                    map[2].wallPoints2.append((2244, 1112))
                    map[2].wallPoints2.append((2244, 1243))
                    map[2].updateWalls()
                    wall.draw(canvas, offset)
                    map[2].trap = False
            if boss.health <= 0:
                boss.death = True
            if not boss.death and detect:
                global batTimer
                boss.detectionArea(character)
                boss.drawDetectionArea(canvas, offset)
                boss.update()
                if boss.spawn and batTimer % 100 == 0:
                    enemies.append(flameBat(boss.pos + Vector(0, -80), "Blue", "Melee", image_Bat, [0, 0], 160))
                    batTimer = 0
                if boss.health < 700 and boss.health > 500 or boss.health < 200:
                    boss.drawFire(canvas, offset, character, projectiles, lasers)
                batTimer += 1
            boss.updateSprite(canvas, offset, character)



        #Draw HUD
        fps.draw_fct(canvas)
        for i in range(0,character.noHearts):
            character.healthOB[i].draw(canvas, offset)

        canvas.draw_line((20, 100), (175, 100), 30, "white")
        canvas.draw_line((25, 100), (170, 100), 25, "black")
        canvas.draw_line((25, 100), (170-character.stamina, 100), 25, character.staminaColor)

    def click(self,pos):
        print(Vector(pos[0],pos[1])-offset)
        if inventory.isOpen:
            inventory.select(character)

    def keyDown(self,key):
        keyboard.keyDown(key)

    def keyUp(self,key):
        keyboard.keyUp(key)

    def nextMap(self):
        global currentMap,offset,projectiles,lasers,teleporter,walls,enemies,pickups,inventory,character,boss,noHearts
        currentMap += 1
        if map.__len__() > currentMap:
            map[currentMap].start(frame,CANVAS_WIDTH,CANVAS_HEIGHT)
            offset = -map[currentMap].startPos + (Vector(CANVAS_WIDTH, CANVAS_HEIGHT) / 2)
            projectiles = []
            lasers = []
            if currentMap != 2:
                teleporter = map[currentMap].teleporter
            walls = map[currentMap].walls
            enemies = map[currentMap].enemies
            pickups = map[currentMap].pickups
            if currentMap == 1:
                inventory = Inventory(CANVAS_WIDTH, CANVAS_HEIGHT,character)
                character.healthInit(HealthIMG, heart1)
                character.healthStart(character.healthOB, 3)
                Cannon().baseDamage = Cannon().resetDamage
                Laser().baseDamage = Laser().resetDamage
                Shotgun().baseDamage = Shotgun().resetDamage
                character.staminaReg = 0.5
            if currentMap == 2:
                boss = map[2].Boss
            character.pos = map[currentMap].startPos
