from OpenGL.GL import *
from OpenGL.GL import shaders
import ctypes
import pygame

USE_NUMPY = True

if USE_NUMPY:
    import numpy
else:
    import array

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

vertices = [ 0.6,  0.6, 0.0, 1.0,
            -0.6,  0.6, 0.0, 1.0,
             0.0, -0.6, 0.0, 1.0]

texcoords = [0,0, 0,1, 1,0.5]

vertices = (numpy.array(vertices, dtype=numpy.float32) if USE_NUMPY else
            array.array('f', vertices))

texcoords = (numpy.array(texcoords, dtype=numpy.float32) if USE_NUMPY else
            array.array('f', texcoords))

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
    glVertexAttribPointer(position, 4, GL_FLOAT, False, 0, ctypes.c_void_p(0))
    glBufferData(GL_ARRAY_BUFFER, 48, vertices if USE_NUMPY else vertices.tostring(), GL_STATIC_DRAW)
    
    texcoord_buffer = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, texcoord_buffer)
    
    mytexcoord = glGetAttribLocation(shader, 'mytexcoord')
    glEnableVertexAttribArray(mytexcoord)
    glVertexAttribPointer(mytexcoord, 2, GL_FLOAT, False, 0, ctypes.c_void_p(0))
    glBufferData(GL_ARRAY_BUFFER, 24, texcoords if USE_NUMPY else texcoords.tostring(), GL_STATIC_DRAW)
    
    # texture
    image = pygame.image.load('player.png').convert_alpha()
    image_data = pygame.image.tostring(image, 'RGBA', 1)
    
    global vaisseau_tex
    vaisseau_tex = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, vaisseau_tex)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.get_width(), image.get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glBindTexture(GL_TEXTURE_2D, 0)
    
    # Unbind the VAO first (Important)
    glBindVertexArray( 0 )
    
    # Unbind other stuff
    # glDisableVertexAttribArray(position)
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    
    return vertex_array_object
    
def display(shader, vertex_array_object):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glUseProgram(shader)
    
    glBindVertexArray( vertex_array_object )
    glActiveTexture(GL_TEXTURE0) # tex 0 on GPU
    glBindTexture(GL_TEXTURE_2D, vaisseau_tex) # is vaisseau_tex
    loc_vaisseau = glGetUniformLocation(shader, 'vaisseau')
    glUniform1i(loc_vaisseau, 0) # vaisseau is tex unit 0
    glDrawArrays(GL_TRIANGLES, 0, 3)
    glBindVertexArray( 0 )
    
    glUseProgram(0)

def main():
    pygame.init()
    screen = pygame.display.set_mode((512, 512), pygame.OPENGL|pygame.DOUBLEBUF)
    glClearColor(0.5, 0.5, 0.5, 1.0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_ALPHA_TEST);
    glAlphaFunc(GL_GREATER, 0);
    # glEnable(GL_TEXTURE_2D)
    # glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);

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