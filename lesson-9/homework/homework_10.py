class EvenNumbers():
    def __init__(self, number):
        self.number = number

    def generate_even(self):
        for x in range(1, self.number+1):
            if x % 2 == 0:
                print(x)

number = EvenNumbers(10)
number.generate_even()
