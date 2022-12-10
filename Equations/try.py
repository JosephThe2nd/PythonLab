# A basic code for matrix input from user

R = int(input("Enter the number of rows/columns:"))

matrix = []
print("Introduceti elementele:")


for i in range(R):		
	a =[]
	for j in range(R):	 
		a.append(int(input()))
	matrix.append(a)


for i in range(R):
	for j in range(R):
		print(matrix[i][j], end = " ")
	print()
