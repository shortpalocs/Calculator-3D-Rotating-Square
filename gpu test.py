import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from PIL import Image
import time
import numpy

# Vertices of the pyramid
vertices = [
    [0.0, 1.0, 0.0],  # Top
    [-1.0, -1.0, 1.0],  # Front left
    [1.0, -1.0, 1.0],  # Front right
    [1.0, -1.0, -1.0],  # Back right
    [-1.0, -1.0, -1.0],  # Back left
]

# Faces of the pyramid (using vertex indices)
faces = [
    [0, 1, 2],  # Front face
    [0, 2, 3],  # Right face
    [0, 3, 4],  # Back face
    [0, 4, 1],  # Left face
    [1, 4, 3, 2],  # Bottom face (square)
]

# Texture coordinates
tex_coords = [
    [0.5, 1.0],  # Top
    [0.0, 0.0],  # Bottom left
    [1.0, 0.0],  # Bottom right
]


# Load a texture
def load_texture(image_path):
    texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture)

    # Load the image and flip it vertically
    image = Image.open(image_path)
    image = image.transpose(Image.FLIP_TOP_BOTTOM)
    img_data = image.convert("RGBA").tobytes()

    # Set texture parameters
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.width, image.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    return texture


# Draw the pyramid with textures
def draw_pyramid(texture):
    glBindTexture(GL_TEXTURE_2D, texture)
    glEnable(GL_TEXTURE_2D)

    glBegin(GL_TRIANGLES)
    for i in range(4):  # Draw the 4 triangular faces
        for j, vertex in enumerate(faces[i]):
            glTexCoord2fv(tex_coords[j])
            glVertex3fv(vertices[vertex])
    glEnd()

    # Draw the bottom face (square)
    glBegin(GL_QUADS)
    for vertex in faces[4]:
        glTexCoord2fv([0.5, 0.5])  # Center for texture
        glVertex3fv(vertices[vertex])
    glEnd()

    glDisable(GL_TEXTURE_2D)


def main():
    # Initialize Pygame and set 4K resolution
    pygame.init()
    display = (1920, 1800)  # 4K Resolution
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    # Set up OpenGL perspective
    gluPerspective(20, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -50)

    # Load texture
    texture = load_texture("photo.jpg")  # Use a valid texture image file here

    # Enable depth testing for proper rendering
    glEnable(GL_DEPTH_TEST)

    angle = 180  # Rotation angle

    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return

        # Clear the screen and depth buffer
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Apply rotation
        glPushMatrix()
        glRotatef(angle, 1, 1, 0)  # Rotate around X and Y axes
        draw_pyramid(texture)
        glPopMatrix()

        # Update the display
        pygame.display.flip()

        # Increment the rotation angle
        angle += 1
        if angle >= 360:
            angle = 0

        # Add a small delay for smoother animation
        time.sleep(0.01)


if __name__ == "__main__":
    main()
