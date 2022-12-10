import turtle

#screen settings

#WIDTH, HEIGHT = 1600, 900
screen = turtle.Screen()
screen.setup(width=650,height=650,startx=None,starty=None)
#screen.screensize(3 * WIDTH, 3 * HEIGHT)
screen.bgcolor("black")
screen.delay(0)
turtle.bgcolor("black")
turtle.delay(0)

#turtle settings
leo = turtle.Turtle()
leo.pensize(4)
leo.speed(1)
#leo.setpos(-WIDTH // 6, -HEIGHT // 6) 
leo.setpos(0,0)
leo.color('gold')

# l - system settings

gens = 3
axiom = 'F++F++F'
chr_1, rule_1 = 'F', "F-F++F-F"
#chr_2, rule_2 = 'Y', '-FX-Y'
step = 8
angle = 60


def apply_rules(axiom):
    return ''.join([rule_1 if chr == chr_1 else 
                     chr for chr in axiom])

def get_result(gens, axiom):
    for gen in range(gens):
        axiom = apply_rules(axiom)
    return axiom


turtle.pencolor("white")
turtle.goto(0,0)
turtle.clear()
turtle.write(f'generation: {gens}', font=("Arial", 30, "normal"), align="right")   
    
axiom = get_result(gens, axiom)

for chr in axiom:
    if chr == chr_1:
        leo.forward(step)
    elif chr == "+":
        leo.right(angle)
    elif chr == "-":
        leo.left(angle)

        

turtle.mainloop()