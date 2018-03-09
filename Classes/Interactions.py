from Classes.Vector import Vector
import math
class Interactions:
    def __init__(self):
        pass

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

    def ballHitPlayer(self,projectile,player,projectiles,health):
        if projectiles.count(projectile) == 0: return
        seperation = player.pos-projectile.pos
        if not projectile.owner == "player":
            if projectile.radius + player.radius >= seperation.length():
                player.health -= projectile.damage
                health.damageTaken()
                try:
                    projectiles.pop(projectiles.index(projectile))
                except ValueError:
                    print("Projectile missing error")

    def playerHitWall(self,wall,player):
        if max(player.size[0],player.size[1])/2 + wall.halfThickness >= wall.distanceTo(player):
            if wall.playerInBounds(player):
                direction:Vector = player.vel.getProj(wall.line.getNormal()).getNormalized().negate()
                distance = ((player.radius + wall.halfThickness + 1) - wall.distanceTo(player))

                player.vel:Vector = player.vel.getProj(wall.line.getNormalized())
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