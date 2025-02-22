class Circle():
    
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print(3.14 * self.radius ** 2)

r = Circle(3)
r.area()
