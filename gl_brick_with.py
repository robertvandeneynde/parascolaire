#!coding: utf-8
"""
Ce code est une légère simplification pythonique du code gl_brick.py
En utilisant la structure "with"

with permet de mettre en évidence un code qui fait une action "au début"
et une action "à la fin"

un glPushMatrix() va quasi toujours se finir par un glEndMatrix()
, avec le with, on dit simple :
"le code qui suit commence par un push et finit par un pop"

Et ce quoiqu'il arrive (une exception est lancée, voir chapitre sur les exceptions)
"""
from __future__ import print_function, division

import pygame
import random

# importer la bibliothèque OpenGL !
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()

class PushPop:
    def __enter__(self):
        glPushMatrix() # quand on entre : push
    def __exit__(self, a,b,c):
        glPopMatrix() # quand on sort : push

class BeginEnd:
    def __init__(self, mode):
        self.mode = mode
    def __enter__(self):
        glBegin(self.mode)
    def __exit__(self, a,b,c):
        glEnd()

def nouvel_ecran():
    e = pygame.display.set_mode(taille, pygame.DOUBLEBUF | pygame.OPENGL | pygame.RESIZABLE)
    
    glViewport(0, 0, taille[0], taille[1])
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_NORMALIZE)
    glShadeModel(GL_SMOOTH)
    glLight(GL_LIGHT0, GL_AMBIENT,  (0,0,0,1))
    glLight(GL_LIGHT0, GL_DIFFUSE,  (1,1,1,1))
    glLight(GL_LIGHT0, GL_SPECULAR,  (1,1,1,1))
        
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    
    return e

taille = [12*60, 500]
ecran = nouvel_ecran()

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

def draw_cube():
    '''
    from (0,0,0) to (1,1,1)
    faces are ccw (counter clockwise : sens contraire des aiguilles d'une montre)
    '''
    with BeginEnd(GL_TRIANGLES): # GL_QUADS is deprecated
    
        glNormal3f(0, 0, 1) # up
        glVertex3f(0, 0, 1)
        glVertex3f(1, 0, 1)
        glVertex3f(0, 1, 1) 
        glVertex3f(1, 0, 1)
        glVertex3f(1, 1, 1)
        glVertex3f(0, 1, 1) 
        
        glNormal3f(0, 0, -1) # down  
        glVertex3f(0, 0, 0)
        glVertex3f(0, 1, 0)
        glVertex3f(1, 0, 0)
        glVertex3f(0, 1, 0)
        glVertex3f(1, 1, 0)
        glVertex3f(1, 0, 0)
        
        glNormal3f(1, 0, 0) # right
        glVertex3f(1, 0, 0)
        glVertex3f(1, 1, 0)
        glVertex3f(1, 0, 1)
        glVertex3f(1, 1, 0)
        glVertex3f(1, 1, 1)
        glVertex3f(1, 0, 1)
        
        glNormal3f(-1, 0, 0) # left
        glVertex3f(0, 0, 0)
        glVertex3f(0, 0, 1)
        glVertex3f(0, 1, 0)
        glVertex3f(0, 0, 1)
        glVertex3f(0, 1, 1)
        glVertex3f(0, 1, 0)
        
        glNormal3f(0, 1, 0) # back
        glVertex3f(0, 1, 0)
        glVertex3f(0, 1, 1)
        glVertex3f(1, 1, 0)
        glVertex3f(0, 1, 1)
        glVertex3f(1, 1, 1)
        glVertex3f(1, 1, 0)
        
        glNormal3f(0, -1, 0) # front
        glVertex3f(1, 0, 0)
        glVertex3f(1, 0, 1)
        glVertex3f(0, 0, 0)
        glVertex3f(1, 0, 1)
        glVertex3f(0, 0, 1)
        glVertex3f(0, 0, 0)

t = 0

fini = 0
while fini == 0:
    # pour tous les événements qui se sont passsés depuis la dernière fois
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # si l'event est de type QUIT
            fini = 1 # on met fini à 1, ce qui va quitter la boucle à la fin de ce tick
        elif event.type == pygame.VIDEORESIZE:
            # on s'adapte à la nouvelle fenêtre
            taille = [event.w, event.h]
            ecran = nouvel_ecran() # re créer l'écran !
    
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
        
        if b.x > taille[0] - b.taille:
            b.sx = -1
        if b.x < 0:
            b.sx = 1
        if b.y > taille[1] - b.taille:
            b.sy = -1
        if b.y < 0:
            b.sy = 1
        
    t += 1
    
    # dessin
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 1.0 * taille[0] / taille[1], 100, 2000) # fov 45°, ratio taille[0] / taille[1], distance min : 100, distance max : 2000
    
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    # position et orientation de la camera :
    camera_x = taille[0]/2 # au milieu de l'arène
    camera_y = -taille[1] # derrière l'arène 
    camera_z = 700 # bien haut
    
    cible_camera_x, cible_camera_y = taille[0]/2, taille[1]/2 # regarde le milieu de l'arène
    cible_camera_z = 0 # regarde par terre
    
    gluLookAt(camera_x, camera_y, camera_z, cible_camera_x, cible_camera_y, cible_camera_z, 0,0,1)
    
    # position de la lampe :
    light_x, light_y = taille[0] / 2, taille[1] / 2 # au milieu de l'arène
    light_z = 150 # un peu au dessus des briques (de taille 100)
    glLight(GL_LIGHT0, GL_POSITION,  [light_x, light_y, light_z, 1])
    
    # dessin du sol
    glColor3ubv(BLEU_CLAIR) # 3ubv signifie que l'on indique la couleur avec une liste de 3 int de 0 à 255
    with BeginEnd(GL_TRIANGLES): # GL_QUADS is deprecated
        glNormal3f(0, 0, 1)
        glVertex3f(0, 0, 0)
        glVertex3f(taille[0], 0, 0)
        glVertex3f(taille[0], taille[1], 0)
        glVertex3f(0, taille[1], 0)

    # dessin des 4 côtés
    glColor3f(0.8, 0.8, 0.8) # 3f signifie que l'on indique la couleur avec 3 float (nombres réels / à virgule) entre 0 et 1
    
    with PushPop():
        glTranslatef(0, -50, 0)
        glScalef(taille[0], 50, 50)
        draw_cube()
    
    with PushPop():
        glTranslatef(0, taille[1], 0)
        glScalef(taille[0],50,50)
        draw_cube()
    
    with PushPop():
        glTranslatef(-50, 0, 0)
        glScalef(50, taille[1], 50)
        draw_cube()
    
    with PushPop():
        glTranslatef(taille[0], 0, 0)
        glScalef(50, taille[1], 50)
        draw_cube()
    
    # dessin des briques
    for r in briques:
        color = (ROUGE if r.vie == 3 else
                 VERT if r.vie == 2 else
                 JAUNE)
        
        glColor3ubv(color)
        
        with PushPop():
            d = 5
            glTranslatef(r.x + d, taille[1] - (r.y + d) - (r.taille_y - 2*d), 0)
            glScalef(r.taille_x - 2*d, r.taille_y - 2*d, 100)
            draw_cube()
    
    # dessin des balles
    glColor3ubv(ORANGE)
    for b in balles:
        with PushPop():
            glTranslatef(b.x, taille[1] - b.y - b.taille, 0)
            glScalef(b.taille, b.taille, b.taille)
            draw_cube()
    
    # dessin du repère en (0,0,100) (sans lighting)
    
    glDisable(GL_LIGHTING)
    with PushPop():
        glTranslatef(0,0,100)
        glScalef(50,50,50)
        
        with BeginEnd(GL_LINES):
            glColor3ubv(ROUGE)
            glVertex3f(0, 0, 0)
            glVertex3f(1, 0, 0)
            glColor3ubv(VERT)
            glVertex3f(0, 0, 0)
            glVertex3f(0, 1, 0)
            glColor3ubv(BLEU)
            glVertex3f(0, 0, 0)
            glVertex3f(0, 0, 1)
        
        glPointSize(5)
        
        with BeginEnd(GL_POINTS):
            glColor3ubv(ROUGE)
            glVertex3f(1, 0, 0)
            glColor3ubv(VERT)
            glVertex3f(0, 1, 0)
            glColor3ubv(BLEU)
            glVertex3f(0, 0, 1)
            
    glEnable(GL_LIGHTING)
    
    # appliquer les dessins
        
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

