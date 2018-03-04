from Classes.Abilities.Ability import Ability
import math


class Inventory:

    def __init__(self, CANVAS_WIDTH, CANVAS_HEIGHT):
        self.enabledAbility = Ability
        self.abilities = []  # Items the user has
        self.activePowerups = []  # Lists all active power ups
        self.powerups = []  # Lists all power ups
        self.abilityCount = 7  # Temporary ability count for testing purposes
        self.isOpen = False  # Determines if the inventory should be open or closed
        self.radius = min(CANVAS_WIDTH, CANVAS_HEIGHT) // 4
        self.thickness = min(CANVAS_WIDTH, CANVAS_HEIGHT) // 6
        self.color = 'Grey'

    def update(self, keyboard):  # Update method to be called each game loop
        if keyboard.i:
            self.isOpen = True
        else:
            self.isOpen = False
        pass

    def draw(self, canvas, CANVAS_WIDTH, CANVAS_HEIGHT):  # Draw method to be called each game loop
        if self.isOpen:
            canvas.draw_circle((CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2),
                               self.radius, self.thickness, '#666666', )

            for i in range(self.abilityCount):
                canvas.draw_circle(
                    (CANVAS_WIDTH // 2 + self.radius * -math.sin(i / self.abilityCount * 2 * math.pi),
                     CANVAS_HEIGHT // 2 + self.radius * -math.cos(i / self.abilityCount * 2 * math.pi)),
                    self.thickness // 2.2, 2, '#555555', '#777777')

    def enableAbility(self, ability):  # Weapon being used
        pass

    def usePowerUp(self, powerup):  # Remove it from inventory and add to game loop
        pass
