from Classes.PowerUps.PowerUp import PowerUp


class DamagePowerUp(PowerUp):
    def __init__(self):
        self.damage = 3

    def Apply(self, player, inventory):  # Changes the speed within projectile
        for i in range(0, inventory.availableAbilities.__len__()):
            if inventory.availableAbilities[i] != inventory.activeAbility:
                inventory.availableAbilities[i].baseDamage += inventory.availableAbilities[i].baseDamage/self.damage
        player.activeAbility.baseDamage += player.activeAbility.baseDamage/self.damage
