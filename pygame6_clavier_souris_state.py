#!/usr/bin/env python3
#!coding: utf-8

"""
ici on va faire un test à chaque tick : SI la touchée est enfoncée, on fait l'action
TANT QUE gauche est enfoncée : ma_position diminue
TANT QUE gauche est enfoncée : ma_position augmente
TANT QUE le bouton de la souris est enfoncé
Attention ! Ce TANT QUE se traduit par un if à chaque tick
De la même manière que "TANT QUE le perso est en vie, on l'affiche" est traduit par 
"À chaque tick, SI le perso est en vie, on l'affiche"

on fait donc une action à chaque tick si la touchée est enfoncée
cela arrive dans un jeu quand on
- bouge
- tourne
- tire à la mitraillette (un missile par tick)
- tire un rayon laser continu

Pour savoir le numéro des touches, vous pouvez faire print event.key dans
un KEYDOWN event (voir fichier précédent)
Cependant pygame contient des variables bien nommées contenant les numéros des touches
pygame.K_LEFT = 276 par exemple
on peut donc faire if pressed[pygame.K_LEFT] à la place de if pressed[276]
tous les noms ici : https://www.pygame.org/docs/ref/key.html
cependant, sous windows, les touches correspondent au clavier QWERTY
"""

from __future__ import print_function, division

import pygame

pygame.init()

taille = [700, 500]
ecran = pygame.display.set_mode(taille)

clock = pygame.time.Clock()

rouge = [255,0,0]
blanc = [255,255,255]

ma_position = 10

fini = 0
while fini == 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    
    pressed = pygame.key.get_pressed() # liste contenant l'état des touches du clavier
    
    # à chaque tick...
    # si Gauche est enfoncée
    if pressed[276]: # 276: touche gauche (voir le fichier pygame5 pour connaître les numéros de toutes les touches)
        ma_position = ma_position - 5
    
    if pressed[275]: # 275: touche droite
        ma_position = ma_position + 5
    
    buttons = pygame.mouse.get_pressed() # liste contenant l'état des touches de la souris : gauche/milieu/droit
    
    if buttons[0]: # si le bouton de gauche de la souris est enfoncé
        position_souris = pygame.mouse.get_pos() # liste de taille 2 avec x,y
        ma_position = position_souris[0]
    
    # dessin
    ecran.fill(blanc)
    pygame.draw.rect(ecran, rouge, [ma_position, 20, 100, 200])
    
    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()
