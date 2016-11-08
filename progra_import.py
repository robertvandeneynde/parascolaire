#!coding: utf-8

## IMPORT ##

# pour utiliser des fonctions externes, on utilise import

# 1) import <module>
import random # pour faire du hasard : randrange, randint, shuffle...
import pygame # notre bibliothèque de fenêtres favorite

# pour accéder aux fonctions et variables, on utilise module.variable
a = random.randint(5,10)
pygame.init()

# 2) import <module> as <name>

# on peut donner un petit nom au module importé
import random as r
import pygame as py
import pygame.draw as d
a = r.randint(5, 10)
py.init()
d.rect(ecran, [10, 20, 30, 40])

# 3) from
# on peut choisir de n'importer que certaines fonctions/variables
from random import randint, randrange
from random import shuffle as melange # en renommmant si on veut

L = [1,2,4]
melange(L)
x = randrange(4)

# 4) import *
# ou de tout prendre sans préfixer
from random import *

# on déconseille l'utilisation de "*",
# car cela devient difficile de savoir d'où viennent les fonctions/variables

## MODULES ##

# pour structurer, on peut aussi faire nos propres modules !
# j'ai fait un fichier appelé progra_module_exemple
# celui-ci contient des fonctions et des classes utiles

# j'utilise la 2ème manière d'importer
import program_module_exemple as m

bob = m.Personnage(85,100)
bob.boire_potion(25)

x = m.calcul(6)
y = m.TAILLE * 50