
class complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return self.a + other.a,  self.b + other.b

    def __sub__(self, other):
        return self.a - other.a, self.b - other.b

    def __mul__(self, other):
        return (self.a * other.a) - (self.b * other.b), (self.a * other.b) + (self.b * other.a)
  
    

Ob1 = complex(1, 2)
Ob2 = complex(2, 3)
Ob3 = Ob1 + Ob2
Ob4 = Ob1 - Ob2
Ob5 = Ob1 * Ob2
print("Suma:", Ob3)
print("Diferența:", Ob4)
print("Produs:", Ob5)



