import math
from os import walk

class Inventory:

    def __init__(self, CANVAS_WIDTH, CANVAS_HEIGHT):

        abilities:list = []
        for (dirpath, dirnames, filenames) in walk('Classes/Abilities/'):
            abilities.extend( filenames )
            break
        for file in abilities:
            abilities[abilities.index(file)] = file = file.split('.')[0]
            command = 'from Classes.Abilities.'+file+' import '+file
            exec(command,globals())

        self.enabledAbility = eval(abilities[0])()
        self.abilities = []  # Items the user has
        self.activePowerups = []  # Lists all active power ups
        self.powerups = []  # Lists all power ups
        self.abilityCount = 7  # Temporary ability count for testing purposes
        self.released = True  # Stores if the inventory button has been released while the inventory is open
        self.isOpen = False  # Determines if the inventory should be open or closed
        self.isDragged = False
        self.radius = min(CANVAS_WIDTH, CANVAS_HEIGHT) // 9  # Radius of the inventory wheel
        self.thickness = min(CANVAS_WIDTH, CANVAS_HEIGHT) // 12  # Thickness of the inventory wheel
        self.pos = []  # Position of the inventory wheel
        self.angle = 0  # Angle of the line between the inventory wheel and cursor

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
                radius = self.thickness // 2.2  # Radius of inventory wheel slots
                if ((i - 0.5) / self.abilityCount * 2 * math.pi) <= self.angle < (
                        (i + 0.5) / self.abilityCount * 2 * math.pi) and self.isDragged:
                    radius = self.thickness // 1.8
                #  Split for clarity
                elif ((i - 0.5 + self.abilityCount) / self.abilityCount * 2 * math.pi) <= self.angle and self.isDragged:
                    radius = self.thickness // 1.8

                canvas.draw_circle(
                    (self.pos[0] + self.radius * -math.sin(i / self.abilityCount * 2 * math.pi),
                     self.pos[1] + self.radius * -math.cos(i / self.abilityCount * 2 * math.pi)),
                    radius, 2, '#555555', '#777777')

    def drag(self, pos):  # Highlights the selected powerup or ability
        self.isDragged = True
        self.angle = math.atan2(self.pos[0] - pos[0], self.pos[1] - pos[1])
        if self.angle < 0:
            self.angle += 2 * math.pi

    def select(self, pos):  # Select either a powerup or ability in the inventory wheel
        self.isOpen = False
        self.isDragged = False

    def enableAbility(self):  # Weapon being used
        pass

    def usePowerUp(self, powerup):  # Remove it from inventory and add to game loop
        pass
