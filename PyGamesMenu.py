import pygame,sys

class Menu:

    hovered = False


    def __init__(self, text, pos):
        self.text = text
        self.pos = pos
        self.set_rect()
        self.draw()


    def draw(self):
        self.set_rend()
        screen.blit(self.rend, self.rect)



    def set_rend(self):
        self.rend = menu_font.render(self.text, True, self.get_color())



    def get_color(self):
        if self.hovered:
            return (255, 255, 255)

        else:
            return (100, 100, 100)



    def set_rect(self):
        self.set_rend()
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.pos

    def get(self):
        return(self.text)

def call_game():
    global menu
    menu=False

def change_walls():
    global drawWalls
    drawWalls = not drawWalls

def change_resolution():
    global resolution
    if resolution == (1600,900):
        resolution = (1200,675)
    elif resolution == (1200,675):
        resolution = (2000,1125)
    elif resolution == (2000,1125):
        resolution = (1600,900)


pygame.init()

menu = True
global drawWalls,resolution
drawWalls = False
resolution = (1600,900)
screen = pygame.display.set_mode((900, 900))
display = pygame.display.get_surface()
background_image = pygame.image.load("Resources/images/bg.bmp").convert()
menu_font = pygame.font.Font(None, 40)
menu_options = [Menu("PLAY GAME", (345, 225)), Menu("RESOLUTION", (345, 285)),Menu("WALLS",(345,345)),Menu("QUIT", (345, 405))]
font = pygame.font.Font(None, 70)
text = font.render("ZELDA GAME", True, (0,0,0))


while menu==True:

    screen.fill((0,0,0))

    for event in pygame.event.get():
        for mo in menu_options:
            if event.type == pygame.MOUSEBUTTONUP and mo.rect.collidepoint(pygame.mouse.get_pos()):
                if mo.get() == "PLAY GAME":
                    call_game()
                elif mo.get() == "RESOLUTION":
                    change_resolution()
                elif mo.get() == "WALLS":
                    change_walls()
                elif mo.get() == "QUIT":
                    pygame.quit()
                    quit()

    screen.blit(background_image, [0, 0])
    screen.blit(text, (270, 80))

    font = pygame.font.Font(None, 40)
    screen.blit(font.render(resolution.__str__(), True, (100, 100, 100)), (600, 285))
    screen.blit(font.render(drawWalls.__str__(), True, (100, 100, 100)), (600, 345))

    for option in menu_options:
        if option.rect.collidepoint(pygame.mouse.get_pos()):
            option.hovered = True
        else:
            option.hovered = False

        option.draw()

    pygame.display.update()


pygame.quit()
del pygame

from Classes.Main import game

game(resolution,drawWalls)