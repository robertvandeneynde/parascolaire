#!coding: utf-8

# importer pygame, fatalement
import pygame

# pygame contient plein de fonctions pour utiliser les fenêtres 

# initialiser pygame
pygame.init()

# créer un écran : 700x500 pixels
taille = [700, 500]
ecran = pygame.display.set_mode(taille)
# ecran est une "surface" de 700x500 pixels

# maintenant qu'on a des pixels, on peut dessiner dessus
couleur = [253, 126, 0]
ecran.fill(couleur)

# on peut dessiner des rectangles avec draw.rect :
rouge = [255,0,0]
coordonnees = [10,20,100,200] # gauche, haut, largeur, hauteur
pygame.draw.rect(ecran, rouge, coordonnees)

# on peut aussi dessiner des cercles et plein d'autres formes
bleu = [0,0,255]
pygame.draw.circle(ecran, bleu, [110, 220], 20) # centre [110, 220], rayon 20

# finalement, il faut appliquer les dessins
pygame.display.flip()

# bloquer le programme avec une fonction, input() par exemple
input()

# pour ne pas avoir de problèmes avec pyscripter, on appelle "quit()" 
pygame.quit()

###########################
# Explications détaillées #
###########################

# la fonction pygame.display.set_mode crée une fenêtre et prends un paramètre :
# une liste de taille deux représentant la largeur et la hauteur de la fenêtre 
# elle renvoie une variable : ecran, celle ci représente la "Surface" de 700x500 pixels

# remarque que les deux lignes :
# taille = [700,500];
# ecran = pygame.display.set_mode(taille)

# peuvent s'écrire en une (question de style) :
# ecran = pygame.display.set_mode([700, 500])

# fill remplit l'écran avec la couleur [253,126,0],
# en informatique une couleur est une liste de taille 3
# Paint peut nous donner ces nombres ! (regarde l'image en attaché)
# tu vois sur l'image que 253, 126, 0 est un beau ORANGE :)

# pygame.draw.rect cette fonction prends 3 paramètres : 
# - la surface sur laquelle dessiner le rectangle, ici c'est l'écran
# - la couleur, ici on a donné [255,0,0] qui est du rouge flash
# - les coordonnées, une liste de taille 4
#   - la position en x (x = 0 est tout à gauche de l'écran, x = 10 est 10 pixels plus à DROITE)
#   - la position en y (y = 0 est tout en haut de l'écran, y = 20 est 20 pixels plus BAS)
#   - la largeur du rectangle, en pixels
#   - la hauteur du rectangle, en pixels
# la position donnée sera la position du coin en haut à gauche

# on peut également dessiner, des éllipses, des segments de droite, des polygones...
# https://www.pygame.org/docs/ref/draw.html

# Si on ne met pas "input()" à la fin du code,
# la fenêtre va se créer et puis disparaître à la fin du programme
# donc quasi instantanément
# il faut donc appeler une fonction qui bloque l'exécution, comme input

# pour quitter, ne cliquez pas sur la croix, ça ne marchera pas,
# cliquez sur le carré rouge dans pyscripter