import pygame, sys
from pygame.locals import *
import random

CLOCK = pygame.time.Clock()
FPS = 60
pygame.init()
pygame.display.set_caption('game base')
WIDTH, HEIGHT = 640, 480
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
 
font = pygame.font.SysFont("Impact", 40)
 
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# Ecran principal
def main_screen():
    click = False
    while True:
        # Fond noir
        SCREEN.fill((40,40,40))
        pygame.display.set_caption("Hangman Game")
        draw_text('Hangman Game', font, (255, 255, 255), SCREEN, 195, 50)
        # Coordonnées souris
        mouse_x, mouse_y = pygame.mouse.get_pos()
 
        # Boutons
        button_1 = pygame.Rect(225, 150, 200, 70)
        button_2 = pygame.Rect(225, 250, 200, 70)
        button_3 = pygame.Rect(225, 350, 200, 70)

        # Cliquer sur un bouton = ouvre une fenêtre
        if button_1.collidepoint((mouse_x, mouse_y)):
            if click:
                hangman_game()
        if button_2.collidepoint((mouse_x, mouse_y)):
            if click:
                add_words()
        if button_3.collidepoint((mouse_x, mouse_y)):
            if click:
                difficulty()

        # Print les boutons
        pygame.draw.rect(SCREEN, (112, 212, 72), button_1, 0, 25)
        pygame.draw.rect(SCREEN, (85, 134, 255), button_2, 0, 25)
        pygame.draw.rect(SCREEN, (255, 0, 0), button_3, 0, 25)
        draw_text('Play', font, (255, 255, 255), SCREEN, 290, 160)
        draw_text('Add words', font, (255, 255, 255), SCREEN, 240, 260)
        draw_text('Difficulty', font, (255, 255, 255), SCREEN, 250, 360)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                # Echap = quitte le jeu
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                # Si clic souris alors click = True
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        CLOCK.tick(FPS)

# Le pendu
def hangman_game():
    click = False
    # Mettre le mot 
    test = "key"
    for i in test:
        print('_')

    # Choisir un mot dans le fichier texte
    with open("pendu/mots.txt", "r") as file:
        word = print(file.readlines()[random.randint(0, 10)])
        print_word = str(word)

    running = True
    while running:
        # Fond noir
        SCREEN.fill((40,40,40))
        pygame.display.set_caption('Hangman Game')
        draw_text('Hangman Game', font, (255, 255, 255), SCREEN, 195, 50)
        draw_text(print_word, font, (255, 255, 255), SCREEN, 280, 150)
        # Coordonnées souris
        mouse_x, mouse_y = pygame.mouse.get_pos()
    
 
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                # Echap = quitte le jeu
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                # Si clic souris alors click = True
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        CLOCK.tick(FPS)

# Ajout de mots
def add_words():
    running = True
    while running:
        SCREEN.fill((0,0,0))
        draw_text('Add words', font, (255, 255, 255), SCREEN, 20, 20)
        word_append = "test"
        file = open('mots.txt', 'a')
        file.write("\n")
        file.close()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        CLOCK.tick(FPS)
 
# Modes de difficulté
def difficulty():
    click = False
    running = True
    while running:
        # Fond noir
        SCREEN.fill((40,40,40))
        pygame.display.set_caption("Hangman Game")
        draw_text('Hangman Game', font, (255, 255, 255), SCREEN, 195, 50)
        # Coordonnées souris
        mouse_x, mouse_y = pygame.mouse.get_pos()
 
        # Boutons
        button_menu = pygame.Rect(25, 25, 120, 70)
        button_1 = pygame.Rect(0, 250, 190, 70)
        button_2 = pygame.Rect(225, 250, 190, 70)
        button_3 = pygame.Rect(450, 250, 190, 70)

        # Cliquer sur un bouton = ouvre une fenêtre
        if button_menu.collidepoint((mouse_x, mouse_y)):
            if click:
                main_screen()
        if button_1.collidepoint((mouse_x, mouse_y)):
            if click:
                print("facile")
                return "facile"
        if button_2.collidepoint((mouse_x, mouse_y)):
            if click:
                print("normal")
                return "facile"
        if button_3.collidepoint((mouse_x, mouse_y)):
            if click:
                print("difficile")
                return "facile"

        # Print les boutons, le background, le texte
        pygame.draw.rect(SCREEN, (255, 216, 39), button_menu, 0, 25)
        pygame.draw.rect(SCREEN, (112, 212, 72), button_1, 0, 25)
        pygame.draw.rect(SCREEN, (85, 134, 255), button_2, 0, 25)
        pygame.draw.rect(SCREEN, (255, 0, 0), button_3, 0, 25)
        draw_text('Menu', font, (255, 255, 255), SCREEN, 40, 30)
        draw_text('Easy', font, (255, 255, 255), SCREEN, 60, 260)
        draw_text('Normal', font, (255, 255, 255), SCREEN, 265, 260)
        draw_text('Hard', font, (255, 255, 255), SCREEN, 505, 260)
 
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                # Echap = quitte le jeu
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                # Si clic souris alors click = True
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        CLOCK.tick(FPS)
 
main_screen()