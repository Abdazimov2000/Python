class Person():
    def __init__(self, name = 'John', age = 30):
        self.name = name
        self.age = age
    def describe(self):
        print(f"Name: {self.name}\nAge: {self.age}")

x = Person()
x.describe()
y = Person('Bob', 25)
y.describe()
