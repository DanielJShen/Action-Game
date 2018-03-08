import math
from os import walk


class Inventory:

    def __init__(self, CANVAS_WIDTH, CANVAS_HEIGHT, player):

        self.abilities: list = []
        for (dirpath, dirnames, filenames) in walk('Classes/Abilities/'):
            self.abilities.extend(filenames)
            break
        for file in self.abilities:
            self.abilities[self.abilities.index(file)] = file = file.split('.')[0]
            command = 'from Classes.Abilities.' + file + ' import ' + file
            exec(command, globals())

        self.activeAbility = player.activeAbility = eval(self.abilities[0])()
        self.availableAbilities = []  # Items the user has
        self.activePowerups = []  # Lists all active power ups
        self.powerups = []  # Lists all power ups
        self.abilityCount = self.abilities.__len__()  # Ability count from abilities list
        self.released = True  # Stores if the inventory button has been released while the inventory is open
        self.isOpen = False  # Determines if the inventory should be open or closed
        self.radius = min(CANVAS_WIDTH, CANVAS_HEIGHT) // 9  # Radius of the inventory wheel
        self.thickness = min(CANVAS_WIDTH, CANVAS_HEIGHT) // 12  # Thickness of the inventory wheel
        self.pos = []  # Position of the inventory wheel
        self.mousePos = [0, 0]  # Stores the current position of the mouse
        self.angle = 0  # Angle of the line between the inventory wheel and cursor
        self.selected = 0

    def update(self, keyboard, pos, mousePos):  # Update method to be called each game loop
        self.pos = pos
        self.mousePos = mousePos
        if self.isOpen:
            self.angle = math.atan2(self.pos[0] - self.mousePos[0], self.pos[1] - self.mousePos[1])

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
                if self.abilities[i] == self.activeAbility.__class__.__name__:
                    borderColour = '#FF0000'
                else:
                    borderColour = '#555555'
                radius = self.thickness // 2.2  # Radius of inventory wheel slots
                if ((i - 0.5) / self.abilityCount * 2 * math.pi) <= self.angle <= (
                        (i + 0.5) / self.abilityCount * 2 * math.pi):
                    self.selected = i
                #  Split for clarity
                elif ((i - 0.5 - self.abilityCount) / self.abilityCount * 2 * math.pi) <= self.angle <= (
                        (i + 0.5 - self.abilityCount) / self.abilityCount * 2 * math.pi):
                    self.selected = i
                else:
                    canvas.draw_circle(
                        (self.pos[0] + self.radius * -math.sin(i / self.abilityCount * 2 * math.pi),
                         self.pos[1] + self.radius * -math.cos(i / self.abilityCount * 2 * math.pi)),
                        radius, 2, borderColour, '#777777')

            #Draw selected circle
            if self.abilities[self.selected] == self.activeAbility.__class__.__name__:
                borderColour = '#FF0000'
            else:
                borderColour = '#555555'
            radius = self.thickness // 1.8
            canvas.draw_circle(
                (self.pos[0] + self.radius * -math.sin(self.selected / self.abilityCount * 2 * math.pi),
                 self.pos[1] + self.radius * -math.cos(self.selected / self.abilityCount * 2 * math.pi)),
                radius, 2, borderColour, '#777777')

    def select(self,player):  # Select either a powerup or ability in the inventory wheel
        self.isOpen = False
        print("Clicked: ",self.abilities[self.selected])
        self.activeAbility = player.activeAbility = eval(self.abilities[self.selected])()

    def enableAbility(self):  # Weapon being used
        pass

    def usePowerUp(self, powerup):  # Remove it from inventory and add to game loop
        pass
