class Persoane(object):
    def __init__(self,name):
        self.name = name
    
    def getName(self):
        return self.name

    def isEmployee(self):
        return False
    def isManager(self):
        return False
    
class Angajati(Persoane):
    def getName(self):
        return self.name

    def isEmployee(self):
        return True
    def isManager(self):
        return False

class Manager(Persoane):
    def getName(self):
        return self.name

    def isEmployee(self):
        return True

    def isManager(self):
        return True


pers1 = Persoane("Covasan Iosif") 
print(pers1.getName(), pers1.isEmployee(), pers1.isManager())

pers2 = Angajati("Popescu Marian") 
print(pers2.getName(), pers2.isEmployee(), pers2.isManager())

pers3 = Manager("Suciu Andrei")
print(pers3.getName(), pers3.isEmployee(), pers3.isManager())

pers4 = Manager("Anghel Mihai")
print(pers4.getName(), pers4.isEmployee(), pers4.isManager())

