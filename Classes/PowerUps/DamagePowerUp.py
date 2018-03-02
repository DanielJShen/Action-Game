from Classes.PowerUps.PowerUp import PowerUp


class DamagePowerUp(PowerUp):
    def __init__(self, projectile):
        self.projectile = projectile

    def Apply(self):  # Changes the damage within projectile
        pass
