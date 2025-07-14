# Natalie Banks
# 7/5/2026
# P4LAB1A
# draw triangle and square using turtle

import turtle


t = turtle.Turtle()
t.pensize(3)


t.color("blue")
for _ in range(4):
    t.forward(100)
    t.right(90)


t.color("green")
for _ in range(3):
    t.forward(100)
    t.left(120)

turtle.done()



