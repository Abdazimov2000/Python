def cal():
    ls = []
    while True:
        number = input("Enter numbers or 's' to see sum of numbers: ")
        if number == 's':
            break
        else:
            ls.append(int(number))
    print(sum(ls))
cal()
