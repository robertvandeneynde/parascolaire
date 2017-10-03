#!coding: utf-8
"""
Fichier 1: Changer avec les flèches les couleurs de l'arrière plan.
Es-tu capable de compléter le code afin que l'on puisse également utiliser la flèche droite? (pygame.K_RIGHT)
Note: couleur_active désigne le numéro de la couleurs actuellement affichée. Les couleurs sont numérotées de la manière suivante : 0, 1, 2 ,3, 4.
Il faut faire attention à ce que couleur_active ne prennent pas de valeur < 0 et > 4. Sinon une erreur se produira.

Si tu souhaites rajouter une couleur à la liste, combien de ligne devras tu modifier ? Est-ce que cela te semble long à faire ?
"""
from __future__ import division, print_function

import pygame

pygame.init()
taille_fenetre = [700, 700]
fenetre = pygame.display.set_mode(taille_fenetre)
horloge = pygame.time.Clock()

couleurs = [(0, 0, 0), (255, 255, 255), (0, 0, 255), (0, 255, 0), (255, 0, 0)]

fenetre_active = 1

couleur_active = 0

while fenetre_active == 1:

    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            fenetre_active = 0
        if evenement.type == pygame.KEYDOWN:
            if evenement.key == pygame.K_LEFT:
                couleur_active += 1
                if couleur_active > 4:
                    couleur_active = 0

    fenetre.fill(couleurs[couleur_active])
    pygame.display.flip()
    horloge.tick(60)
