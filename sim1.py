import glfw
from OpenGL.GL import *

def main():
    if not glfw.init():
        return
    
    window = glfw.create_window(800, 600, "OpenGL Test", None, None)
    if not window:
        glfw.terminate()
        return
    
    glfw.make_context_current(window)
    
    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT)
        glBegin(GL_TRIANGLES)
        glColor3f(0, 0, 1)
        glVertex3f(-0.5, -0.5, 0)
        glVertex3f(0.5, -0.5, 0)
        glVertex3f(0, 0.5, 0)
        glEnd()
        glfw.swap_buffers(window)
        glfw.poll_events()
    
    glfw.terminate()

if __name__ == "__main__":
    main()