#scrierea intr-un fisier(append)
f = open("emptyfile.txt","a")
f.write(" Acest text va aparea in continuarea textului existent")
f.close()

f = open ("emptyfile.txt", "r")
print(f.read())