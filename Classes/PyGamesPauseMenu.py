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

def resume_game():
    print("resume game")

    
    #call the main game method from this function

def change_sound():
    print("change sound")
    

def change_resoultion():
    print("change resoultion")


pygame.init()

screen = pygame.display.set_mode((900, 900))
display = pygame.display.get_surface()
background_image = pygame.image.load("bg.bmp").convert()
menu_font = pygame.font.Font(None, 40)
menu_options = [Menu("RESUME GAME", (345, 225)), Menu("RESOULTION", (345, 285)),Menu("SOUND",(345,345)),Menu("QUIT", (345, 405))]
font = pygame.font.Font(None, 70)
text = font.render("GAME PAUSED", True, (0,0,0))



while True:

    screen.fill((0,0,0))
    
    for event in pygame.event.get():
        for mo in menu_options:
            if event.type == pygame.MOUSEBUTTONUP and mo.rect.collidepoint(pygame.mouse.get_pos()):
                if mo.get() == "RESUME GAME":
                    resume_game()
                elif mo.get() == "RESOULTION":
                    change_resoultion()
                elif mo.get() == "SOUND":
                    change_sound()
                elif mo.get() == "QUIT":
                    pygame.quit()
                    quit()
                        
    screen.blit(background_image, [0, 0])  
    screen.blit(text, (270, 80))
    
    for option in menu_options:
        if option.rect.collidepoint(pygame.mouse.get_pos()):
            option.hovered = True
        else:
            option.hovered = False

        option.draw()

    
    pygame.display.update()
