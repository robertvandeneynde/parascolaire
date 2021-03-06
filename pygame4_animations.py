#!/usr/bin/env python3 
#!coding: utf-8

"""
En mettant ensemble les trois exemples précédents, on peut créer une animation !
À chaque tick, on va re-dessiner tout l'écran
Mais ici, la commande qui dessine un rectangle utilisera une VARIABLE
Vu que cette variable change à chaque tick,
le dessin du premier tick sera différent du dessin du second !

On a créé une "magnifique" animation : un carré...
... qui bouge
... de 10 pixels
... vers la droite
... 60 fois par seconde

En effet, au début on a :
ma_position = 50

Ensuite, imaginons que l'utilisateur n'a pas cliqué sur la croix,
la boucle "for" ne fait donc rien.

Ensuite:
ma_position = ma_position + 10 # ma_position = 60 maintenant

Ensuite :
ecran.fill(blanc)
pygame.draw.rect(ecran, rouge, [ma_position, 20, 100, 200]) # rect(ecran, rouge, [60,20,100,200])
pygame.display.flip()

On a donc un rectangle en 60,20 de dimensions 100,200 !

Ensuite:
clock.tick(60) # on attend 1/60 secondes

On arrive au second tick:
Imaginons que l'utilisateur n'a pas cliqué sur la croix,
la boucle "for" ne fait rien.

Ensuite:
ma_position = ma_position + 10 # ma_position = 70 maintenant

Ensuite:
ecran.fill(blanc)
pygame.draw.rect(ecran, rouge, [ma_position, 20, 100, 200]) # rect(ecran, rouge, [70,20,100,200])
pygame.display.flip()

On a donc un rectangle en 70,20 de dimensions 100,200 !

Si on compare les deux images, on voit.
Deux images différentes séparées de 1/60 secondes, c'est une animation !
"""

from __future__ import print_function, division

import pygame

pygame.init()

taille = [700, 500]
ecran = pygame.display.set_mode(taille)

clock = pygame.time.Clock()

rouge = [255,0,0]
blanc = [255,255,255]

# on va utiliser une variable pour se souvenir de la position de notre rectangle
ma_position = 50

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
