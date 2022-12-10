import sympy as sp
x, y, z = sp.symbols('x, y, z')
rho, sigma, beta = sp.symbols('rho, sigma, beta')
f1 = sigma * (y - x)
f2 = x * (rho - z) - y
f3 = x * y - beta * z
print(sp.solvers.solve((f1, f2, f3), (x, y, z)))



