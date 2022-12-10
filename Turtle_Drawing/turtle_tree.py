from turtle import *

shape("turtle")
speed(0) # 0 is fastest , 1 is slowest

def tree(size, levels, angle):
    if levels == 0:
        color("green")
        dot(size)
        color("black")
        return

    forward(size)

    right(angle)

    tree(size * 0.8, levels - 1, angle)

    left(angle * 2)

    tree(size * 0.8, levels - 1, angle)

    right(angle)
    backward(size)

left(90)
tree(70,7,30)

mainloop()