from OpenGL.GL import *
from OpenGL.GLUT import *
def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_TRIANGLES)
    glVertex2f(0, 1)
    glVertex2f(-1, -1)
    glVertex2f(1, -1)
    glEnd()
    glutSwapBuffers()
glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(800, 600)
glutCreateWindow(b"Test")
glutDisplayFunc(draw)
glutMainLoop()