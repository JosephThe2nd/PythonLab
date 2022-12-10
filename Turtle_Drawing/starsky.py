import turtle
import random

t = turtle.Turtle()

t.getscreen().bgcolor("#000000")

def draw_star(turtle_obj,size):
    for _ in range(5):
        turtle_obj.forward(size)
        turtle_obj.left(216)

t.color("white","yellow")
t.speed(0)
for _ in range(50):
    x, y = random.randint(-300,300),random.randint(-300,300) # 0  este centru ecranului din stanga sus creste
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    draw_star(t,random.randint(5,25))
    t.end_fill()

t.setheading()
turtle.done()