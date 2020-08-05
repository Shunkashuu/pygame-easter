import pygame

class Panier(pygame.sprite.Sprite):

    def __init__(self, largeur_ecran, hauteur_ecran):
        super().__init__()
        self.largeur_ecran = largeur_ecran
        self.points = 0
        self.image = pygame.image.load('assets/panier.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = (largeur_ecran /2) - self.image.get_width() /2
        self.rect.y = hauteur_ecran - 170
        self.velocity = 5

    def deplacement_droite(self):
        if self.rect.x + self.image.get_width() < self.largeur_ecran:
            self.rect.x += self.velocity

    def deplacement_gauche(self):
        if self.rect.x > 0:
            self.rect.x -= self.velocity