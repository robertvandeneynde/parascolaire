#!/usr/bin/env python3
#!coding: utf-8

"""
On crée des images, et on les blitte (blit = dessiner).
Plus d'infos [ici](http://programarcadegames.com/index.php?chapter=bitmapped_graphics_and_sound&lang=fr).

Attention aux images tournées, leur taille change.
Essayez de faire pygame.draw.rect(ecran, rouge, [0,0,image_perso_tournee.get_width(), image_perso_tournee.get_height()], 1)
Question : comment faire pour dessiner une image telle sorte que son centre soit en 200,300 ?

Certaines images ne gèrent pas la transparence, cependant en écrivant
image_perso.set_colorkey(noir)
on lui indique la couleur qui doit devenir transparente à l'affichage
"""

from __future__ import print_function, division

import pygame

pygame.init()

taille = [700, 500]
ecran = pygame.display.set_mode(taille)

clock = pygame.time.Clock()

noir = [0,0,0]
rouge = [255,0,0]
blanc = [255,255,255]

# on charge l'image
image_perso = pygame.image.load('player.png').convert_alpha() # Téléchargez l'image [ici](https://robertvandeneynde.be/parascolaire/player.png)
# image_perso est une "surface de pixels"
# convert_alpha va garder la transparence

# on peut savoir sa taille
print("Taille :", image_perso.get_width(), image_perso.get_height())

# on peut même avoir une version tournée, et/ou redimensionnée
image_perso_tournee = pygame.transform.rotozoom(image_perso, 30, 1) # 30 degrés, taille gardée (x1)

ma_position = 10

fini = 0
while fini == 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    
    ma_position = ma_position + 2
    
    # dessin
    ecran.fill(blanc)
    
    # on peut "blitter" une image sur n'importe quelle surface, comme l'écran, ou une autre image
    ecran.blit(image_perso, [ma_position, 200])
    ecran.blit(image_perso_tournee, [0, 0])
    
    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()
