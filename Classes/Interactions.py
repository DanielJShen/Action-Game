from Classes.Utilities.Vector import Vector
from Classes.PowerUps.SpeedPowerUp import SpeedPowerUp
from Classes.PowerUps.DamagePowerUp import DamagePowerUp
from Classes.PowerUps.StaminaPowerUp import StaminaPowerUp
from Classes.Abilities.Laser import Laser
from Classes.Inventory import Inventory
import pygame

class Interactions:
    def __init__(self):
        self.dmgP = DamagePowerUp()

    def bounceBallOffWall(self,projectile,wall,projectiles):
        if projectiles.count(projectile) == 0: return
        if projectile.bounce():
            if projectile.radius + wall.halfThickness >= wall.distanceTo(projectile):
                if wall.inBounds(projectile):
                    wall.reflect(projectile)
            # else:
            #     wall.reflectEdge(projectile)
        else:
            try:
                projectiles.pop(projectiles.index(projectile))
            except ValueError:
                print("Projectile missing error")

    def ballHitPlayer(self,projectile,player,projectiles):
        if projectiles.count(projectile) == 0: return
        seperation = player.pos-projectile.pos
        if not projectile.owner == "player":
            if projectile.radius + player.radius >= seperation.length():
                player.health -= projectile.damage
                player.damageTaken()
                try:
                    projectiles.pop(projectiles.index(projectile))
                except ValueError:
                    print("Projectile missing error")

    def playerHitWall(self,wall,player):
        if max(player.size[0],player.size[1])/1.8 + wall.halfThickness >= wall.distanceTo(player):
            if wall.playerInBounds(player):
                direction:Vector = player.vel.getProj(wall.line.getNormal()).getNormalized().negate()
                distance = max(((player.radius + wall.halfThickness + 1) - wall.distanceTo(player)),0)

                player.vel:Vector = player.vel.getProj(wall.line.getNormalized())
                player.pos.add(direction*distance)
        if max(player.size[0],player.size[1])/1.8 + wall.halfThickness >= (player.pos-wall.pos1).length():
            direction = (player.pos-wall.pos1).getNormalized()
            distance = max((player.radius+wall.halfThickness+1) - (player.pos-wall.pos1).length() , 0)
            player.vel = player.vel.getProj(direction.getNormal())
            player.pos.add(direction*distance)
        elif max(player.size[0],player.size[1])/1.8 + wall.halfThickness >= (player.pos-wall.pos2).length():
            direction = (player.pos-wall.pos1).getNormalized()
            distance = max((player.radius+wall.halfThickness+1) - (player.pos-wall.pos2).length() , 0)
            player.vel = player.vel.getProj(direction.getNormal())
            player.pos.add(direction*distance)


    def ballHitEnemy(self,projectile,projectiles,enemy,enemylist):
        if  not projectiles.count(projectile) > 0: return
        seperation = enemy.pos-projectile.pos
        if projectile.owner == "player":
            if projectile.radius + enemy.radius >= seperation.length():
                if not enemy.found and enemy.stealthDistance(enemy):
                    enemy.health -= 100
                elif not enemy.found:
                    enemy.found = True
                    enemy.health -= projectile.damage
                else:
                    enemy.health -= projectile.damage
                    try:
                        projectiles.pop(projectiles.index(projectile))
                    except ValueError:
                        print("Projectile missing error")
                if enemy.health <= 0:
                    enemylist.pop(enemylist.index(enemy))

    def ballHitBoss(self,projectile,projectiles,boss,inventory):
        if  not projectiles.count(projectile) > 0: return
        seperation = boss.pos-projectile.pos
        if projectile.owner == "player":
            if projectile.radius + boss.radius >= seperation.length():
                    boss.health -= projectile.damage/inventory.activeAbility.baseDamage
                    try:
                        projectiles.pop(projectiles.index(projectile))
                    except ValueError:
                        print("Projectile missing error")
            if boss.health <= 0:
                boss.death = True

    def laserHitBoss(self,laser,lasers:list,boss):
        enemyRadius = max(boss.boss.scaleX,boss.boss.scaleY)/2
        if laser.distanceTo(boss) <= enemyRadius + laser.thickness/2 and (laser.pA-boss.pos).length() < laser.length:
            boss.health -= Laser().baseDamage/boss.damageResistence
        if boss.health <= 0:
            boss.death = True

    def laserHitEnemy(self,laser,lasers:list,enemy,enemylist:list):
        enemyRadius = max(enemy.enemyIMG.scaleX,enemy.enemyIMG.scaleY)/2
        if laser.distanceTo(enemy) <= enemyRadius + laser.thickness/2 and (laser.pA-enemy.pos).length() < laser.length:
            enemy.health -= Laser().baseDamage
            enemy.found = True
        if enemy.health <= 0:
            enemylist.pop(enemylist.index(enemy))

    def playerTouchPickup(self,pickup,pickups:list,character,inventory,canvas):
        if pickups.count(pickup) > 0:
            seperation:Vector = (pickup.pos-character.pos).length()
            if seperation <= pickup.radius +character.radius:
                if pickup.type == "powerup":
                    if pickup.value == "speed":
                        character.speedStack += 1
                        SpeedPowerUp().Apply(character,inventory)
                    elif pickup.value == "damage":
                        character.damageStack += 1
                        self.dmgP.Apply(character,inventory)
                    elif pickup.value == "stamina":
                        StaminaPowerUp().Apply(character)
                        character.staminaStack += 1
                    elif pickup.value == "heart":
                        pickups.pop(pickups.index(pickup))
                        return True
                else:
                    character.pickup(pickup,inventory)
                pickups.pop(pickups.index(pickup))
                return False

    def playerPickupsHeart(self,noHeart, heart,hearts:list, character):
        seperation: Vector = (heart.pos - character.pos).length()
        if seperation <= heart.radius + character.radius:
            hearts.pop(hearts.index(heart))
            return True
        return False
        # print(noHeart)

    def playerTouchTeleporter(self,teleporter,player,nextMap):
        seperation = (teleporter.pos-player.pos).length()
        if seperation < max(teleporter.dim[0],teleporter.dim[0]) + player.radius:
            player.vel = Vector(0,0)
            player.pos = teleporter.pos.copy()
            nextMap()