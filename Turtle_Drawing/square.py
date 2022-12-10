import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("Black")
t.color("White")

print(t.position())
t.penup() #100
t.goto(-100,100)
print(t.position())
t.pendown()
t.setheading(0) 
t.forward(200)
print(t.position())
turtle.done()