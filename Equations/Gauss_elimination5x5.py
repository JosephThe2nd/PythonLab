#2.117*x1 + 2x2 = 1691.45
#2.8235*x1 - 4x2  = 1935.22
#0.7058*x1 - 0.666*x2 + x3 = -241.9
#-0.5294*x1 - 0.33*x2 + x4 = -211.43
#-0.4705*x1 - 0.666*x2 + x5 = 762.02

#x1 = 753.54    x2 = 48.101 x3 = -741.71    x4 = 203.37     x5 =   1148.6
# System 5x5

import numpy
from numpy import array,zeros

#Input System of Equations
# a - augmented matrix
# b - dupa egal
# x - solutiile
a = array([[2.117,2,0,0,0], 
           [2.8235,-4,0,0,0],
           [0.7058,-0.666,1,0,0],
           [-0.5294,-0.33,0,1,0],
           [-0.4705,-0.666,0,0,1]], float)
 
b = array([1691.45,1935.22,-241.9,-211.43,762.02], float)
n = len(b)
x = zeros(n, float)

#Forward Elimination
for k in range(n-1):
    for i in range(k+1, n):
        fctr = a[i,k] / a[k,k]
        for j in range(k,n):
            a[i,j] = a[i,j] - fctr*a[k,j]
        b[i] = b[i] - fctr*b[k]

#Back Substitution
x[n-1] = b[n-1] / a[n-1, n-1]
for i in range(n-2,-1,-1):
    Sum = b[i]
    for j in range(i+1,n):
        Sum = Sum - a[i,j]*x[j]
    x[i] = Sum/a[i,i]

print('The solution of the system:')
print(f'x1 = {x[0]}')
print(f'x2 = {x[1]}')
print(f'x3 = {x[2]}')
print(f'x4 = {x[3]}')
print(f'x5 = {x[4]}')
