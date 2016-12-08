#!coding: utf-8

import pygame
import random

pygame.init()

tx,ty = taille = [12*60, 500]
ecran = pygame.display.set_mode(taille, pygame.DOUBLEBUF)

clock = pygame.time.Clock()

ROUGE = [255,0,0]
VERT = [0,255,0]
BLEU = [0,0,255]
JAUNE = [255,255,0]
BLANC = [255,255,255]
NOIR = [0, 0, 0]
ORANGE = [255, 153, 0]
BLEU_CLAIR = [135, 206, 250]

class Balle:
    pass

balles = []

for i in range(5):
    b = Balle()
    b.taille = 20
    b.x = random.randrange(700 - b.taille)
    b.y = 300 + random.randrange(200)
    b.sx = random.choice([-1,1])
    b.sy = random.choice([-1,1])
    balles.append(b)

class Brique:
    pass

briques = []

for i in range(12):
    for j in range(5):
        r = Brique()
        r.vie = 3
        r.taille_x = 60
        r.taille_y = 30
        r.x = i * r.taille_x
        r.y = j * r.taille_y
        briques.append(r)
t = 0

fini = 0
while fini == 0:
    # pour tous les événements qui se sont passsés depuis la dernière fois
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # si l'event est de type QUIT
            fini = 1 # on met fini à 1, ce qui va quitter la boucle à la fin de ce tick
    
    # déplacement
    
    for b in balles:
        b.x += b.sx * 5
        b.y += b.sy * 5
        
        i = 0
        while i < len(briques):
            r = briques[i]
            if not(
                r.x > b.x + b.taille or
                r.y > b.y + b.taille or
                r.x + r.taille_x < b.x or
                r.y + r.taille_y < b.y
            ):
                b.x -= b.sx * 5
                b.y -= b.sy * 5
                
                dx = r.x - b.x if r.x > b.x else b.x - (r.x + r.taille_x)
                dy = r.y - b.y if r.y > b.y else b.y - (r.y + r.taille_y)
                if dx > dy:
                    b.sx *= -1
                else:
                    b.sy *= -1
                
                r.vie -= 1
                if r.vie == 0:
                    del briques[i]
                    i -= 1
                
            i += 1
        
        if b.x > tx - b.taille:
            b.sx = -1
        if b.x < 0:
            b.sx = 1
        if b.y > ty - b.taille:
            b.sy = -1
        if b.y < 0:
            b.sy = 1
        
    t += 1
    
    # dessin
    ecran.fill(BLEU_CLAIR)

    for r in briques:
        
        color = (ROUGE if r.vie == 3 else
                VERT if r.vie == 2 else
                JAUNE)
        
        pygame.draw.rect(ecran, color, [r.x+1, r.y+1, r.taille_x-2, r.taille_y-2])
        
    for b in balles:
        pygame.draw.rect(ecran, orange, [b.x, b.y, b.taille, b.taille])
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
