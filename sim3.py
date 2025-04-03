import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import time

angle = 0.0
last_time = time.time()
camera_x, camera_y = 0.0, 0.0


def initialize():
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 800/600, 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)


def draw_cube():
    global angle, last_time, camera_x, camera_y

    current_time = time.time()
    delta_time = current_time - last_time
    last_time = current_time
    angle += (360.0 / 10.0) * delta_time

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(camera_x, camera_y, -5.0)
    glRotatef(angle, 1.0, 1.0, 1.0)

    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 1.0)

    vertices = [
        (-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1),
        (-1, -1,  1), (1, -1,  1), (1, 1,  1), (-1, 1,  1)
    ]

    faces = [
        (0, 1, 2, 3), (4, 5, 6, 7), (0, 1, 5, 4),
        (2, 3, 7, 6), (0, 3, 7, 4), (1, 2, 6, 5)
    ]

    for face in faces:
        for vertex in face:
            glVertex3fv(vertices[vertex])

    glEnd()

    glColor3f(1.0, 1.0, 0.0)
    glBegin(GL_LINES)
    edges = [
        (0,1), (1,2), (2,3), (3,0),
        (4,5), (5,6), (6,7), (7,4),
        (0,4), (1,5), (2,6), (3,7)
    ]

    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])

    glEnd()


def key_callback(window, key, scancode, action, mods):
    global camera_x, camera_y
    if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
        glfw.set_window_should_close(window, True)
    elif key == glfw.KEY_LEFT and (action == glfw.PRESS or action == glfw.REPEAT):
        camera_x += 0.1
    elif key == glfw.KEY_RIGHT and (action == glfw.PRESS or action == glfw.REPEAT):
        camera_x -= 0.1
    elif key == glfw.KEY_UP and (action == glfw.PRESS or action == glfw.REPEAT):
        camera_y -= 0.1
    elif key == glfw.KEY_DOWN and (action == glfw.PRESS or action == glfw.REPEAT):
        camera_y += 0.1


def main():
    if not glfw.init():
        return

    window = glfw.create_window(800, 600, "Rotating Cube", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)
    glfw.set_key_callback(window, key_callback)
    initialize()

    while not glfw.window_should_close(window):
        draw_cube()
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()


if __name__ == "__main__":
    main()
