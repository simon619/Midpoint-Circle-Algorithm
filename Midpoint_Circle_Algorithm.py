from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math


def init():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    # call the draw methods here
    draw()
    glutSwapBuffers()


def write_pixel(m, n):
    glPointSize(1.5)
    glColor3d(1, 0, 0)
    glBegin(GL_POINTS)
    glVertex2f(m, n)
    glEnd()


def circle_point(p, q, h, k):
    write_pixel(h + p, k + q)
    write_pixel(h + q, k + p)
    write_pixel(h + q, k - p)
    write_pixel(h + p, k - q)
    write_pixel(h - p, k - q)
    write_pixel(h - q, k - p)
    write_pixel(h - q, k + p)
    write_pixel(h - p, k + q)


def mid_point(rad, h, k):
    d = 1 - rad
    x = 0
    y = rad
    circle_point(x, y, h, k)
    while x < y:
        if d < 0:
            d = d + 2 * x + 3
            x += 1
        else:
            d = d + 2 * x - 2 * y + 5
            x += 1
            y -= 1
        circle_point(x, y, h, k)


def draw():
    mid_point(200, 250, 250)
    a = [0, math.pi / 4, math.pi / 2, (3 * math.pi) / 4, math.pi, (5 * math.pi) / 4, (3 * math.pi) / 2, (7 * math.pi) / 4]
    for i in a:
        mid_point(100, 250 + 100 * math.cos(i), 250 + 100 * math.sin(i))


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
glutCreateWindow("OpenGL Template")
glutDisplayFunc(showScreen)

init()

glutMainLoop()