try:
    openf = open("textfile.txt", "w+")
    openf.write("Text pentru exemplu. \nAlt text pentru exemplu")
except IOError:
    print("Error: can't find the file or write the data")
else: print("The content was written successfully")

openf.close()

try:
    openf = open("textfile.txt", "r+")
    str = openf.read()
    print(str) 
except IOError:
    print("Error: can't find the file or read the data")
else: print("The content was read successfully") 

openf.close()
'''
print ("Name of the file: ", openf.name)
print ("Closed or not: ", openf.closed)
print("Opening mode: ", openf.mode)
print("")
'''