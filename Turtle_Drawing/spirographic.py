import turtle

turtle.bgcolor("Black")
t = turtle.Turtle()
colors = ["white", "black"]
t.speed(0)
for number in range(0,800):
    t.forward(number+1)
    t.right(89)#unghiul daca ar fi 90 ar fi patrat
    t.pencolor(colors[number%2])

turtle.done()