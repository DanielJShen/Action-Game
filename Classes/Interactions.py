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
            if projectile.radius + player.size[0] >= seperation.x and projectile.radius + player.size[1] >= seperation.y:
                player.health -= projectile.damage
                projectiles.pop(projectiles.index(projectile))