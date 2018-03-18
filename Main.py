import runpy
file_globals = runpy.run_path("Classes/PyGamesMenu.py") #Run menu before importing for seperate pygame's
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
from Classes.Enemy.flameBat import flameBat
from Classes.Maps.LynelBoss import LynelMap

import pygame

class game():

    def __init__(self):
        CANVAS_HEIGHT=900
        CANVAS_WIDTH=1600
        offset = Vector(0,0)
        mousePos = (0,0)

        #Defining Objects
        character_image = simplegui._load_local_image('Resources/images/Deku_Link.png')
        heart1 = simplegui._load_local_image('Resources/images/Health.png')
        image_Bat = simplegui._load_local_image('Resources/images/hellBat.png')

        frame = simplegui.create_frame("Action Game", CANVAS_WIDTH, CANVAS_HEIGHT)
        keyboard = Keyboard()
        currentMap = 0
        map = [Tutorial(),ManMap(),LynelMap()]
        map[currentMap].start(frame,CANVAS_WIDTH,CANVAS_HEIGHT)
        character = Character(Vector(0,0), map[currentMap].startPos, character_image, 0, (64, 64))
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
        defaultHearts = 3
        noHearts = defaultHearts
        previous = 50
        healthList = []
        for i in range(0,noHearts):
            healthList.append(HealthIMG(Vector(previous,50),heart1))
            previous += 50

        healthOB = []
        for i in range(0,noHearts):
            healthOB.append(healthList[i])

        health = Health(healthOB,noHearts)
        trident = simplegui._load_local_image('Resources/images/Trident.png')
        incrementalTimer = 0
        batTimer = 0
        cooldownAbility = 0
        detect = False

        globals().update(locals())

        # Assign callbacks to event handlers
        frame.set_mouseclick_handler(self.click)
        frame.set_keydown_handler(self.keyDown)
        frame.set_keyup_handler(self.keyUp)
        frame.set_draw_handler(self.draw)
        timer = simplegui.create_timer(300, self.attack)
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
                elif enemy.type == "Malee":
                    enemy.attack(character,health)
            if not enemy.found:
                enemy.losColour = 'rgba(255,255,0,0.6)'

    def draw(self,canvas):
        global noHearts,interactions,health,previous,healthList,heart1,frame,keyboard,CANVAS_WIDTH,CANVAS_HEIGHT,healthOB,image_Bat

        for pickup in pickups:
            if interactions.playerTouchPickup(pickup, pickups, character, inventory):
                if health.heartList[health.last] > 1:
                    health.heartList[health.last] = 1
                    health.hearts[health.last - 1].frameIndex = [0, 0]
                elif health.last < noHearts:
                    health.last += 1
                    health.heartList[health.last] = 1
                    health.hearts[health.last - 1].frameIndex = [0, 0]
                else:
                    noHearts += 1
                    healthList.append(HealthIMG(Vector(previous, 50), heart1))
                    previous += 50
                    health.hearts.append(healthList[noHearts - 1])
                    health.heartList.append(1)
                    health.last += 1

        for pickup in pickups:
            pickup.draw(canvas, offset)

        # for heart in hearts:
        #     if interactions.playerPickupsHeart(noHearts, heart, hearts, character):
        #         if health.heartList[health.last] > 1:
        #             health.heartList[health.last] = 1
        #             health.hearts[health.last - 1].frameIndex = [0, 0]
        #         elif health.last < noHearts:
        #             health.last += 1
        #             health.heartList[health.last] = 1
        #             health.hearts[health.last - 1].frameIndex = [0, 0]
        #         else:
        #             noHearts += 1
        #             healthList.append(HealthIMG(Vector(previous, 50), heart1))
        #             previous += 50
        #             health.hearts.append(healthList[noHearts-1])
        #             health.heartList.append(1)
        #             health.last += 1
        #
        #     # health = Health(healthOB, noHearts)
        #     heart.draw(canvas, offset)

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



        #Moving Screen
        View().moveScreen(offset,character.pos,CANVAS_WIDTH,CANVAS_HEIGHT)
        for proj in projectiles:
            proj.draw(canvas,offset)
            proj.update(projectiles, map[currentMap].zoom)
            Interactions().ballHitPlayer(proj,character,projectiles,health)
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

        for wall in walls:
            #To see collision walls
            wall.draw(canvas,offset)
        inventory.draw(canvas)
        inventory.update(keyboard, (character.pos+offset).getP(), mousePos)


        if currentMap == 2:
            global detect
            if character.pos.x >= 2881:
                detect = True
            if boss.health <= 0:
                boss.death = True
            if not boss.death and detect:
                global batTimer
                boss.detectionArea(character)
                boss.drawDetectionArea(canvas, offset)
                boss.update()
                if boss.spawn and batTimer % 100 == 0:
                    enemies.append(flameBat(boss.pos + Vector(0, -80), "Blue", "Malee", image_Bat, [0, 0], 160))
                    batTimer = 0
                if boss.health < 700 and boss.health > 500 or boss.health < 200:
                    boss.drawFire(canvas, offset, character, projectiles, lasers)
                batTimer += 1
            boss.updateSprite(canvas, offset, character)



        #Draw HUD
        for i in range(0,noHearts):
            healthOB[i].draw(canvas, offset)

        canvas.draw_line((20, 100), (175, 100), 30, "white")
        canvas.draw_line((25, 100), (170, 100), 25, "black")
        canvas.draw_line((25, 100), (170-character.stamina, 100), 25, character.staminaColor)
        # canvas.draw_text("Testing", [50,112], 48, "white")
        # canvas.draw_text("Health: "+str(character.health), [50, 200], 48, "Red")

    def click(self,pos):
        print(Vector(pos[0],pos[1])-offset)
        if inventory.isOpen:
            inventory.select(character)

    def keyDown(self,key):
        keyboard.keyDown(key)

    def keyUp(self,key):
        keyboard.keyUp(key)

    def nextMap(self):
        global currentMap,offset,projectiles,lasers,teleporter,walls,enemies,pickups,inventory,character,boss
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
            if currentMap == 2:
                boss = map[2].Boss
            character.pos = map[currentMap].startPos


game()