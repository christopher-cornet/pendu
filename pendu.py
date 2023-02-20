import pygame
import sys

pygame.init()
FPS = 60
CLOCK = pygame.time.Clock()
WIDTH, HEIGHT = 640, 480
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu")

FONT = pygame.font.SysFont("Times New Romans", 40)

PLAYBGCOLOR = (0, 255, 0)

objects = []

class Button():
    def __init__(self, x, y, width, height, buttonText="Button", onclick=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclick = onclick
        self.onePress = onePress

        self.fillColors = {
            "normal": "#1285F2",
            "hover": "#124FF2",
            "pressed": "#101AEF",
        }

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)
        # Couleur du texte
        self.buttonSurf = FONT.render(buttonText, True, (255, 255, 255))

        self.alreadyPressed = False

        objects.append(self)

    def process(self):
        mouse_position = pygame.mouse.get_pos()
        
        self.buttonSurface.fill(self.fillColors["normal"])
        if self.buttonRect.collidepoint(mouse_position):
            self.buttonSurface.fill(self.fillColors["hover"])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors["pressed"])
                if self.onePress:
                    self.onclick()
                elif not self.alreadyPressed:
                    self.onclick()
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False

        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])
        SCREEN.blit(self.buttonSurface, self.buttonRect)

def play():
        Play()
        print("Fenêtre de jeu")
        return True

def addwords():
    AddWords()
    print("Fenêtre d'ajout de mots")

def difficulty():
    Difficulty()
    print("Fenêtre de difficulté")

class MainScreen():
    def __init__(self):
        button_play = Button(200, 70, 250, 100, "Jouer", play)
        button_add_words = Button(200, 180, 250, 100, "Ajouter des mots", addwords)
        button_difficulty = Button(200, 290, 250, 100, "Difficulté", difficulty)

class Play():
    def __init__(self):
        SCREEN.fill(PLAYBGCOLOR)
        pygame.display.update()

class AddWords():
    def __init__(self):
        SCREEN.fill((10,40,50))
        pygame.display.flip()

class Difficulty():
    def __init__(self):
        SCREEN.fill((255, 46, 46))
        pygame.display.flip()

MainScreen()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    for object in objects:
        object.process()

    pygame.display.flip()
    CLOCK.tick(FPS)