import turtle
import math

screen = turtle.Screen()


for i in range(1300):
    vt = i / 40 * math.pi
    Y = (vt * 5 + 5) * math.sin(vt)
    X = (vt * 5 + 5) * math.cos(vt)
    turtle.goto(X, Y)

screen.exitonclick()

# créditos: https://www.youtube.com/watch?v=hytQiMHX9kQ
