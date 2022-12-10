import turtle
#with l system grammar respresentation
#screen settings

#WIDTH, HEIGHT = 1600,900
screen = turtle.Screen()
screen.setup(width=650,height=650,startx=None,starty=None)
screen.screensize(3*650,3*650)
screen.bgcolor("black")
screen.delay(0)
turtle.bgcolor("black")
turtle.delay(0)

#turtle settings
leo = turtle.Turtle()
leo.pensize(2)
leo.speed(10)
#leo.setpos(WIDTH/4,HEIGHT/4) 
leo.color('magenta')

# l - system settings

gens = 6
axiom = 'F+XFF+XFF+XFF+XF'
chr_1, rule_1 = 'X', "-Y-F+XFF+XFF+XF-Y"
chr_2, rule_2 = 'Y', 'YFY'
step = 5
angle = 90

def apply_rules(axiom):
    return ''.join([rule_1 if chr == chr_1 else 
                    rule_2 if chr == chr_2 else chr for chr in axiom])

def get_result(gens, axiom):
    for gen in range(gens):
        axiom = apply_rules(axiom)
    return axiom


turtle.pencolor("white")
#turtle.goto(-WIDTH // 2 + 60, HEIGHT // 2 - 100)
turtle.goto(0,0)
turtle.clear()
turtle.write(f'generation: {gens}', font=("Arial", 30, "normal"), align="right")   
    
axiom = get_result(gens, axiom)

for chr in axiom:
    if chr == chr_1 or chr == chr_2:
        leo.forward(step)
    elif chr == "+":
        leo.right(angle)
    elif chr == "-":
        leo.left(angle)

        
turtle.mainloop()