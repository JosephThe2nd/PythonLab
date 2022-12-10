from scipy.optimize import fsolve

def equations(p):
    x, y = p
    return (y - x**2 -7 + 5*x, 4*y - 8*x + 21)

x, y =  fsolve(equations, (5, 5))

print((x, y))
