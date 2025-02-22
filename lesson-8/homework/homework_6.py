with open('numbers.txt', 'w+') as num:
    for x in range(1, 6):
        num.write(f"{x}\n")
    num.seek(0)
    y = num.read()
    print(y)
