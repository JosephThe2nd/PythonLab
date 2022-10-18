#program simplu pentru verificare numar prim
n = 13

if n > 1:
	
	for i in range(2, int(n/2)+1):
		
		
		if (n % i) == 0:
			print(n, " nu este numar prim")
			break
	else:
		print(n, "este numar prim")
else:
	print(n, "nu este numar prim")
