import pygame, sys
from pygame.locals import *
import random

CLOCK = pygame.time.Clock()
FPS = 60
pygame.init()
WIDTH, HEIGHT = 640, 480
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

font = pygame.font.SysFont("Impact", 40)

# Créer un texte et le styliser
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# Ecran principal
def main_screen():
    click = False
    while True:
        # Couleur de fond
        SCREEN.fill((40,40,40))
        pygame.display.set_caption("Hangman Game - Main menu")
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

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                # Echap = quitte le jeu
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Si clic souris alors click = True
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        CLOCK.tick(FPS)

# Le pendu
def hangman_game():
    click = False

    # Choisir un mot au hasard dans le fichier texte
    with open("mots.txt", "r", encoding='UTF-8') as file:
        word = file.read() # Lire tous les caractères du fichier
        words = word.split() # String en liste
        random_word = random.randint(0, len(words)-1) # Choisir un mot aléatoirement
        underscore = '_ ' * len(words[random_word]) # Mot sous forme de tiret

    print(words[random_word])

    running = True
    while running:
        # Couleur de fond
        SCREEN.fill((40,40,40))
        pygame.display.set_caption('Hangman Game')
        draw_text('Hangman Game', font, (255, 255, 255), SCREEN, 195, 50)
        # Mettre le mot en tiret
        for i in words[random_word]:
            draw_text(underscore, font, (255, 255, 255), SCREEN, 100, 170)
        # Coordonnées souris
        mouse_x, mouse_y = pygame.mouse.get_pos()
    
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                # Echap = quitte le jeu
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Si clic souris alors click = True
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        CLOCK.tick(FPS)

# Ajout de mots
def add_words():
    click = False
    running = True
    # Mot de l'utilisateur
    new_word = ''
    while running:
        # Couleur de fond
        SCREEN.fill((40,40,40))
        pygame.display.set_caption('Hangman Game - Add a word')
        draw_text('Hangman Game', font, (255, 255, 255), SCREEN, 195, 50)
        draw_text('New word', font, (255, 255, 255), SCREEN, 100, 200)

        # Coordonnées souris
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Bouton menu
        button_menu = pygame.Rect(25, 25, 120, 70)
        pygame.draw.rect(SCREEN, (255, 216, 39), button_menu, 0, 5)
        draw_text('Menu', font, (255, 255, 255), SCREEN, 40, 30)

        # Retour au menu
        if button_menu.collidepoint((mouse_x, mouse_y)):
            if click:
                main_screen()

        # Bouton d'ajout
        button_add = pygame.Rect(400, 250, 120, 70)
        pygame.draw.rect(SCREEN, (99, 189, 63), button_add, 0, 25)
        draw_text('Add', font, (255, 255, 255), SCREEN, 425, 260)

        # Entrée utilisateur
        button_user_entry = pygame.Rect(50, 250, 260, 70)
        pygame.draw.rect(SCREEN, (112, 212, 72), button_user_entry, 0, 5)

        # Bouton d'ajout
        if button_add.collidepoint((mouse_x, mouse_y)):
            if click:
                print("test")
                file = open('mots.txt', 'a')
                file.write('\n' + new_word)
                file.close()
    
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                # Echap = quitte le jeu
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                # Efface le dernier caractère que l'utilisateur a rentré
                if event.key == pygame.K_BACKSPACE:
                    new_word = new_word[:-1]
                else:
                    new_word += event.unicode
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Si clic souris alors click = True
                if event.button == 1:
                    click = True
  
        text_surface = font.render(new_word, True, (255, 255, 255))
        SCREEN.blit(text_surface, (button_user_entry.x+5, button_user_entry.y+5))
            
        pygame.display.update()
        CLOCK.tick(FPS)
 
# Modes de difficulté
def difficulty():
    click = False
    running = True
    while running:
        # Couleur de fond
        SCREEN.fill((40,40,40))
        pygame.display.set_caption("Hangman Game - Difficulty mode")
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
                main_screen()
        if button_2.collidepoint((mouse_x, mouse_y)):
            if click:
                print("normal")
                main_screen()
        if button_3.collidepoint((mouse_x, mouse_y)):
            if click:
                print("difficile")
                main_screen()

        # Print les boutons, le background, le texte
        pygame.draw.rect(SCREEN, (255, 216, 39), button_menu, 0, 5)
        pygame.draw.rect(SCREEN, (112, 212, 72), button_1, 0, 25)
        pygame.draw.rect(SCREEN, (85, 134, 255), button_2, 0, 25)
        pygame.draw.rect(SCREEN, (255, 0, 0), button_3, 0, 25)
        draw_text('Menu', font, (255, 255, 255), SCREEN, 40, 30)
        draw_text('Easy', font, (255, 255, 255), SCREEN, 60, 260)
        draw_text('Normal', font, (255, 255, 255), SCREEN, 265, 260)
        draw_text('Hard', font, (255, 255, 255), SCREEN, 505, 260)
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                # Echap = quitte le jeu
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Si clic souris alors click = True
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        CLOCK.tick(FPS)
 
main_screen()