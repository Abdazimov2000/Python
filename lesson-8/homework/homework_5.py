with open('log.txt', 'a+') as text:
    text.write('New data')
    text.seek(0)
    x = text.read()
    print(x)
