#!coding: utf-8
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
        
        # elif est un raccourci pour "if... else... if ... else..."
        elif event.type == pygame.KEYDOWN:
            print("La touche numero", event.key)
            if event.key == 276: # touche gauche
                ma_position = ma_position - 100
            elif event.key == 275: # touche droite
                ma_position = ma_position + 100
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # event.pos est une liste de taille 2 contenant le x et le y
            print("Clic en", event.pos[0], event.pos[1])
            ma_position = event.pos[0]
    
    # dessin
    ecran.fill(blanc)
    pygame.draw.rect(ecran, rouge, [ma_position, 20, 100, 200])
    
    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()

# on va contrôler le carré (gauche, droite) avec le clavier ou la souris
# QUAND on appuie sur gauche : ma_position diminue
# QUAND on appuie sur droite : ma_position augmente
# QUAND on clique avec le bouton gauche : ma_position est changée au clic de la souris

# ces events se passe quand la touche passe de l'état "non enfoncé" à "enfoncé"
# les events nous donne donc des TRANSITIONS d'état
# ce genre d'action arrive par exemple quand on
# - tire un missile
# - saute
# - change de sélection dans un menu

# remarquez qu'on peut coder la transition inverse avec KEYUP et MOUSEBUTTONUP

# Pour savoir le numéro d'une touche, on peut utiliser notre print "La touche numero", event.key
# Cependant pygame contient des variables bien nommées contenant les numéros des touches
# pygame.K_LEFT = 276 par exemple 
# on peut donc faire if event.key == pygame.K_LEFT à la place de if event.key == 276
# tous les noms ici : https://www.pygame.org/docs/ref/key.html
# cependant, sous windows, les touches correspondent au clavier QWERTY