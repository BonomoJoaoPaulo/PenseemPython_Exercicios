import turtle
import math

from numpy import square

bob = turtle.Turtle()

# funcao que desenha um poligono
# def polygon(t, n, length):
#    angle = 360 / n
#    for i in range(n):
#        t.fd(length)
#        t.lt(angle)

# polygon(bob, 12, 75)


def polyline(t, n, length, angle):
    """Isso é uma docstring
    Desenha n segmentos de reta com o comprimento dado e
    ângulo (em graus) entre eles. t é um turtle.
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)


def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)


def circle(t, r):
    arc(t, r, 360)

circle(bob, 100)
turtle.mainloop()
