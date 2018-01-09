#!coding: utf-8
from __future__ import print_function, division

from OpenGL.GL import *
from OpenGL.GL import shaders
import ctypes
import pygame

import numpy

from vec3_utils import * # téléchargez vec3_utils [ici](https://robertvandeneynde.be/parascolaire/vec3_utils.py.html)

vertex_shader = """
#version 330
in vec4 position;
in vec2 mytexcoord;
out vec2 texcoord;
void main()
{
    texcoord = mytexcoord;
    gl_Position = position;
}
"""

fragment_shader = """
#version 330
uniform sampler2D vaisseau;
in vec2 texcoord;
out vec4 pixel;
void main()
{
    pixel = vec4(texture(vaisseau, texcoord).rgb, 1);
}
"""

vertices = farray([
    0.6, 0.6, 0.0, 1.0,
    -0.6, 0.6, 0.0, 1.0,
    0.0, -0.6, 0.0, 1.0,
])

texcoords = farray([
    0, 0,
    0, 1,
    1, 0.5,
])

def create_object(shader):
    # Create a new VAO (Vertex Array Object) and bind it
    vertex_array_object = glGenVertexArrays(1)
    glBindVertexArray(vertex_array_object)
    
    # Generate buffers to hold our vertices
    vertex_buffer = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vertex_buffer)
    
    # Get the position of the 'position' in parameter of our shader and bind it.
    position = glGetAttribLocation(shader, 'position')
    if position != -1:
        glEnableVertexAttribArray(position)
        glVertexAttribPointer(position, 4, GL_FLOAT, False, 0, ctypes.c_void_p(0))
        glBufferData(GL_ARRAY_BUFFER, 48, vertices, GL_STATIC_DRAW)
    else:
        print('Inactive attribute "{}"'.format('position'))
    
    # Texture coordinates
    mytexcoord = glGetAttribLocation(shader, 'mytexcoord')
    if mytexcoord != -1:
        glEnableVertexAttribArray(mytexcoord)
        glVertexAttribPointer(mytexcoord, 2, GL_FLOAT, False, 0, ctypes.c_void_p(0))
        glBufferData(GL_ARRAY_BUFFER, 24, texcoords, GL_STATIC_DRAW)
    else:
        print('Inactive attribute "{}"'.format('mytexcoord'))
    
    # Texture
    texcoord_buffer = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, texcoord_buffer)
    
    image = pygame.image.load('player.png').convert_alpha()
    image_data = pygame.image.tostring(image, 'RGBA', 1)
    
    vaisseau_tex = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, vaisseau_tex)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.get_width(), image.get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glBindTexture(GL_TEXTURE_2D, 0)
    
    # Unbind the VAO first (Important)
    glBindVertexArray(0)
    
    # Unbind other stuff
    # glDisableVertexAttribArray(position)
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    
    return vertex_array_object, vaisseau_tex
    
def display(shader, vertex_array_object, vaisseau_tex):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glUseProgram(shader)
    
    glBindVertexArray(vertex_array_object)
    glActiveTexture(GL_TEXTURE0) # tex 0 on GPU
    glBindTexture(GL_TEXTURE_2D, vaisseau_tex) # is vaisseau_tex
    loc_vaisseau = glGetUniformLocation(shader, 'vaisseau')
    glUniform1i(loc_vaisseau, 0) # vaisseau is tex unit 0
    glDrawArrays(GL_TRIANGLES, 0, 3)
    glBindVertexArray(0)
    
    glUseProgram(0)

def main():
    pygame.init()
    screen = pygame.display.set_mode((512, 512), pygame.OPENGL|pygame.DOUBLEBUF)
    glClearColor(0.5, 0.5, 0.5, 1.0)
    glEnable(GL_DEPTH_TEST)

    shader = shaders.compileProgram(
        shaders.compileShader(vertex_shader, GL_VERTEX_SHADER),
        shaders.compileShader(fragment_shader, GL_FRAGMENT_SHADER))
    
    vertex_array_object, vaisseau_tex = create_object(shader)
    
    clock = pygame.time.Clock()
    
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        
        display(shader, vertex_array_object, vaisseau_tex)
        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    try:
        main()
    finally:
        pygame.quit()
