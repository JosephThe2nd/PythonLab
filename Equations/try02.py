import numpy as np

R = int(input("Enter the number of rows/columns: "))

print("Introduceti elementele intr-o singură linie, separate prin space:")

entries = list(map(float, input().split()))

#Afisare Matrice
matrix = np.array(entries).reshape(R, R)
print(matrix)
