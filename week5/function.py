from fib import Fibonacci

i = 1
while i <= 10 :
    print(Fibonacci(i))
    i += 1
    

#parametru default age = 18
def printinfo (name, age = 18):
    print ("Name:", name)
    print ("Age:", age)
    return
printinfo(name = "Mihai")
printinfo(name = "Iosif", age = 21)

#Anonymous functions
prod = lambda arg1, arg2: arg1 * arg2;
x = int(input("x = "))
y = int(input("y = "))
print("x * y este: ", prod(x,y)) 

