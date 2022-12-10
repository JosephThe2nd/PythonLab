# Functie pt al n-lea numar din sirul lui Fibonacci recursiv
def Fibonacci(n):
	if n <= 0:
		print("Incorrect input")
	# Primul numar din sir este 0
	elif n == 1:
		return 0
	# Al 2 lea numbar din sir este 1
	elif n == 2:
		return 1
	else:
		return Fibonacci(n-1)+Fibonacci(n-2)

