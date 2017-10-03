#!coding: utf-8
"""
Fichier 2: une écriture alternative
La flèche droite permet maintenant de parcourir les couleurs dans le sens inverse, es-tu d'accord avec le code ?
Les couleurs sont maintenant rajoutées à la liste "couleurs" en utilisant .append() est ce que tu trouves ça plus pratique ?
Une boucle "for" permet maintenant de rajouter plein de couleurs générées automatiquement à la liste.
Est-ce que tu sais obtenir de nouvelles couleurs en modifiant la manière dont les valeurs rouge, vert et bleu sont calculées ?
Note: range(1, 26) fait que i vaudra successivement 1, 2, 3, ..., 24, 25.
Attention seules les valeurs entre 0 et 255 sont admises! 0 représentant "pas de couleur" et 255 "couleur maximale"
Ainsi (255, 0, 0) veut dire "un max de rouge, pas de vert, pas de bleu"
Ainsi (255, 255, 255) veut dire "un max de rouge, de vert et de bleu" donc du blanc (lumière pure)
Ainsi (0, 0, 0) veut dire "pas de rouge, ni vert ni bleu" donc du noir (pas de lumière)

Deux cercles sont maintenant en bas de l'écran, leur couleurs par défaut est bleur. Peut tu modifier le code pour qu'il affiche la prochaine couleur à droite et à gauche?
Pour que cela soit plus visible peut tu faire en sorte que cela affiche la couleur qui apparaiterais si l'utilisateur appuyais 3 fois sur la flèche correspondante?
"""
from __future__ import division, print_function

import pygame

pygame.init()
taille_fenetre = [700, 700]
fenetre = pygame.display.set_mode(taille_fenetre)
horloge = pygame.time.Clock()

couleurs = []

couleurs.append((255, 255, 255))
couleurs.append((0, 0, 0))

for i in range(1, 26):
    rouge = i * 5
    vert = i * 10
    bleu = 0
    couleurs.append((rouge, vert, bleu))

fenetre_active = 1
couleur_active = 0

while fenetre_active == 1:

    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            fenetre_active = 0
        if evenement.type == pygame.KEYDOWN:
            if evenement.key == pygame.K_LEFT:
                couleur_active += 1
                if couleur_active > len(couleurs) - 1:
                    couleur_active = 0
            if evenement.key == pygame.K_RIGHT:
                couleur_active -= 1
                if couleur_active < 0:
                    couleur_active = len(couleurs) - 1

    fenetre.fill(couleurs[couleur_active])

    pygame.draw.circle(fenetre, (0, 0, 255), [35, 700 - 35], 25)  # Cercle gauche
    pygame.draw.circle(fenetre, (0, 0, 255), [700 - 35, 700 - 35], 25)  # Cercle droit

    pygame.display.flip()
    horloge.tick(60)
