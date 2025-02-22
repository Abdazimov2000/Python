class Rectangle():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        print(self.a * self.b)

    def perimeter(self):
        print(2 * (self.a + self.b))

x = Rectangle(5, 4)
x.area()
x.perimeter()
