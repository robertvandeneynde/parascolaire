#!coding: utf-8
"""
Ce code montre que pour faire un jeu en 3D, une seule chose varie : le DESSIN
Ainsi un jeu purement 2D peut être affiché en 3D, comme ce casse brique.
Pour comparer la version 2D et la version 3D, regardez le code gl_brick_2D.py

On fait de la 3D grâce à OpenGL.
ATTENTION: Ce code utilise de la Vieille 3D (années 2000)
On parle d'OpenGL "version 2" ou de "fixed pipeline" ou "mode immédiat" ou "opengl sans shaders"
Il est vivement conseillé d'apprendre les shaders dès le début de votre apprentissage OpenGL
pour pouvoir faire de puissants effets modernes.
Il y a plein de fichier d'exemples pour les shaders sur le site.
Un très bon tutoriel d'opengl moderne (OpenGL 3 / OpenGL avec shaders) est :
learnopengl.com

Cependant, ce code est très utile pour comprendre les bases de la 3D et les matrices.
(Ou pour avoir vite fait un affichage)
"""
from __future__ import print_function, division

import pygame
import random

# importer la bibliothèque OpenGL !
from OpenGL.GL import *
from OpenGL.GLU import *

import sys
pygame.init()

def nouvel_ecran(W,H):
    e = pygame.display.set_mode([W,H], pygame.DOUBLEBUF | pygame.OPENGL | pygame.RESIZABLE)
    
    glViewport(0, 0, W, H)
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

tx,ty = taille = [12*60, 500]
ecran = nouvel_ecran(tx, ty)

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

def creer_briques():

    for i in range(12):
        for j in range(5):
            r = Brique()
            r.vie = 3
            r.taille_x = 60
            r.taille_y = 30
            r.x = i * r.taille_x
            r.y = j * r.taille_y
            briques.append(r)

creer_briques()

def draw_cube():
    """
    from (0,0,0) to (1,1,1)
    faces are ccw (counter clockwise : sens contraire des aiguilles d'une montre)
    """
    glBegin(GL_TRIANGLES) # GL_QUADS is deprecated
    
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
    
    glEnd()

t = 0

fini = 0
while fini == 0:
    # pour tous les événements qui se sont passsés depuis la dernière fois
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # si l'event est de type QUIT
            fini = 1 # on met fini à 1, ce qui va quitter la boucle à la fin de ce tick
        elif event.type == pygame.VIDEORESIZE:
            # on s'adapte à la nouvelle fenêtre
            ecran = nouvel_ecran(event.w, event.h) # re créer l'écran !
    
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
    
    if len(briques) == 0:
        creer_briques()
    
    t += 1
    
    # dessin
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 1.0 * tx / ty, 100, 2000) # fov 45°, ratio tx / ty, distance min : 100, distance max : 2000
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    # position et orientation de la camera :
    camera_x = tx/2 # au milieu de l'arène
    camera_y = -ty # derrière l'arène 
    camera_z = 700 # bien haut
    
    cible_camera_x, cible_camera_y = tx / 2, ty / 2 # regarde le milieu de l'arène
    cible_camera_z = 0 # regarde par terre
    
    gluLookAt(camera_x, camera_y, camera_z, cible_camera_x, cible_camera_y, cible_camera_z, 0,0,1)
    
    # position de la lampe :
    light_x, light_y = tx / 2, ty / 2 # lampe au milieu de l'arène
    light_z = 150 # un peu au dessus des briques (hauteur : 100)
    glLight(GL_LIGHT0, GL_POSITION,  [light_x, light_y, light_z, 1])
    
    # dessin du sol
    glColor3ubv(BLEU_CLAIR) # 3ubv signifie que l'on indique la couleur avec une liste de 3 int de 0 à 255
    glBegin(GL_TRIANGLES) # GL_QUADS is deprecated
    glNormal3f(0, 0, 1)
    glVertex3f(0, 0, 0)
    glVertex3f(tx, 0, 0)
    glVertex3f(0, ty, 0)
    glVertex3f(tx, 0, 0)
    glVertex3f(tx, ty, 0)
    glVertex3f(0, ty, 0)
    glEnd()
    
    # dessin des 4 côtés
    glColor3f(0.8, 0.8, 0.8) # 3f signifie que l'on indique la couleur avec 3 float (nombres réels / à virgule) entre 0 et 1
    
    glPushMatrix()
    glTranslatef(0, -50, 0)
    glScalef(tx, 50, 50)
    draw_cube()
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(0, ty, 0)
    glScalef(tx,50,50)
    draw_cube()
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(-50, 0, 0)
    glScalef(50, ty, 50)
    draw_cube()
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(tx, 0, 0)
    glScalef(50, ty, 50)
    draw_cube()
    glPopMatrix()
    
    # dessin des briques
    for r in briques:
        color = (ROUGE if r.vie == 3 else
                 VERT if r.vie == 2 else
                 JAUNE)
        
        glColor3ubv(color)
        
        glPushMatrix()
        d = 5
        glTranslatef(r.x + d, ty - (r.y + d) - (r.taille_y - 2*d), 0)
        glScalef(r.taille_x - 2*d, r.taille_y - 2*d, 100)
        draw_cube()
        
        glPopMatrix()
    
    # dessin des balles
    glColor3ubv(ORANGE)
    for b in balles:
        glPushMatrix()
        glTranslatef(b.x, ty - b.y - b.taille, 0)
        glScalef(b.taille, b.taille, b.taille)
        draw_cube()
        glPopMatrix()
    
    # dessin du repère en (0,0,100) (sans lighting)
    
    glDisable(GL_LIGHTING)
    glPushMatrix()
    glTranslatef(0,0,100)
    glScalef(50,50,50)
    
    glBegin(GL_LINES)
    glColor3ubv(ROUGE)
    glVertex3f(0, 0, 0)
    glVertex3f(1, 0, 0)
    glColor3ubv(VERT)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 1, 0)
    glColor3ubv(BLEU)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 0, 1)
    glEnd()
    
    glPointSize(5)
    
    glBegin(GL_POINTS)
    glColor3ubv(ROUGE)
    glVertex3f(1, 0, 0)
    glColor3ubv(VERT)
    glVertex3f(0, 1, 0)
    glColor3ubv(BLEU)
    glVertex3f(0, 0, 1)
    glEnd()
        
    glEnable(GL_LIGHTING)
    glPopMatrix()
    
    # appliquer les dessins
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
