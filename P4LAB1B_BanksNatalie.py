# Natalie Banks
# 7/5/2025
# P4LAB1B
# drawing intials using turtle


import turtle

t = turtle.Turtle()
t.pensize(5)
t.color("purple")


t.penup()
t.goto(-100, 0)
t.pendown()
t.goto(-100, 100)
t.goto(-50, 0)
t.goto(-50, 100)


t.penup()
t.goto(0, 0)
t.pendown()


t.goto(0, 100)
t.circle(-25, 180)
t.goto(0, 50)
t.circle(-25, 180)
t.goto(0, 0)


t.hideturtle()
turtle.done()
