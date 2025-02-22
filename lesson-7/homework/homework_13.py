def countdown(n):
    if n == 1:
        print(1)
    else:
        print(n)
        countdown(n-1)
countdown(5)
