
import numpy as np

arr1 = np.array([90, 180, 270, 360])
print(arr1)

x = np.deg2rad(arr1) #converts degrees to radians
print(x)

y = np.sin(x) #calculeaza sinusul 
print(y)

print()
arr2 = np.array([2, 4, 8, 10])

x = np.lcm.reduce(arr2) #Lowest Common Multiple
y = np.gcd.reduce(arr2) #Greatest Common Denominator


print("Cel mai mic multiplu comun este:", x)
print("Cel mai mare divizor comun este:", y)

arr3 = np.array([1, 2, 3, 4])
z = np.prod([arr2, arr3])
z1 = np.sum([arr2, arr3])
print("Produsul elementelor din cei doi vectori este:", z)
print("Suma elementelor din cei doi vectori este:", z1)

