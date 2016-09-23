#!encoding=utf-8
from OpenGL.GL import *
from OpenGL.GL import shaders
import ctypes
import pygame

USE_NUMPY = True # Mettre à False si vous n'avez pas installé numpy

if USE_NUMPY:
    import numpy
else:
    import array

vertex_shader = """
#version 330
in vec4 position;
void main()
{
    gl_Position = position;
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

vertices = [ 0.6,  0.6, 0.0, 1.0,
            -0.6,  0.6, 0.0, 1.0,
             0.0, -0.6, 0.0, 1.0]

vertices = (numpy.array(vertices, dtype=numpy.float32) if USE_NUMPY else
            array.array('f', vertices))

def create_object(shader):
    # Create a new VAO (Vertex Array Object) and bind it
    vertex_array_object = glGenVertexArrays(1)
    glBindVertexArray( vertex_array_object )
    
    # Generate buffers to hold our vertices
    vertex_buffer = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vertex_buffer)
    
    # Get the position of the 'position' in parameter of our shader and bind it.
    position = glGetAttribLocation(shader, 'position')
    glEnableVertexAttribArray(position)
    
    # Describe the position data layout in the buffer
    glVertexAttribPointer(position, 4, GL_FLOAT, False, 0, ctypes.c_void_p(0))
    
    # Send the data over to the buffer
    glBufferData(GL_ARRAY_BUFFER, 48, vertices if USE_NUMPY else vertices.tostring(), GL_STATIC_DRAW)
    
    # Unbind the VAO first (Important)
    glBindVertexArray( 0 )
    
    # Unbind other stuff
    glDisableVertexAttribArray(position)
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    
    return vertex_array_object
    
def display(shader, vertex_array_object):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glUseProgram(shader)
    
    glBindVertexArray( vertex_array_object )
    glDrawArrays(GL_TRIANGLES, 0, 3)
    glBindVertexArray( 0 )
    
    glUseProgram(0)

def main():
    pygame.init()
    screen = pygame.display.set_mode((512, 512), pygame.OPENGL|pygame.DOUBLEBUF)
    glClearColor(0.5, 0.5, 0.5, 1.0)
    glEnable(GL_DEPTH_TEST)

    shader = shaders.compileProgram(
        shaders.compileShader(vertex_shader, GL_VERTEX_SHADER),
        shaders.compileShader(fragment_shader, GL_FRAGMENT_SHADER)
    )
    
    vertex_array_object = create_object(shader)
    
    clock = pygame.time.Clock()
    
    done = False
    while not done:     
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        
        display(shader, vertex_array_object)
        pygame.display.flip()

if __name__ == '__main__':
    try:
        main()
    finally:
        pygame.quit()