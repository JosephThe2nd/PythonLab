import datetime
import math

ThisList = ["Apple", "Pear", "Orange", "Cherry"]
print(ThisList)
ThisList.append("Grapes")
for i in range(len(ThisList)):
    print(ThisList[i])


ThisList.sort()
print(ThisList)
ThisList.reverse()
print(ThisList)

ThisList.pop(1)
print(ThisList)

#date
x = datetime.datetime.now()
print(x)
print(x.year)

print("Azi suntem in data de:", x.strftime("%d"), x.strftime("%B"), x.strftime("%Y"), "intr-o zi de", x.strftime("%A"))

x = math.pi
print(x)
