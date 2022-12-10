import sqlite3

connection = sqlite3.connect('mydata.db') #creating the database
cursor = connection.cursor() #defining a cursor

#Create the table Persons if doesn't already exists
cursor.execute("""   
CREATE TABLE IF NOT EXISTS Persons(
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name, TEXT
    age INTEGER
)
""")
connection.commit()

class Person():
    def __init__(self, id_number=-1, first='', last='', age=-1):
        self.id_number = id_number
        self.first = first
        self.last = last
        self.age = age
        self.connection = sqlite3.connect('mydata.db') #creating the database
        self.cursor = self.connection.cursor() #defining a cursor

    def load_person(self, id_number):
        self.cursor.execute("""
        SELECT * FROM Persons
        WHERE id = {}
        """.format(id_number))

        results =  self.cursor.fetchone()

        self.id_number = id_number
        self.first = results[1]
        self.last = results[2]
        self.age = results[3]

    def insert_person(self):
        self.cursor.execute("""
        INSERT INTO Persons VALUES
        ({}, "{}", "{}", {})
        """.format(self.id_number, self.first, self.last, self.age))
        self.connection.commit()
        self.connection.close()

# p1 = Person(1, "Alex", "Smith", 21)
# p1.insert_person()
# p2 = Person(2, "Andrei", "Johnson", 22)
# p2.insert_person()
# p3 = Person(3, "Johny", "Cage", 37)
# p3.insert_person()

p1_load = Person()
p2_load = Person()
p1_load.load_person(1)
p2_load.load_person(2) #the id of the person
print(p1_load.first) #the column of the person

print(f"The ID number: {p1_load.id_number} \nThe first name of the person: {p1_load.first} \nThe last name of the person: {p1_load.last} \nThe age of the person: {p1_load.age}\n")
print(f"The ID number: {p2_load.id_number} \nThe first name of the person: {p2_load.first} \nThe last name of the person: {p2_load.last} \nThe age of the person: {p2_load.age}\n")

cursor.execute("SELECT * FROM Persons")
results = cursor.fetchall()
print(results)

connection.commit()
connection.close()