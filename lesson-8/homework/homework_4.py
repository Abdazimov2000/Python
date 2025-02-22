with open('test.txt', 'w+') as text:
    text.write('Python is fun!')
    text.seek(0)
    x = text.read()
    print(x)
