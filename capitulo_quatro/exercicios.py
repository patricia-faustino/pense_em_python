import math
import turtle


# 1-
# def square(t):
#     for i in range(4):
#         t.fd(100)
#         t.lt(90)
#
#
# bob = turtle.Turtle()
# square(bob)


# 2-
def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)


# 3 -
'''Desenha polígonos de acordo com o tamanho e número de lados
informado. n é o número de lados, t é o turtle e length é o tamanho dos lados
'''
def polygon(t, length, n):
    angle = 360.0 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def arcle(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    polyline(t, n, step_length, step_angle)


def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def circle(t, r):
    arcle(t, r, 360)

# def arcle(t, r, angle):

# uma interface é o contrato da função, é como devemos chamar a função de acordo com sua declaração, ou seja,
# deve-se chamar pelo nome e utilizando os parametros informados no momento da declaração


bob = turtle.Turtle()
# polygon(bob, 100, 8)
circle(bob, 95)
turtle.mainloop()
