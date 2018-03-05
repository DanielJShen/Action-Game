from Classes.Abilities.Ability import Ability
import math


class Inventory:

    def __init__(self, CANVAS_WIDTH, CANVAS_HEIGHT):
        self.enabledAbility = Ability
        self.abilities = []  # Items the user has
        self.activePowerups = []  # Lists all active power ups
        self.powerups = []  # Lists all power ups
        self.abilityCount = 7  # Temporary ability count for testing purposes
        self.released = True  # Stores if the inventory button has been released while the inventory is open
        self.isOpen = False  # Determines if the inventory should be open or closed
        self.radius = min(CANVAS_WIDTH, CANVAS_HEIGHT) // 9  # Radius of the inventory wheel
        self.thickness = min(CANVAS_WIDTH, CANVAS_HEIGHT) // 12  # Thickness of the inventory wheel
        self.pos = []  # Position of the inventory wheel

    def update(self, keyboard, pos):  # Update method to be called each game loop
        self.pos = pos

        if keyboard.i and self.released:
            self.isOpen = True
        elif not keyboard.i and self.isOpen:
            self.released = False
        elif keyboard.i and not self.released:
            self.isOpen = False
        else:
            self.released = True

    def draw(self, canvas):  # Draw method to be called each game loop
        if self.isOpen:
            canvas.draw_circle((self.pos[0], self.pos[1]),
                               self.radius, self.thickness, '#666666', )

            for i in range(self.abilityCount):
                canvas.draw_circle(
                    (self.pos[0] + self.radius * -math.sin(i / self.abilityCount * 2 * math.pi),
                     self.pos[1] + self.radius * -math.cos(i / self.abilityCount * 2 * math.pi)),
                    self.thickness // 2.2, 2, '#555555', '#777777')

    def drag(self, pos):  # Highlights the selected powerup or ability
        pass

    def select(self, pos):  # Select either a powerup or ability in the inventory wheel
        self.isOpen = False

    def enableAbility(self):  # Weapon being used
        pass

    def usePowerUp(self, powerup):  # Remove it from inventory and add to game loop
        pass
