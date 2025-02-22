class DogA():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def describe(self):
        if self.age > 1:
            print(f"{self.name} is {self.age} years old")
        else:
            print(f"{self.name} is {self.age} year old")

    def run(self):
        print(f"{self.name} is running right now!")

class DogB(DogA):
    def __init__(self, name, age):
        super().__init__(name, age)

    def bark(self):
        print(f"{self.name} is barking!")

    def roll_over(self):
        print(f"{self.name} rolled over!")

class DogC(DogB):
    def __init__(self, name, age):
        super().__init__(name, age)

    def sit(self):
        print(f"{self.name} is sitting right now!")

dog = DogC("Bo'bik", 2)

dog.describe()

dog.run()

dog.bark()

dog.roll_over()

dog.sit()
