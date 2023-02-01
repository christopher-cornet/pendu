import pygame

window = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Pendu")
pygame.init()

# Créer un menu: le joueur choisit s'il veut jouer ou insérer un mot dans le fichier mots.txt.
def menu():
    surface.fill(color)
    pygame.display.flip()
    # Bouton jouer, Bouton ajouter un mot, Bouton difficulté
    
    # Si menu = jouer
    # play()
    # Si menu = ajouter
    # addWord()
    # Si menu = difficulty
    # difficulty()
    pass

def play():
    # Si menu = jouer
    # Remplacer le _ par la lettre découverte
    pass

def addWord():
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

surface = window
color = (100,149,237)

while running:
    menu()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False