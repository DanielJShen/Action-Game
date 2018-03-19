from Classes.PowerUps.PowerUp import PowerUp

class StaminaPowerUp(PowerUp):
    def __init__(self):
        self.staminaReg = 0.2
        self.stack = 0


    def Apply(self,player): #Changes the timer within projectile so the projectile lasts longer
        player.staminaReg += self.staminaReg #expected this to be harder
        self.stack += 1
