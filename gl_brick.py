#!coding: utf-8

import pygame
import random

IN_3D = True # Mettre à False si vous voulez voir l'affichage 2D

if IN_3D:
    from OpenGL.GL import *
    from OpenGL.GLU import *

pygame.init()

taille = [12*60, 500]
if IN_3D:
    ecran = pygame.display.set_mode(taille, pygame.DOUBLEBUF | pygame.OPENGL | pygame.RESIZABLE)
else:
    ecran = pygame.display.set_mode(taille, pygame.DOUBLEBUF)

clock = pygame.time.Clock()

rouge = [255,0,0]
vert = [0,255,0]
bleu = [0,0,255]
jaune = [255,255,0]
blanc = [255,255,255]
noir = [0, 0, 0]
orange = [255, 153, 0]
bleu_clair = [135, 206, 250]

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

if IN_3D:
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
    
def draw_cube():
    '''
    from (0,0,0) to (1,1,1)
    faces are ccw (counter clockwise : sens contraire des aiguilles d'une montre)
    '''
    glBegin(GL_QUADS);
    
    glNormal3f(0, 0, 1); # up
    glVertex3f(0, 0, 1);
    glVertex3f(1, 0, 1);
    glVertex3f(1, 1, 1);
    glVertex3f(0, 1, 1); 
    
    glNormal3f(0, 0, -1); # down  
    glVertex3f(0, 0, 0);
    glVertex3f(0, 1, 0);
    glVertex3f(1, 1, 0);
    glVertex3f(1, 0, 0);
    
    glNormal3f(1, 0, 0); # right
    glVertex3f(1, 0, 0);
    glVertex3f(1, 1, 0);
    glVertex3f(1, 1, 1);
    glVertex3f(1, 0, 1);
    
    glNormal3f(-1, 0, 0); # left
    glVertex3f(0, 0, 0);
    glVertex3f(0, 0, 1);
    glVertex3f(0, 1, 1);
    glVertex3f(0, 1, 0);
    
    glNormal3f(0, 1, 0); # back
    glVertex3f(0, 1, 0);
    glVertex3f(0, 1, 1);
    glVertex3f(1, 1, 1);
    glVertex3f(1, 1, 0);
    
    glNormal3f(0, -1, 0); # front
    glVertex3f(1, 0, 0);
    glVertex3f(1, 0, 1);
    glVertex3f(0, 0, 1);
    glVertex3f(0, 0, 0);
    
    glEnd();

t = 0

fini = 0
while fini == 0:
    # pour tous les événements qui se sont passsés depuis la dernière fois
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # si l'event est de type QUIT
            fini = 1 # on met fini à 1, ce qui va quitter la boucle à la fin de ce tick
        elif event.type == pygame.VIDEORESIZE:
            if IN_3D:
                ecran = pygame.display.set_mode(event.size, pygame.DOUBLEBUF | pygame.OPENGL | pygame.RESIZABLE)
                glViewport(0, 0, event.w, event.h)
    
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
    if IN_3D:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        glMatrixMode(GL_PROJECTION)
        gluPerspective(45, 1.0 * taille[0] / taille[1], 1, 2000)
        
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(taille[0]/2, -taille[1], 700, taille[0]/2,taille[1]/2,0, 0,0,1)
        glLight(GL_LIGHT0, GL_POSITION,  (taille[0]/2, taille[1]/2, 500, 1))
        
        # dessin du sol
        glColor3ubv(bleu_clair) # 3ubv signifie que l'on indique la couleur avec une liste de 3 int de 0 à 255
        glPushMatrix()
        glBegin(GL_QUADS)
        glNormal3f(0,0,1)
        glVertex3f(0,0,0)
        glVertex3f(taille[0],0,0)
        glVertex3f(taille[0],taille[1],0)
        glVertex3f(0,taille[1],0)
        glEnd()
        glPopMatrix()
        
        # dessin des 4 côtés
        glColor3f(0.8,0.8,0.8) # 3f signifie que l'on indique la couleur avec 3 float entre 0 et 1
        
        glPushMatrix()
        glTranslatef(0,-50,0)
        glScalef(taille[0],50,50)
        draw_cube()
        glPopMatrix()
        
        glPushMatrix()
        glTranslatef(0,taille[1],0)
        glScalef(taille[0],50,50)
        draw_cube()
        glPopMatrix()
        
        glPushMatrix()
        glTranslatef(-50,0,0)
        glScalef(50,taille[1],50)
        draw_cube()
        glPopMatrix()
        
        glPushMatrix()
        glTranslatef(taille[0],0,0)
        glScalef(50,taille[1],50)
        draw_cube()
        glPopMatrix()
        
        # dessin des briques
        for r in briques:
            color = (rouge if r.vie == 3 else
                     vert if r.vie == 2 else
                     jaune)
            
            glColor3ubv(color)
            
            glPushMatrix()
            d = 5
            glTranslatef(r.x + d, taille[1] - (r.y + d) - (r.taille_y - 2*d), 0)
            glScalef(r.taille_x - 2*d, r.taille_y - 2*d, 100)
            draw_cube()
            
            glPopMatrix()
        
        # dessin des balles
        glColor3ubv(orange)
        for b in balles:
            
            glPushMatrix()
            glTranslatef(b.x, taille[1] - b.y - b.taille, 0)
            glScalef(b.taille, b.taille, b.taille)
            draw_cube()
            glPopMatrix()
        
        # dessin du repère en (0,0,100)
        
        glPushMatrix()
        glTranslatef(0,0,100)
        glScalef(50,50,50)
        
        glDisable(GL_LIGHTING)
        
        glBegin(GL_LINES)
        glColor3ubv(rouge)
        glVertex3f(0,0,0)
        glVertex3f(1,0,0)
        glColor3ubv(vert)
        glVertex3f(0,0,0)
        glVertex3f(0,1,0)
        glColor3ubv(bleu)
        glVertex3f(0,0,0)
        glVertex3f(0,0,1)
        glEnd()
        
        glPointSize(5)
        
        glBegin(GL_POINTS)
        glColor3ubv(rouge)
        glVertex3f(1,0,0)
        glColor3ubv(vert)
        glVertex3f(0,1,0)
        glColor3ubv(bleu)
        glVertex3f(0,0,1)
        glEnd()
            
        glEnable(GL_LIGHTING)
        glPopMatrix()
        
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        
    else: # 2D
        ecran.fill(bleu_clair)
    
        for r in briques:
            
            color = (rouge if r.vie == 3 else
                    vert if r.vie == 2 else
                    jaune)
            
            pygame.draw.rect(ecran, color, [r.x+1, r.y+1, r.taille_x-2, r.taille_y-2])
            
        for b in balles:
            pygame.draw.rect(ecran, orange, [b.x, b.y, b.taille, b.taille])
        
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
