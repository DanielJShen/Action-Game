class Interactions:
    def __init__(self):
        pass

    def bounceBallOffWall(self,projectiles,walls):
        for wall in walls:
            for projectile in projectiles:

                    if projectile.bounce():
                        wall.reflect(projectile)
                    else:
                        pass #Remove projectile