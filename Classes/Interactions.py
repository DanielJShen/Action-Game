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