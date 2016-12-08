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

vertices = [
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
]

vertices = numpy.array(vertices, dtype=numpy.float32)

class Axe:
    pass

Axe.X = 0
Axe.Y = 1
Axe.Z = 2

def polar(*args):
    if len(args) == 2: r,t = args
    elif len(args) == 1: r,t = 1,args[0]
    else: raise TypeError('Accept 1 or 2 arguments')
    
    return r * vec2(cos(t), sin(t))

def polard(*args):
    if len(args) == 2: r,t = args
    elif len(args) == 1: r,t = 1,args[0]
    else: raise TypeError('Accept 1 or 2 arguments')
    
    return r * polar(radians(t))

def vec2(x,y):
    return array((x,y), dtype=numpy.float32)

def vec3(*args):
    '''
    returns a vector in 3 dimensions
    vec3(1,2,3)   
    vec3((1,2),3)
    '''
    if len(args) == 3: x,y,z = args
    elif len(args) == 2: (x,y),z = args
    else: raise TypeError('Accept 2 or 3 arguments')
    
    return array((x,y,z), dtype=numpy.float32)

def normalized(v):
    return v / linalg.norm(v)

def PerspectiveMatrix(fovy, aspect, zNear, zFar):
    f = 1.0 / tan(radians(fovy) / 2.0)
    return array([
            [f/aspect, 0, 0, 0],
            [0, f, 0, 0],
            [0, 0, 1. * (zFar + zNear) / (zNear - zFar), 2.0 * zFar * zNear / (zNear - zFar)],
            [0,0,-1,0]
        ], dtype=numpy.float32)

def TranslationMatrix(*args):
    '''
    returns the TranslationMatrix 
    TranslationMatrix(2,1,0)
    TranslationMatrix(2,1) 
    TranslationMatrix((2,1,0))
    '''
    if len(args) == 3: tx,ty,tz = args
    elif len(args) == 2: (tx,ty),tz = args, 0
    elif len(args) == 1: tx,ty,tz = args[0]
    else: raise TypeError("Accept 1, 2 or 3 arguments")
        
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
    e, c, up = array(e), array(c), array(up)

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
    x,y,z = normalized(axe)
    
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
            [x*x*k + c,   x*y*k - z*s, x*z*k + y*s, 0],
            [y*x*k + z*s, y*y*k + c,   y*z*k - x*s, 0],
            [x*z*k - y*s, y*z*k + x*s, z*z*k + c,   0],
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
    pv = p.dot(v)
    
    # build model matrix of triangles (boucy animation)
    m = TranslationMatrix(0, 0, abs(sin(3*t)))
    pvm = pv.dot(m)
    
    # use our only vao
    glBindVertexArray(vertex_array_object)
    
    # set matrix
    loc_matrix = glGetUniformLocation(shader, 'pvmMatrix')
    glUniformMatrix4fv(loc_matrix, 1, False, pvm.T)
    
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
        shaders.compileShader(fragment_shader, GL_FRAGMENT_SHADER)
    )
    
    vertex_array_object = create_object(shader)
    
    clock = pygame.time.Clock()
    
    t = 0
    done = False
    while not done:     
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        
        t += 1
        display(shader, vertex_array_object, t/60.)
        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    try:
        main()
    finally:
        pygame.quit()