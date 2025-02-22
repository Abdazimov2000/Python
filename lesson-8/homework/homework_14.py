try:
    x = int(input('Enter Number: '))
    if x > 0:
        print(x)
except Exception:
    print('You cannot enter a negative number.')
