class Car():
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    def describe(self):
        long_name = f"{self.brand}, {self.year}"
        return long_name
my_car = Car('Tesla', 2025)
print(my_car.describe())
