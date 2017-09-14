#!coding: utf-8
from __future__ import print_function, division

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

###########
# glutils #
###########

def farray(x):
    return numpy.array(x, numpy.float32)

def cosd(x):
    return cos(radians(x))

def sind(x):
    return sin(radians(x))

def vec2(x, y):
    """ Create vector in 2 dimensions of correct type (numpy float32)
    >>> vec2(4,5)
    array([4.0, 5.0], dtype=float32)
    """
    return farray((x, y))

def vec3(*args):
    """ Create vector in 3 dimensions of correct type (numpy float32)
    >>> vec3(1,2,3)
    array([1.0, 2.0, 3.0], dtype=float32)
    >>> vec3((1,2),3)
    array([1.0, 2.0, 3.0], dtype=float32)
    """
    if len(args) == 3:
        x, y, z = args
    elif len(args) == 2:
        (x, y), z = args
    else:
        raise TypeError('Accept 2 or 3 arguments')

    return farray((x, y, z))


def polar(*args):
    """ Polar coordinate in radians
    >>> polar(pi/3)
    array([0.5, 0.8660254])
    >>> polar(10, pi/3)
    array([5.0, 8.66025404])
    """
    if len(args) == 2:
        r, t = args
    elif len(args) == 1:
        r, t = 1, args[0]
    else:
        raise TypeError('Accept 1 or 2 arguments')

    return r * vec2(cos(t), sin(t))


def polard(*args):
    """ Polar coordinate in degrees
    >>> polard(60)
    array([0.5, 0.8660254])
    >>> polar(10, 60)
    array([5.0, 8.66025404])
    """
    if len(args) == 2:
        r, t = args
    elif len(args) == 1:
        r, t = 1, args[0]
    else:
        raise TypeError('Accept 1 or 2 arguments')

    return r * polar(radians(t))

def normalized(v):
    return v / linalg.norm(v)


def PerspectiveMatrix(fovy, aspect, zNear, zFar):
    """ PerspectiveMatrix
    PerspectiveMatrix(45, 16/9.0, 100, 2000)
    """
    f = 1.0 / tan(radians(fovy) / 2.0)
    return farray([
        [f / aspect, 0, 0, 0],
        [0, f, 0, 0],
        [0, 0, 1. * (zFar + zNear) / (zNear - zFar), 2.0 * zFar * zNear / (zNear - zFar)],
        [0, 0, -1, 0]
    ])

def LookAtMatrix(eye, target, up, *others):
    """ LookAt: I am in "eye" I look at "target" and the up is "up"
    LookAtMatrix(1,2,3, 4,5,6, 7,8,9)
    LookAtMatrix((1,2,3), (4,5,6), (7,8,9))
    """
    if len(others) == 0:
        pass
    elif len(others) == 6:
        eye, target, up = (eye, target, up), others[:3], others[3:]
    else:
        raise TypeError("Accept 3 or 9 arguments")
    target = array(target)

    f = normalized(target - eye)
    s = normalized(numpy.cross(f, up))
    u = numpy.cross(s, f)

    return farray([
        [s[0], s[1], s[2], -s.dot(eye)],
        [u[0], u[1], u[2], -u.dot(eye)],
        [-f[0], -f[1], -f[2], f.dot(eye)],
        [0, 0, 0, 1],
    ]) # corresponds to M(s, u, -f).to4x4 @ Translate(-eye)


def TranslationMatrix(*args):
    """ TranslationMatrix
    TranslationMatrix(2,1,0)
    TranslationMatrix(2,1)
    TranslationMatrix((2,1,0))
    """
    if len(args) == 3:
        tx, ty, tz = args
    elif len(args) == 2:
        (tx, ty), tz = args, 0
    elif len(args) == 1:
        tx, ty, tz = args[0]
    else:
        raise TypeError("Accept 1, 2 or 3 arguments")

    return farray([
        [1, 0, 0, tx],
        [0, 1, 0, ty],
        [0, 0, 1, tz],
        [0, 0, 0, 1]
    ])


class Axe:
    X = 0
    Y = 1
    Z = 2

def SimpleRotationMatrix(angle, axe=Axe.Z):
    """ Rotation matrix for angle in degree around X Y or Z
    SimpleRotationMatrix(30, Axe.Z)
    """
    if angle % 90 == 0:
        a = angle % 360
        c = 1 if a == 0 else -1 if a == 180 else 0
        s = 1 if a == 90 else -1 if a == 270 else 0
    else:
        t = radians(angle)
        c = cos(t)
        s = sin(t)

    return farray([
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
    ])


def GenericRotationMatrix(angle, axe):
    """ Rotation matrix for angle in degree around any axe
    GenericRotationMatrix(30, (0,0,1))
    """
    x, y, z = normalized(axe)

    if angle % 90 == 0:
        a = angle % 360
        c = 1 if a == 0 else -1 if a == 180 else 0
        s = 1 if a == 90 else -1 if a == 270 else 0
    else:
        t = radians(angle)
        c = cos(t)
        s = sin(t)

    k = 1 - c

    # Rodriguez rotation formula
    return farray([
        [x * x * k + c, x * y * k - z * s, x * z * k + y * s, 0],
        [y * x * k + z * s, y * y * k + c, y * z * k - x * s, 0],
        [x * z * k - y * s, y * z * k + x * s, z * z * k + c, 0],
        [0, 0, 0, 1]
    ])


def ScaleMatrix(kx, ky=None, kz=None):
    """ ScaleMatrix
    ScaleMatrix(2) = ScaleMatrix(2,2,2)
    ScaleMatrix(1,2,3)
    """
    if ky is None:
        ky = kx
    if kz is None:
        kz = kx
    return farray([
        [kx, 0, 0, 0],
        [0, ky, 0, 0],
        [0, 0, kz, 0],
        [0, 0, 0, 1]
    ])

def IdentityMatrix():
    """ IdentityMatrix
    IdentityMatrix()
    """
    return farray([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

###############
# END glutils #
###############

def couleur01(r,g,b):
    return [r/255, g/255, b/255]

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

sol_points = farray([
    0, 0, 0,
    tx, 0, 0,
    0, ty, 0,
    tx, 0, 0,
    tx, ty, 0,
    0, ty, 0,
])

sol_normals = farray([0,0,1] * 6)

"""
triangles (quads are deprecated)
from (0,0,0) to (1,1,1)
faces are ccw (counter clockwise : sens contraire des aiguilles d'une montre)
"""
cube_points = farray([
    # up
    0, 0, 1,
    1, 0, 1,
    0, 1, 1,
    1, 0, 1,
    1, 1, 1,
    0, 1, 1,

    # down
    0, 0, 0,
    0, 1, 0,
    1, 0, 0,
    0, 1, 0,
    1, 1, 0,
    1, 0, 0,

    # right
    1, 0, 0,
    1, 1, 0,
    1, 0, 1,
    1, 1, 0,
    1, 1, 1,
    1, 0, 1,

    # left
    0, 0, 0,
    0, 0, 1,
    0, 1, 0,
    0, 0, 1,
    0, 1, 1,
    0, 1, 0,

    # back
    0, 1, 0,
    0, 1, 1,
    1, 1, 0,
    0, 1, 1,
    1, 1, 1,
    1, 1, 0,

    # front
    1, 0, 0,
    1, 0, 1,
    0, 0, 0,
    1, 0, 1,
    0, 0, 1,
    0, 0, 0,
])

cube_normals = farray(
    [0, 0, 1] * 6
    + [0, 0, -1] * 6
    + [1, 0, 0] * 6
    + [-1, 0, 0] * 6
    + [0, 1, 0] * 6
    + [0, -1, 0] * 6)


def creer_vao_sol(shader):
    """
    renvoie le vao de nos objets :
    vertices:
    4 vtx : sol
    """
    vao = glGenVertexArrays(1)
    glBindVertexArray(vao)
    
    position = glGetAttribLocation(shader, 'position')
    if position != -1:
        vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, vbo)
        glBufferData(GL_ARRAY_BUFFER, ArrayDatatype.arrayByteCount(sol_points), sol_points, GL_STATIC_DRAW)

        glEnableVertexAttribArray(position)
        glVertexAttribPointer(position, 3, GL_FLOAT, False, 0, ctypes.c_void_p())
    else:
        print('Inactive attribute "{}"'.format('position'))
    
    normal = glGetAttribLocation(shader, 'normal')
    if normal != -1:
        vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, vbo)
        glBufferData(GL_ARRAY_BUFFER, ArrayDatatype.arrayByteCount(sol_normals), sol_normals, GL_STATIC_DRAW)
    
        glEnableVertexAttribArray(normal)
        glVertexAttribPointer(normal, 3, GL_FLOAT, False, 0, ctypes.c_void_p())
    else:
        print('Inactive attribute "{}"'.format('normal'))

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
        shaders.compileShader(fragment_shader, GL_FRAGMENT_SHADER))

    vao_sol = creer_vao_sol(shader)
    vao_cube = creer_vao_cube(shader)

    t = 0

    fini = 0
    while fini == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fini = 1
            elif event.type == pygame.VIDEORESIZE: # la fenêtre a été redimensionnée
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

        P = PerspectiveMatrix(45, tx / ty, 100, 2000) # fov 45°, ratio tx / ty, distance min : 100, distance max : 2000

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

        PV = P @ V # P.dot(V) si Python < 3.5
        # dessin du sol
        glBindVertexArray(vao_sol)

        glUniformMatrix4fv(glGetUniformLocation(shader, 'pvMatrix'), 1, True, PV)
        glUniformMatrix4fv(glGetUniformLocation(shader, 'mMatrix'), 1, True, IdentityMatrix())
        glUniform3fv(glGetUniformLocation(shader, 'color'), 1, BLEU_CLAIR)

        glDrawArrays(GL_TRIANGLES, 0, 6)

        glBindVertexArray(0)

        # dessin des 4 côtés
        glBindVertexArray(vao_cube)

        glUniform3fv(glGetUniformLocation(shader, 'color'), 1, (0.8, 0.8, 0.8))

        M = TranslationMatrix(0, -50, 0).dot(ScaleMatrix(tx, 50, 50))
        glUniformMatrix4fv(glGetUniformLocation(shader, 'pvMatrix'), 1, True, PV)
        glUniformMatrix4fv(glGetUniformLocation(shader, 'mMatrix'), 1, True, M)
        glDrawArrays(GL_TRIANGLES, 0, 36)

        M = TranslationMatrix(0, ty, 0).dot(ScaleMatrix(tx, 50, 50))
        glUniformMatrix4fv(glGetUniformLocation(shader, 'pvMatrix'), 1, True, PV)
        glUniformMatrix4fv(glGetUniformLocation(shader, 'mMatrix'), 1, True, M)
        glDrawArrays(GL_TRIANGLES, 0, 36)

        M = TranslationMatrix(-50, 0, 0).dot(ScaleMatrix(50, ty, 50))
        glUniformMatrix4fv(glGetUniformLocation(shader, 'pvMatrix'), 1, True, PV)
        glUniformMatrix4fv(glGetUniformLocation(shader, 'mMatrix'), 1, True, M)
        glDrawArrays(GL_TRIANGLES, 0, 36)
        
        M = TranslationMatrix(tx, 0, 0).dot(ScaleMatrix(50, ty, 50))
        glUniformMatrix4fv(glGetUniformLocation(shader, 'pvMatrix'), 1, True, PV)
        glUniformMatrix4fv(glGetUniformLocation(shader, 'mMatrix'), 1, True, M)
        glDrawArrays(GL_TRIANGLES, 0, 36)

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
            glUniformMatrix4fv(glGetUniformLocation(shader, 'mMatrix'), 1, True, T @ S) # T.dot(S) si Python < 3.5
            glDrawArrays(GL_TRIANGLES, 0, 36)
        
        # dessin des balles
        glUniform3fv(glGetUniformLocation(shader, 'color'), 1, ORANGE)
        for b in balles:
            T = TranslationMatrix(b.x, ty - b.y - b.taille, 0)
            S = ScaleMatrix(b.taille, b.taille, b.taille)
            glUniformMatrix4fv(glGetUniformLocation(shader, 'pvMatrix'), 1, True, PV)
            glUniformMatrix4fv(glGetUniformLocation(shader, 'mMatrix'), 1, True, T @ S) # T.dot(S) si Python < 3.5
            glDrawArrays(GL_TRIANGLES, 0, 36)

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
