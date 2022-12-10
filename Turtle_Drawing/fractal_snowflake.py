from turtle import *

shape("turtle")
speed(0)

def snowflake_side(length, levels):
    if levels == 0:
        forward(length)
        return
    
    length /= 3.0
    snowflake_side(length, levels-1)
    left(60)
    snowflake_side(length, levels-1)
    right(120)
    snowflake_side(length, levels-1)
    left(60)
    snowflake_side(length, levels-1)


#snowflake_side(200,2)
#On Click snowflake

# def create_snowflake(x, y):
#     sides = 3
#     length = 200
#     penup()
#     goto(x,y)
#     pendown()
#     colors = ["green", "blue", "yellow","black"]
#     for i in range(sides):
#         color(colors[i])
#         snowflake_side(length,sides)
#         right(360 / sides)
    
# getscreen().onclick(create_snowflake)


def create_snowflake(sides,length):
    colors = ["green", "blue", "yellow","black","purple"]
    for i in range(sides):
        color(colors[i])
        snowflake_side(length,sides)
        right(360 / sides)
create_snowflake(3, 200)
hideturtle()
mainloop()