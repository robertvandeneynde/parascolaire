#!coding: utf-8
from __future__ import print_function, division

import pygame

pygame.init()

taille = [700, 500]
ecran = pygame.display.set_mode(taille)

# on crée une clock qui va gérer les fps (frame par seconde / image par seconde)
clock = pygame.time.Clock()

fini = 0
while fini == 0:
    print("Tick")
    
    # on demande à la clock de faire en sorte que notre jeu tourne à du 60 fps
    clock.tick(2)

pygame.quit()

# Vous verrez que le code va faire print "Tick" 60 fois par secondes
# Changez le 60 en 2 et vous verrez que c'est plus facile à voir ;)

# pour fermer le programme, il faut quitter brutalement pyscripter... ctrl-shift-escape