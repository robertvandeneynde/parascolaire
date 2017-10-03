#!coding: utf-8
""" Fichier 3: Introduction d'un objet couleur. """
from __future__ import division, print_function

import pygame
pygame.init()

taille_fenetre = [700, 700]
fenetre = pygame.display.set_mode(taille_fenetre)
horloge = pygame.time.Clock()

class Couleur: # Permets de manipuler l'objet Color de pygame mais en ajoutant des foncitonalités.
    def __init__(self, rouge, vert, bleu):
        self.rouge = rouge
        self.bleu = bleu
        self.vert = vert

    def modifier_rouge(self, ajout):
        nouveau_rouge = self.rouge + ajout
        if nouveau_rouge >= 0 and nouveau_rouge <= 255:
            self.rouge = nouveau_rouge

    def modifier_bleu(self, ajout):
        nouveau_bleu = self.bleu + ajout
        if nouveau_bleu >= 0 and nouveau_bleu <= 255:
            self.bleu = nouveau_bleu

    def modifier_vert(self, ajout):
        nouveau_vert = self.vert + ajout
        if nouveau_vert >= 0 and nouveau_vert <= 255:
            self.vert = nouveau_vert

    def get_couleur(self):
        return pygame.Color(self.rouge, self.vert, self.bleu) # On appelle cette méthode qui renvoi un objet défini dans Pygame utilisable par draw ou fill !

couleurs = []
for i in range(1, 11):
    couleurs.append(Couleur(0, i * 25, 0))

fenetre_active = 1
couleur_active = 0

while fenetre_active == 1:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            fenetre_active = 0
        if evenement.type == pygame.KEYDOWN:
            if evenement.key == pygame.K_LEFT:
                couleur_active += 1
                if couleur_active > len(couleurs):
                    couleur_active = 0
            if evenement.key == pygame.K_RIGHT:
                couleur_active -= 1
                if couleur_active < 0:
                    couleur_active = len(couleurs) - 1

    fenetre.fill(couleurs[couleur_active].get_couleur())

    pygame.draw.circle(fenetre, couleurs[(couleur_active + 1) % len(couleurs)].get_couleur(), [35, 700 - 35], 25)  # Cercle gauche
    pygame.draw.circle(fenetre, couleurs[(couleur_active - 1) % len(couleurs)].get_couleur(), [700 - 35, 700 - 35], 25)  # Cercle droit

    pygame.display.flip()
    horloge.tick(60)
