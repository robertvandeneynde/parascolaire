#!/usr/bin/env python3
#!coding: utf-8

"""
Ce code montre comment on peut fermer le programme en cliquant sur la croix
"""

from __future__ import print_function, division

import pygame

pygame.init()

taille = [700, 500]
ecran = pygame.display.set_mode(taille)

clock = pygame.time.Clock()

fini = 0
while fini == 0:
    # pendant qu'on attendait, des événements se sont passé
    # on a cliqué sur la croix, on a appuyé sur une touche..
    # pygame.event.get() renvoie la liste d'événement
    liste_event = pygame.event.get()
    
    # on parcourt tous les événements...
    i = 0
    while i < len(liste_event):
        event = liste_event[i]
        
        # chaque event a un type
        # si le type de l'event est "pygame.QUIT" c'est qu'on a cliqué sur la croix
        if event.type == pygame.QUIT:
            # on met "fini" à 1 pour que la boucle while fini == 0 soit fausse
            # et donc que le programme finisse
            fini = 1
        
        # on passe à l'événement suivant
        i = i + 1
    
    clock.tick(60)

pygame.quit()
