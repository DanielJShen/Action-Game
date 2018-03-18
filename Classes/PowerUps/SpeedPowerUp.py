from Classes.PowerUps.PowerUp import PowerUp
from Classes.Inventory import Inventory

class SpeedPowerUp(PowerUp):
    def __init__(self):
        self.speedBonus = 5

    def Apply(self,player,inventory): #Changes the speed within projectile
        for i in range(0,inventory.availableAbilities.__len__()):
            if inventory.availableAbilities[i] != inventory.activeAbility:
                inventory.availableAbilities[i].speed += self.speedBonus
        player.activeAbility.speed += self.speedBonus