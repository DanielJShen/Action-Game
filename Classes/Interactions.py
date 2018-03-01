class Interactions:
    def __init__(self):
        pass
    def bounceBallOffWall(self,projectile,wall):
        if projectile.bounce():
            if projectile.radius + wall.thickness >= wall.distanceTo(projectile):
                if wall.inBounds(projectile):
                    self.inCollision = True
                    wall.reflect(projectile)
                else:
                    self.inCollision = True
                    wall.reflectEdge(projectile)
        else:
            pass #Remove projectile