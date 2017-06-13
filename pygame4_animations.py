#!coding: utf-8
from __future__ import print_function, division

import pygame

pygame.init()

taille = [700, 500]
ecran = pygame.display.set_mode(taille)

clock = pygame.time.Clock()

rouge = [255,0,0]
blanc = [255,255,255]

# on va utiliser une variable pour se souvenir de la position de notre rectangle
ma_position = 10

sens = 0
fini = 0
while fini == 0:
    # pour tous les événements qui se sont passsés depuis la dernière fois
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # si l'event est de type QUIT
            fini = 1 # on met fini à 1, ce qui va quitter la boucle à la fin de ce tick
    
    # déplacement
    ma_position = ma_position + 10
    
    # dessin
    ecran.fill(blanc)
    pygame.draw.rect(ecran, rouge, [ma_position, 20, 100, 200])
    
    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()

# on met tout ensemble !
# à chaque tick, on va re-dessiner tout l'écran :
# par contre, on va dessiner un rectangle en utilisant une
# variable qui change à chaque tick
# on a créé une "magnifique" animation :
# un carré qui bouge de 10 pixels vers la droite 60 fois par seconde...
