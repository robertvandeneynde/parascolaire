#!coding: utf-8
from __future__ import print_function, division
"""
Ce code montre que pour faire un jeu en 3D, une seule chose varie : le DESSIN
Ainsi un jeu purement 2D peut être affiché en 3D, comme ce casse brique.
Pour comparer la version 2D et la version 3D, regardez le code gl_brick_2D.py

On fait de la 3D grâce à OpenGL.
ATTENTION: Ce code utilise de la Vielle 3D (années 2000)
On parle d'OpenGL "version 2" ou de "fixed pipeline" ou "mode immédiat" ou "opengl sans shaders"
Il est vivement conseillé d'apprendre les shaders dès le début de votre apprentissage OpenGL
pour pouvoir faire de puissants effets modernes.
Il y a plein de fichier d'exemples pour les shaders sur le site.

Cependant, ce code est très utile pour comprendre les bases de la 3D et les matrices.
(Ou pour avoir vite fait un affichage)
"""

import pygame
import random

# importer la bibliothèque OpenGL !
from OpenGL.GL import *
from OpenGL.GL import shaders

import ctypes
import pygame
from math import sin, cos, degrees, radians, tan

import numpy
from numpy import array, linalg

vertex_shader = """
#version 330
in vec3 position;
in vec3 normal;

uniform mat4 pvMatrix;
uniform mat4 mMatrix;

out vec3 normalVtx;
out vec3 positionVtx;

void main()
{
    gl_Position = pvMatrix * mMatrix * vec4(position, 1);
    normalVtx = normal;
    positionVtx = (mMatrix * vec4(position, 1)).xyz;
}
"""

fragment_shader = """
#version 330
in vec3 normalVtx;
in vec3 positionVtx;

uniform vec3 lightPos;
uniform vec3 color;

out vec4 pixel;

void main()
{
    vec3 c = color * dot(normalVtx, normalize(lightPos - positionVtx));
    pixel = vec4(c, 1);
    //pixel = vec4((normalVtx+1)/2, 1);
    //pixel = vec4(((positionVtx/100)+1)/2, 1);
}
"""

def couleur01(r,g,b):
    return [r/255, g/255, b/255]

def couleur(s):
    if s in couleur.DATA:
        r,g,b = couleur.DATA[s]
        return couleur01(r,g,b)
    
    if s.startswith('#'):
        s = s[1:]
    
    if len(s) == 6: # "ffc030"
        r,g,b = s[0:2], s[2:4], s[4,6]
    elif len(s) == 3: # "fc9"
        r,g,b = s
        r,g,b = r * 2, g * 2, b * 2
    else:
        raise ValueError('string {} is not a color'.format(s))
    return couleur01(int(r, 16), int(g, 16), int(b, 16))

import os
couleur.DATA = {
    'yellow':     couleur01(255, 255, 0),  
    'honeydew':   couleur01(240, 255, 240),
    'magenta':    couleur01(255, 0,   255),
    'cornsilk':   couleur01(255, 248, 220),
    'peru':       couleur01(205, 133, 63), 
    'black':      couleur01(0,   0,   0),  
    'linen':      couleur01(250, 240, 230),
    'brown':      couleur01(165, 42,  42), 
    'cyan':       couleur01(0,   255, 255),
    'coral':      couleur01(255, 127, 80), 
    'orchid':     couleur01(218, 112, 214),
    'orange':     couleur01(255, 165, 0),  
    'aquamarine': couleur01(127, 255, 212),
    'white':      couleur01(255, 255, 255),
    'turquoise':  couleur01(64,  224, 208),
    'green':      couleur01(0,   255, 0),  
    'blue':       couleur01(0,   0,   255),
    'chocolate':  couleur01(210, 105, 30), 
    'lavender':   couleur01(230, 230, 250),
    'moccasin':   couleur01(255, 228, 181),
    'seashell':   couleur01(255, 245, 238),
    'khaki':      couleur01(240, 230, 140),
    'firebrick':  couleur01(178, 34,  34), 
    'maroon':     couleur01(176, 48,  96), 
    'tan':        couleur01(210, 180, 140),
    'gainsboro':  couleur01(220, 220, 220),
    'violet':     couleur01(238, 130, 238),
    'pink':       couleur01(255, 192, 203),
    'burlywood':  couleur01(222, 184, 135),
    'azure':      couleur01(240, 255, 255),
    'tomato':     couleur01(255, 99,  71), 
    'grey':       couleur01(190, 190, 190),
    'thistle':    couleur01(216, 191, 216),
    'gray':       couleur01(190, 190, 190),
    'gold':       couleur01(255, 215, 0),  
    'bisque':     couleur01(255, 228, 196),
    'beige':      couleur01(245, 245, 220),
    'wheat':      couleur01(245, 222, 179),
    'chartreuse': couleur01(127, 255, 0),  
    'red':        couleur01(255, 0,   0),  
    'snow':       couleur01(255, 250, 250),
    'ivory':      couleur01(255, 255, 240),
    'plum':       couleur01(221, 160, 221),
    'purple':     couleur01(160, 32,  240),
    'goldenrod':  couleur01(218, 165, 32), 
    'navy':       couleur01(0,   0,   128),
    'sienna':     couleur01(160, 82,  45), 
    'salmon':     couleur01(250, 128, 114),
}

def importColors(filename='colors.txt'):

    if os.path.isfile(filename):
        with open(filename) as f:
            for l in f:
                try:
                    l = l.split()
                    name = ' '.join(l[:-3])
                    r,b,g = l[-3:]
                    couleur.DATA[name] = int(r) / 255, int(g) / 255, int(b) / 255
                except:
                    pass
                
importColors()
                
def couleurHexNumber(x):
    return couleur01((x & 0xFF0000) >> 16, (x & 0xFF00) >> 8, x & 0xFF)

def couleurHexNumberAlpha(x):
    r,g,b,a = (x & 0xFF000000) >> 8*3, (x & 0xFF0000) >> 8*2, (x & 0xFF0000) >> 8*2, x & 0xFF
    return r / 255, g / 255, b / 255, a / 255

class Axe:
    pass


Axe.X = 0
Axe.Y = 1
Axe.Z = 2


def polar(*args):
    if len(args) == 2:
        r, t = args
    elif len(args) == 1:
        r, t = 1, args[0]
    else:
        raise TypeError('Accept 1 or 2 arguments')

    return r * vec2(cos(t), sin(t))


def polard(*args):
    if len(args) == 2:
        r, t = args
    elif len(args) == 1:
        r, t = 1, args[0]
    else:
        raise TypeError('Accept 1 or 2 arguments')

    return r * polar(radians(t))


def vec2(x, y):
    return array((x, y), dtype=numpy.float32)


def vec3(*args):
    '''
    returns a vector in 3 dimensions
    vec3(1,2,3)
    vec3((1,2),3)
    '''
    if len(args) == 3:
        x, y, z = args
    elif len(args) == 2:
        (x, y), z = args
    else:
        raise TypeError('Accept 2 or 3 arguments')

    return array((x, y, z), dtype=numpy.float32)


def normalized(v):
    return v / linalg.norm(v)


def PerspectiveMatrix(fovy, aspect, zNear, zFar):
    f = 1.0 / tan(radians(fovy) / 2.0)
    return array([
        [f / aspect, 0, 0, 0],
        [0, f, 0, 0],
        [0, 0, 1. * (zFar + zNear) / (zNear - zFar), 2.0 * zFar * zNear / (zNear - zFar)],
        [0, 0, -1, 0]
    ], dtype=numpy.float32)


def TranslationMatrix(*args):
    '''
    returns the TranslationMatrix
    TranslationMatrix(2,1,0)
    TranslationMatrix(2,1)
    TranslationMatrix((2,1,0))
    '''
    if len(args) == 3:
        tx, ty, tz = args
    elif len(args) == 2:
        (tx, ty), tz = args, 0
    elif len(args) == 1:
        tx, ty, tz = args[0]
    else:
        raise TypeError("Accept 1, 2 or 3 arguments")

    return array([
        [1, 0, 0, tx],
        [0, 1, 0, ty],
        [0, 0, 1, tz],
        [0, 0, 0, 1]
    ], dtype=numpy.float32)


def LookAtMatrix(*args):
    '''
    returns the LookAt matrix
    LookAtMatrix(1,2,3, 4,5,6, 7,8,9)
    LookAtMatrix((1,2,3), (4,5,6), (7,8,9))
    '''
    if len(args) == 3:
        e, c, up = args
    elif len(args) == 9:
        e, c, up = args[:3], args[3:6], args[6:]
    else:
        raise TypeError("Accept 3 or 9 arguments")
    c = array(c)

    f = normalized(c - e)
    s = normalized(numpy.cross(f, up))
    u = numpy.cross(s, f)

    return array([
        [s[0], s[1], s[2], -s.dot(e)],
        [u[0], u[1], u[2], -u.dot(e)],
        [-f[0], -f[1], -f[2], f.dot(e)],
        [0, 0, 0, 1],
    ], dtype=numpy.float32)
    
    # corresponds to M @ Translate(-e)


def SimpleRotationMatrix(angle, axe=Axe.Z):
    '''
    returns the rotation matrix for angle in degree around X Y or Z
    '''
    if angle % 90 == 0:
        x = angle % 360
        c = 1 if x == 0 else -1 if x == 180 else 0
        s = 1 if x == 90 else -1 if x == 270 else 0
    else:
        t = radians(angle)
        c = cos(t)
        s = sin(t)

    return array([
         [c, -s, 0, 0],
         [s, c, 0, 0],
         [0, 0, 1, 0],
         [0, 0, 0, 1]
     ] if axe == 2 else [
        [c, 0, s, 0],
        [0, 1, 0, 0],
        [-s, 0, c, 0],
        [0, 0, 0, 1]
    ] if axe == 1 else [
        [1, 0, 0, 0],
        [0, c, -s, 0],
        [0, s, c, 0],
        [0, 0, 0, 1]
    ], dtype=numpy.float32)


def GenericRotationMatrix(angle, axe):
    '''
    returns the rotation matrix for angle in degree around any axe
    '''
    x, y, z = normalized(axe)

    if angle % 90 == 0:
        x = angle % 360
        c = 1 if x == 0 else -1 if x == 180 else 0
        s = 1 if x == 90 else -1 if x == 270 else 0
    else:
        t = radians(angle)
        c = cos(t)
        s = sin(t)
    k = 1 - c

    # Rodriguez rotation formula
    return array([
        [x * x * k + c, x * y * k - z * s, x * z * k + y * s, 0],
        [y * x * k + z * s, y * y * k + c, y * z * k - x * s, 0],
        [x * z * k - y * s, y * z * k + x * s, z * z * k + c, 0],
        [0, 0, 0, 1]
    ], dtype=numpy.float32)


def ScaleMatrix(kx, ky=None, kz=None):
    if ky is None:
        ky = kx
    if kz is None:
        kz = kx
    return array([
        [kx, 0, 0, 0],
        [0, ky, 0, 0],
        [0, 0, kz, 0],
        [0, 0, 0, 1]
    ], dtype=numpy.float32)

def IdentityMatrix():
    return array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ], dtype=numpy.float32)

ROUGE = couleur01(255, 0, 0)
VERT = couleur01(0, 255, 0)
BLEU = couleur01(0, 0, 255)
JAUNE = couleur01(255, 255, 0)
BLANC = couleur01(255, 255, 255)
NOIR = couleur01(0, 0, 0)
ORANGE = couleur01(255, 153, 0)
BLEU_CLAIR = couleur01(135, 206, 250)

def nouvel_ecran(W, H):
    e = pygame.display.set_mode([W,H], pygame.DOUBLEBUF | pygame.OPENGL | pygame.RESIZABLE)
    
    glViewport(0, 0, W, H)
    glEnable(GL_DEPTH_TEST)

    return e

tx,ty = taille = [12*60, 500]

sol_points = array([
    0, 0, 0,
    tx, 0, 0,
    tx, ty, 0,
    0, ty, 0,
], dtype=numpy.float32)

sol_normals = array([0,0,1] * 4, dtype=numpy.float32)

"""
quads
from (0,0,0) to (1,1,1)
faces are ccw (counter clockwise : sens contraire des aiguilles d'une montre)
"""
cube_points = array([
    # up
    0, 0, 1,
    1, 0, 1,
    1, 1, 1,
    0, 1, 1,

    # down
    0, 0, 0,
    0, 1, 0,
    1, 1, 0,
    1, 0, 0,

    # right
    1, 0, 0,
    1, 1, 0,
    1, 1, 1,
    1, 0, 1,

    # left
    0, 0, 0,
    0, 0, 1,
    0, 1, 1,
    0, 1, 0,

    # back
    0, 1, 0,
    0, 1, 1,
    1, 1, 1,
    1, 1, 0,

    # front
    1, 0, 0,
    1, 0, 1,
    0, 0, 1,
    0, 0, 0,
], dtype=numpy.float32)

cube_normals = array(
    [0, 0, 1] * 4
    + [0, 0, -1] * 4
    + [1, 0, 0] * 4
    + [-1, 0, 0] * 4
    + [0, 1, 0] * 4
    + [0, -1, 0] * 4
    , dtype=numpy.float32)


def creer_vao_sol(shader):
    """
    renvoie le vao de nos objets :
    vertices:
    4 vtx : sol
    """
    vao = glGenVertexArrays(1)
    glBindVertexArray(vao)
    
    vbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vbo)
    glBufferData(GL_ARRAY_BUFFER, ArrayDatatype.arrayByteCount(sol_points), sol_points, GL_STATIC_DRAW)

    position = glGetAttribLocation(shader, 'position')
    if position != -1:
        glEnableVertexAttribArray(position)
        glVertexAttribPointer(position, 3, GL_FLOAT, False, 0, ctypes.c_void_p())
    else:
        print('inactive attribute "{}"'.format('position'))
    
    vbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vbo)
    glBufferData(GL_ARRAY_BUFFER, ArrayDatatype.arrayByteCount(sol_normals), sol_normals, GL_STATIC_DRAW)
    
    normal = glGetAttribLocation(shader, 'normal')
    if normal != -1:
        glEnableVertexAttribArray(normal)
        glVertexAttribPointer(normal, 3, GL_FLOAT, False, 0, ctypes.c_void_p())
    else:
        print('inactive attribute "{}"'.format('normal'))

    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glBindVertexArray(0)

    return vao

def creer_vao_cube(shader):
    vao = glGenVertexArrays(1)
    glBindVertexArray(vao)

    vbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vbo)
    glBufferData(GL_ARRAY_BUFFER, ArrayDatatype.arrayByteCount(cube_points), cube_points, GL_STATIC_DRAW)
    
    position = glGetAttribLocation(shader, 'position')
    if position != -1:
        glEnableVertexAttribArray(position)
        glVertexAttribPointer(position, 3, GL_FLOAT, False, 0, ctypes.c_void_p())
    else:
        print('inactive attribute "{}"'.format('position'))

    vbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vbo)
    glBufferData(GL_ARRAY_BUFFER, ArrayDatatype.arrayByteCount(cube_normals), cube_normals, GL_STATIC_DRAW)
    
    normal = glGetAttribLocation(shader, 'normal')
    if normal != -1:
        glEnableVertexAttribArray(normal)
        glVertexAttribPointer(normal, 3, GL_FLOAT, False, 0, ctypes.c_void_p())
    else:
        print('inactive attribute "{}"'.format('normal'))

    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glBindVertexArray(0)

    return vao

class Balle:
    pass

class Brique:
    pass

def creer_briques(briques):

    for i in range(12):
        for j in range(5):
            r = Brique()
            r.vie = 3
            r.taille_x = 60
            r.taille_y = 30
            r.x = i * r.taille_x
            r.y = j * r.taille_y
            briques.append(r)

def main():
    pygame.init()

    ecran = nouvel_ecran(tx, ty)

    clock = pygame.time.Clock()

    balles = []

    for i in range(5):
        b = Balle()
        b.taille = 20
        b.x = random.randrange(700 - b.taille)
        b.y = 300 + random.randrange(200)
        b.sx = random.choice([-1,1])
        b.sy = random.choice([-1,1])
        balles.append(b)

    briques = []

    creer_briques(briques)

    shader = shaders.compileProgram(
        shaders.compileShader(vertex_shader, GL_VERTEX_SHADER),
        shaders.compileShader(fragment_shader, GL_FRAGMENT_SHADER)
    )

    vao_sol = creer_vao_sol(shader)
    vao_cube = creer_vao_cube(shader)

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
            creer_briques(briques)
        t += 1

        # dessin
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glUseProgram(shader)

        P = PerspectiveMatrix(45, 1.0 * tx / ty, 100, 2000) # fov 45°, ratio tx / ty, distance min : 100, distance max : 2000

        # position et orientation de la camera :
        camera_x = tx/2 # au milieu de l'arène
        camera_y = -ty # derrière l'arène
        camera_z = 700 # bien haut

        cible_camera_x, cible_camera_y = tx / 2, ty / 2 # regarde le milieu de l'arène
        cible_camera_z = 0 # regarde par terre
        
        V = LookAtMatrix(camera_x, camera_y, camera_z, cible_camera_x, cible_camera_y, cible_camera_z, 0,0,1)

        # position de la lampe :
        light_x, light_y = tx / 2, ty / 2 # lampe au milieu de l'arène
        light_z = 150 # un peu au dessus des briques (hauteur : 100)
        glUniform3f(glGetUniformLocation(shader, 'lightPos'), light_x, light_y, light_z)

        PV = P.dot(V)
        # dessin du sol
        glBindVertexArray(vao_sol)

        glUniformMatrix4fv(glGetUniformLocation(shader, 'pvMatrix'), 1, True, PV)
        glUniformMatrix4fv(glGetUniformLocation(shader, 'mMatrix'), 1, True, IdentityMatrix())
        glUniform3fv(glGetUniformLocation(shader, 'color'), 1, BLEU_CLAIR)

        glDrawArrays(GL_QUADS, 0, 4)

        glBindVertexArray(0)

        # dessin des 4 côtés
        glBindVertexArray(vao_cube)

        glUniform3fv(glGetUniformLocation(shader, 'color'), 1, (0.8, 0.8, 0.8))

        M = TranslationMatrix(0, -50, 0).dot(ScaleMatrix(tx, 50, 50))
        glUniformMatrix4fv(glGetUniformLocation(shader, 'pvMatrix'), 1, True, PV)
        glUniformMatrix4fv(glGetUniformLocation(shader, 'mMatrix'), 1, True, M)
        glDrawArrays(GL_QUADS, 0, 24)

        M = TranslationMatrix(0, ty, 0).dot(ScaleMatrix(tx, 50, 50))
        glUniformMatrix4fv(glGetUniformLocation(shader, 'pvMatrix'), 1, True, PV)
        glUniformMatrix4fv(glGetUniformLocation(shader, 'mMatrix'), 1, True, M)
        glDrawArrays(GL_QUADS, 0, 24)

        M = TranslationMatrix(-50, 0, 0).dot(ScaleMatrix(50, ty, 50))
        glUniformMatrix4fv(glGetUniformLocation(shader, 'pvMatrix'), 1, True, PV)
        glUniformMatrix4fv(glGetUniformLocation(shader, 'mMatrix'), 1, True, M)
        glDrawArrays(GL_QUADS, 0, 24)
        
        M = TranslationMatrix(tx, 0, 0).dot(ScaleMatrix(50, ty, 50))
        glUniformMatrix4fv(glGetUniformLocation(shader, 'pvMatrix'), 1, True, PV)
        glUniformMatrix4fv(glGetUniformLocation(shader, 'mMatrix'), 1, True, M)
        glDrawArrays(GL_QUADS, 0, 24)

        # dessin des briques
        for r in briques:
            color = (ROUGE if r.vie == 3 else
                     VERT if r.vie == 2 else
                     JAUNE)

            glUniform3fv(glGetUniformLocation(shader, 'color'), 1, color)
        
            d = 5
            T = TranslationMatrix(r.x + d, ty - (r.y + d) - (r.taille_y - 2*d), 0)
            S = ScaleMatrix(r.taille_x - 2*d, r.taille_y - 2*d, 100)
            glUniformMatrix4fv(glGetUniformLocation(shader, 'pvMatrix'), 1, True, PV)
            glUniformMatrix4fv(glGetUniformLocation(shader, 'mMatrix'), 1, True, T.dot(S))
            glDrawArrays(GL_QUADS, 0, 24)
        
        # dessin des balles
        glUniform3fv(glGetUniformLocation(shader, 'color'), 1, ORANGE)
        for b in balles:
            T = TranslationMatrix(b.x, ty - b.y - b.taille, 0)
            S = ScaleMatrix(b.taille, b.taille, b.taille)
            glUniformMatrix4fv(glGetUniformLocation(shader, 'pvMatrix'), 1, True, PV)
            glUniformMatrix4fv(glGetUniformLocation(shader, 'mMatrix'), 1, True, T.dot(S))
            glDrawArrays(GL_QUADS, 0, 24)

        glUseProgram(0)
        # dessin du repère en (0,0,100) (sans lighting)
        
        """

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
        """

        # appliquer les dessins
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
