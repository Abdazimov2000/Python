def factorial(n):
    y = 1
    for x in range(1, n+1):
        y = y * x
    print(y)
number = int(input('Enter number: '))
factorial(number)
