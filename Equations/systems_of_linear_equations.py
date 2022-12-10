import numpy as np

#2a - 3b + c - 4d = 27
#5a + 5b - 2c + 3d = -23
#3a - b - 3c - d = 18
#4a + b - 4c + 4d = -26

A = np.array([[2,-3,1,-4],[5,5,-2,3],[3,-1,3,-1],[4,1,-4,4]])
B = np.array([[27],[-23],[18],[-26]])

X = np.dot(np.linalg.inv(A),B)

print(f'a is {X[0]}, b is {X[1]}, c = {X[2]}, d = {X[3]}')

XX = np.linalg.solve(A,B)
print (XX)

#System of non-linear equations 
#x^2 + y = 5 
#x*2 + y^2 = 7


