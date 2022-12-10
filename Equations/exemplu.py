import numpy as np
from numpy import array,zeros
'''
#Input System of Equations
# a - augmented matrix
# b - dupa egal / constants
# x - solutiile/necunoscutele
a = array([[2,1],[1,-5]], float)
#dim = int(input("Introduceti dimensiunea matricii de adiacenta: "))
#print("Introduceti elementele matricii de adiacenta intr-o singură linie, separate prin space:")
#a = list((map(float,input().split()))) 
#a = np.array(a).reshape(dim,dim)
#print(a)


#print("Introduceti valorile matricii de constante: ")
#b = list((map(float,input().split())))
#b = np.array(b)
b = array([3,0], float)
n = len(b)
x = zeros(n, float) #vectorul de solutii

#Forward Elimination - obtinerea matricii cu 0 sub diagonala principala
for k in range(n-1): #the fixed row (merge pana la n-2 in python)
    for i in range(k+1, n): 
        fctr = a[i,k] / a[k,k]
        for j in range(k,n):
            a[i,j] = a[i,j] - fctr*a[k,j]
        b[i] = b[i] - fctr*b[k]


#Back Substitution - calculam valoarea necunoscutelor incepand de la ultima ecuatie
x[n-1] = b[n-1] / a[n-1, n-1]
for i in range(n-2,-1,-1):
    Sum = b[i]
    for j in range(i+1,n):
        Sum = Sum - a[i,j]*x[j]
    x[i] = Sum/a[i,i]

print('The solution of the system:')
print(f'x = {x[0]}')
print(f'y = {x[1]}')
'''
x = 15/11
y = 3/11
h1 = (2 * x + y - 3)
h2 = (x - 5 * y)
f = (h1**2 + h2**2)
print(h1,h2,f)
