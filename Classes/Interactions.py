from Classes.Vector import Vector
import math
class Interactions:
    def __init__(self):
        pass
    def bounceBallOffWall(self,projectile,wall):
        if projectile.bounce():
            if projectile.radius + wall.halfThickness >= wall.distanceTo(projectile):
                if wall.inBounds(projectile):
                    wall.reflect(projectile)
            # else:
            #     wall.reflectEdge(projectile)
        else:
            pass #Remove projectile

    def ballHitPlayer(self,projectile,player,projectiles):
        seperation = player.pos-projectile.pos
        if not projectile.owner == "player":
            if projectile.radius + player.radius >= seperation.length():
                player.health -= projectile.damage
                projectiles.pop(projectiles.index(projectile))

    def playerHitWall(self,wall,player):
        if max(player.size[0],player.size[1])/2 + wall.halfThickness >= wall.distanceTo(player):
            if wall.playerInBounds(player):
                direction:Vector = player.vel.getProj(wall.line.getNormal()).getNormalized().negate()
                distance = ((player.radius + wall.halfThickness + 1) - wall.distanceTo(player))

                player.vel:Vector = player.vel.getProj(wall.line.getNormalized())
                player.pos.add(direction*distance)
        pass