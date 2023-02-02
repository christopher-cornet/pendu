import pygame

pygame.init()
window = pygame.display.set_mode((700, 500))
center = window.get_rect().center
background_img = pygame.image.load("pendu/hangman.png")
surface = window
color = (100,149,237)

# Créer un menu: le joueur choisit s'il veut jouer ou insérer un mot dans le fichier mots.txt.
def menu():
    # Bouton jouer, Bouton ajouter un mot, Bouton difficulté
    pygame.display.set_caption("Menu")
    bouton_play = pygame.image.load("pendu/bouton-difficulty.png")
    window.blit(bouton_play, (40, 120))
    bouton_play = pygame.image.load("pendu/bouton-play.png")
    window.blit(bouton_play, (40, 200))
    bouton_play = pygame.image.load("pendu/bouton-add.png")
    window.blit(bouton_play, (40, 280))
    pygame.display.flip()
    
    # Si menu = jouer
    # play()
    # Si menu = ajouter
    # addWord()
    # Si menu = difficulty
    # difficulty()
    pass

def play():
    # Si menu = jouer
    # play()
    # Remplacer le _ par la lettre découverte
    pass

def addWord():
    # Si menu = ajouter
    # addWord()
    # Ouvrir fichier mots.txt
    # Ecrire l'input
    # Fermer
    pass

# A chaque nouvelle partie, un mot est choisi de façon aléatoire dans ce fichier et un ‘_’
# est affiché pour chaque lettre à découvrir.
def randomWord():
    # Prendre un mot aléatoirement dans le fichier txt
    # Remplacer chaque lettre par _ (boucle for)
    pass

# Pour choisir les lettres, le joueur doit utiliser les touches du clavier.
def keyChoice():
    # Si le user clique sur une touche qui est égale à une bonne lettre
    # discoverLetter()
    # Si lettre en dehors de l'alphabet, message d'erreur
    pass

def discoverLetter():
    # Si le user découvre une bonne lettre
    # Remplacer le _ par la lettre découverte
    pass

def win():
    # Si win = True
    # score (user) += 1
    pass

# Aller plus loin:

# Donner la possibilité de choisir le niveau de difficulté de la partie.
def difficulty():
    # Si le user clique sur une touche qui est égale à une bonne lettre
    # discoverLetter()
    pass

# Système de score.
# scores.txt dans lequel on y trouvera le nom du joueur ainsi que son score.
def score():
    # Score
    pass

# Créer un tableau des scores qui sera disponible depuis le menu de jeu.
def scoreboard():
    pass

running = True

window.fill((0, 0, 0))
window.blit(background_img, (0, 0))

menu()
pygame.display.update()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False