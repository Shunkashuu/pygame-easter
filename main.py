import pygame
from panier import Panier
pygame.init()

largeur = 800
hauteur = 480

fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Pygame Eggs")

running = True

fond = pygame.image.load('assets/fond.jpg')
sol = pygame.image.load('assets/sol.png')

touches_active = {}

panier = Panier(largeur, hauteur)

while running:

    fenetre.blit(fond, (0, 0))
    fenetre.blit(panier.image, panier.rect)
    fenetre.blit(sol, (0, 0))

    if touches_active.get(pygame.K_RIGHT):
        panier.deplacement_droite()
    elif touches_active.get(pygame.K_LEFT):
        panier.deplacement_gauche()

    pygame.display.flip()

    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            running = False
            quit()
        elif evenement.type == pygame.KEYDOWN:
            touches_active[evenement.key] = True
        elif evenement.type == pygame.KEYUP:
            touches_active[evenement.key] = False
