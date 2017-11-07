#!coding: utf-8
from __future__ import print_function, division

from OpenGL.GL import *
from OpenGL.GL import shaders
import ctypes
import pygame
from math import sin, cos, degrees, radians, tan

import numpy
from numpy import array, linalg

vertex_shader = """
#version 330
in vec4 position;
uniform mat4 pvmMatrix;
void main()
{
    gl_Position = pvmMatrix * position;
}
"""

fragment_shader = """
#version 330
out vec4 pixel;
void main()
{
    pixel = vec4(1.0f, 1.0f, 1.0f, 1.0f);
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

def LookAtMatrix(*args):
    """ returns the LookAt matrix
    LookAtMatrix(1,2,3, 4,5,6, 7,8,9)
    LookAtMatrix((1,2,3), (4,5,6), (7,8,9))
    """
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

    return farray([
        [s[0], s[1], s[2], -s.dot(e)],
        [u[0], u[1], u[2], -u.dot(e)],
        [-f[0], -f[1], -f[2], f.dot(e)],
        [0, 0, 0, 1],
    ]) # corresponds to M @ Translate(-e)


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


def RotationMatrix(angle, axe):
    """ Rotation matrix for angle in degree around any axe
    RotationMatrix(30, (0,0,1))
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

vertices = farray([
     0, 0, 0, 1,
     1, 0, 0, 1,
     0, 1, 0, 1,
     
     2, 0, 0, 1,
     0, 2, 0, 1,
     3, 0, 0, 1,
     
     0, 3, 0, 1,
     4, 0, 0, 1,
     0, 4, 0, 1,
     
     0, 0, 0, 1,
     -1, 0, 0, 1,
     0, -1, 0, 1,
     
     -2, 0, 0, 1,
     0, -2, 0, 1,
     -3, 0, 0, 1,
     
     0, -3, 0, 1,
     -4, 0, 0, 1,
     0, -4, 0, 1,
])

def create_object(shader):
    '''
    return the VAO for our simple object
    '''
    vertex_array_object = glGenVertexArrays(1)
    glBindVertexArray( vertex_array_object )
    
    vertex_buffer = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vertex_buffer)
    
    position = glGetAttribLocation(shader, 'position')
    glEnableVertexAttribArray(position)
    
    glVertexAttribPointer(position, 4, GL_FLOAT, False, 0, ctypes.c_void_p(0))
    
    glBufferData(GL_ARRAY_BUFFER, ArrayDatatype.arrayByteCount(vertices), vertices, GL_STATIC_DRAW)
    
    glBindVertexArray(0)
    
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    
    return vertex_array_object
    
def display(shader, vertex_array_object, t):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glUseProgram(shader)
    
    # build projection matrix
    p = PerspectiveMatrix(45, 1.0 * 512/512, 0.1, 100)
    
    # build view matrix (lookAt)
    v = LookAtMatrix(vec3(7 * polar(0.5 * t), 5), (0, 0, 0), (0, 0, 1))
    pv = p @ v
    
    # build model matrix of triangles (bouncy animation)
    m = TranslationMatrix(0, 0, abs(sin(3*t)))
    pvm = pv @ m
    
    # use our only vao
    glBindVertexArray(vertex_array_object)
    
    # set matrix
    loc_matrix = glGetUniformLocation(shader, 'pvmMatrix')
    glUniformMatrix4fv(loc_matrix, 1, True, pvm)
    
    # draw
    glPointSize(5)
    glDrawArrays(GL_TRIANGLES, 0, 18)
    
    # unbind
    glBindVertexArray(0)
    glUseProgram(0)

def main():
    pygame.init()
    screen = pygame.display.set_mode((512, 512), pygame.OPENGL|pygame.DOUBLEBUF)
    glClearColor(0.5, 0.5, 0.5, 1.0)
    glViewport(0, 0, 512, 512)
    glEnable(GL_DEPTH_TEST)

    shader = shaders.compileProgram(
        shaders.compileShader(vertex_shader, GL_VERTEX_SHADER),
        shaders.compileShader(fragment_shader, GL_FRAGMENT_SHADER))
    
    vertex_array_object = create_object(shader)
    
    clock = pygame.time.Clock()
    
    t = 0
    done = False
    while not done:     
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        
        t += 1
        display(shader, vertex_array_object, t/60)
        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    try:
        main()
    finally:
        pygame.quit()
