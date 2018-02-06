#!coding: utf-8
from __future__ import print_function, division

from OpenGL.GL import *
from OpenGL.GL import shaders
import ctypes
import pygame
from math import sin, cos, degrees, radians, tan

import numpy
from numpy import array, linalg

from vec3_utils import * # téléchargez vec3_utils [ici](https://robertvandeneynde.be/parascolaire/vec3_utils.py.html)

vertex_shader = """
#version 330
in vec3 position;
in vec3 color;

uniform mat4 pvmMatrix;

out vec3 fcolor;

void main()
{
    gl_Position = pvmMatrix * vec4(position, 1);
    fcolor = color;
}
"""

fragment_shader = """
#version 330

in vec3 fcolor;
out vec4 pixel;

void main()
{
    pixel = vec4(fcolor, 1);
}
"""

vertices = farray([
     0, 0, 0.60,
     1, 0, 0,
     0, 1, 0,
     
     1, 0, 0,
     0, 1, 0,
     1, 1, 1,
     
     0, 0, 0.60,
     -1, 0, 0,
     0, 1, 0,
     
     -1, 0, 0,
     0, 1, 0,
     -1, 1, 1,
])

colors = farray([
     1, 0, 0,
     0, 1, 0,
     0, 0, 1,
     
     1, 0, 0,
     0, 1, 0,
     0, 0, 1,
     
     1, 0, 0,
     0, 1, 0,
     0, 0, 1,
     
     1, 0, 0,
     0, 1, 0,
     0, 0, 1,
])

def create_object(shader):
    # Create a new VAO (Vertex Array Object) and bind it
    vertex_array_object = glGenVertexArrays(1)
    glBindVertexArray( vertex_array_object )
    
    # Get the position of the 'position' in parameter of our shader and bind it.
    position = glGetAttribLocation(shader, 'position')
    if position != -1: # maybe the attribute is useless and was discarded by the compiler
        glEnableVertexAttribArray(position)
    
        # Generate buffers to hold our vertices
        vertex_buffer = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, vertex_buffer)
        
        # Describe the position data layout in the buffer
        glVertexAttribPointer(position, 3, GL_FLOAT, False, 0, ctypes.c_void_p(0))
    
        # Send the data over to the buffer
        glBufferData(GL_ARRAY_BUFFER, ArrayDatatype.arrayByteCount(vertices), vertices, GL_STATIC_DRAW)
    else:
        print('Inactive attribute "{}"'.format('position'))
    
    # Get the position of the 'position' in parameter of our shader and bind it.
    color = glGetAttribLocation(shader, 'color')
    
    if color != -1: # maybe the attribute is useless and was discarded by the compiler
        glEnableVertexAttribArray(color)
        
        # Generate buffers to hold our colors
        vertex_buffer_color = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, vertex_buffer_color)
    
        # Describe the color data layout in the buffer
        glVertexAttribPointer(color, 3, GL_FLOAT, False, 0, ctypes.c_void_p(0))
        
        # Send the data over to the buffer
        glBufferData(GL_ARRAY_BUFFER, ArrayDatatype.arrayByteCount(colors), colors, GL_STATIC_DRAW)
    else:
        print('Inactive attribute "{}"'.format('color'))
    
    # Unbind the VAO first
    glBindVertexArray(0)
    
    # Unbind the VBO
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
    glDrawArrays(GL_TRIANGLES, 0, 18)
    
    # draw other models !
    m2 = TranslationMatrix(3, 2, 1)
    glUniformMatrix4fv(loc_matrix, 1, True, pv @ m2)
    glDrawArrays(GL_TRIANGLES, 0, 18)
    
    m3 = ScaleMatrix(1/2) @ TranslationMatrix(-2, 3, 0) @ RotationMatrix(150, (0,0,1))
    glUniformMatrix4fv(loc_matrix, 1, True, pv @ m3)
    glDrawArrays(GL_TRIANGLES, 0, 18)
    
    # unbind
    glBindVertexArray(0)
    glUseProgram(0)

def main():
    pygame.init()
    screen = pygame.display.set_mode((512, 512), pygame.OPENGL | pygame.DOUBLEBUF)
    pygame.display.set_caption('Colorful birds')
    
    glClearColor(135/255, 206/255, 235/255, 1)
    # glViewport(0, 0, 512, 512) # we don't have to do that because it's the size of the window
    glEnable(GL_DEPTH_TEST)

    shader = shaders.compileProgram(
        shaders.compileShader(vertex_shader, GL_VERTEX_SHADER),
        shaders.compileShader(fragment_shader, GL_FRAGMENT_SHADER))
    
    vertex_array_object = create_object(shader)
    
    clock = pygame.time.Clock()
    
    tick = 0
    done = False
    while not done:     
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        
        tick += 1
        display(shader, vertex_array_object, tick/60)
        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    try:
        main()
    finally:
        pygame.quit()
