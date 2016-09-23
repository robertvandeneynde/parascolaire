#!coding: utf-8
'''
Ceci est le code pygame de base pour afficher une fenêtre.
De courts commentaires sont écrits pour pouvoir vous lancer rapidement dans un projet.
Si vous voulez des explications progressives et plus détaillées lisez :
pygame1_dessin.py, pygame2_tick.py, pygame3_events.py et pygame4_animations.py
'''

# 0) importer pygame, fatalement
import pygame

# 1) initialiser pygame
pygame.init()

# définir des couleurs : [Rouge, Vert, Bleu] (voir paint)
NOIR = [0, 0, 0]
BLANC = [255, 255, 255]
ROUGE = [255, 0, 0]
VERT = [0, 255, 0]
BLEU = [0, 0, 255]

# initaliser des variables
ma_position = 100 # On commence à 100 pixels

# 2) créer un écran : 700x500 pixels pour nous !
taille = [700, 500]
ecran = pygame.display.set_mode(taille)

# 3) faire une clock qui va gérer les fps
clock = pygame.time.Clock()

# 4) boucle principale
fini = 0
while fini == 0:
    
    # 5) lire les événements qui se sont passés depuis la dernière fois 
    for event in pygame.event.get():
        # si on a cliqué sur la croix...
        if event.type == pygame.QUIT:
            fini = 1 # la boucle principale va s'arrêter
    
    # 6) UPDATE : Faire quelque chose à chaque instant/image
    
    ma_position += 1 # on bouge de 1 pixel à droite
    
    # 7) DESSIN : on remplit l'écran de BLANC
    ecran.fill(BLANC)
    
    # 8) on dessine quelque chose, sinon, on ne verra rien
    pygame.draw.rect(ecran, ROUGE, [100,200, 20,40]) # coin en haut à gauche : x=100 y=200, taille 20x40
    pygame.draw.circle(ecran, BLEU, [100,200], 20) # centre : x=100 y=200, rayon=20
    pygame.draw.circle(ecran, VERT, [ma_position, 20], 10) # un cercle vert qui bouge
    
    # 9) mettre à jour 
    pygame.display.flip()
    
    # 10) attendre la clock avec les bons fps !
    clock.tick(60) # 60 images par secondes (frame per second / fps)
    
# 11) quitter... ça peut servir
pygame.quit()
    