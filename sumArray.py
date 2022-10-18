#suma elemente vector

def suma(arr):

	sum = 0

	for i in arr:
		sum = sum + i

	return(sum)

arr = [20, 25, 30, 35]

x = suma(arr)

print('Suma vectorului  este: ', x)
