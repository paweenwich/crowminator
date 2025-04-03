import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import math

platform_yaw = 90.0  # Horizontal rotation of the sentry gun (0-180 degrees)
platform_pitch = 0.0  # Vertical tilt (-90 to 90 degrees)
distance = 5.0  # Distance from scene

def initialize():
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.5, 0.7, 1.0, 1.0)  # Sky blue background
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 800/600, 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

def update_camera():
    glLoadIdentity()
    
    # Convert platform angles to camera position
    rad_yaw = math.radians(platform_yaw)
    rad_pitch = math.radians(platform_pitch)
    
    eye_x = distance * math.cos(rad_pitch) * math.cos(rad_yaw)
    eye_y = distance * math.sin(rad_pitch)
    eye_z = distance * math.cos(rad_pitch) * math.sin(rad_yaw)
    
    target_x = 0
    target_y = 0
    target_z = 0
    
    up_x = 0
    up_y = 1
    up_z = 0
    
    gluLookAt(eye_x, eye_y, eye_z, target_x, target_y, target_z, up_x, up_y, up_z)

def draw_ground():
    glColor3f(0.3, 0.6, 0.3)  # Green ground
    glBegin(GL_QUADS)
    glVertex3f(-5, -1, -5)
    glVertex3f(5, -1, -5)
    glVertex3f(5, -1, 5)
    glVertex3f(-5, -1, 5)
    glEnd()

def draw_cube(x, y, z, size):
    glPushMatrix()
    glTranslatef(x, y, z)
    glScalef(size, size, size)
    glColor3f(0.6, 0.3, 0.1)
    glBegin(GL_QUADS)
    
    # Front face
    glVertex3f(-0.5, -0.5, 0.5)
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(0.5, 0.5, 0.5)
    glVertex3f(-0.5, 0.5, 0.5)
    
    # Back face
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(-0.5, 0.5, -0.5)
    glVertex3f(0.5, 0.5, -0.5)
    glVertex3f(0.5, -0.5, -0.5)
    
    # Left face
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(-0.5, -0.5, 0.5)
    glVertex3f(-0.5, 0.5, 0.5)
    glVertex3f(-0.5, 0.5, -0.5)
    
    # Right face
    glVertex3f(0.5, -0.5, -0.5)
    glVertex3f(0.5, 0.5, -0.5)
    glVertex3f(0.5, 0.5, 0.5)
    glVertex3f(0.5, -0.5, 0.5)
    
    # Top face
    glVertex3f(-0.5, 0.5, -0.5)
    glVertex3f(-0.5, 0.5, 0.5)
    glVertex3f(0.5, 0.5, 0.5)
    glVertex3f(0.5, 0.5, -0.5)
    
    # Bottom face
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(0.5, -0.5, -0.5)
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(-0.5, -0.5, 0.5)
    
    glEnd()
    glPopMatrix()

def draw_objects():
    draw_cube(-2, -0.5, -2, 0.5)
    draw_cube(2, -0.5, 2, 0.5)

def draw_scene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    update_camera()
    draw_ground()
    draw_objects()

def key_callback(window, key, scancode, action, mods):
    global platform_yaw, platform_pitch
    if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
        glfw.set_window_should_close(window, True)
    elif key == glfw.KEY_LEFT and (action == glfw.PRESS or action == glfw.REPEAT):
        platform_yaw = max(0, platform_yaw - 5)
    elif key == glfw.KEY_RIGHT and (action == glfw.PRESS or action == glfw.REPEAT):
        platform_yaw = min(180, platform_yaw + 5)
    elif key == glfw.KEY_UP and (action == glfw.PRESS or action == glfw.REPEAT):
        platform_pitch = min(90, platform_pitch + 5)
    elif key == glfw.KEY_DOWN and (action == glfw.PRESS or action == glfw.REPEAT):
        platform_pitch = max(-90, platform_pitch - 5)

def main():
    if not glfw.init():
        return
    
    window = glfw.create_window(800, 600, "Camera Controlled Scene", None, None)
    if not window:
        glfw.terminate()
        return
    
    glfw.make_context_current(window)
    glfw.set_key_callback(window, key_callback)
    initialize()
    
    while not glfw.window_should_close(window):
        draw_scene()
        glfw.swap_buffers(window)
        glfw.poll_events()
    
    glfw.terminate()

if __name__ == "__main__":
    main()
