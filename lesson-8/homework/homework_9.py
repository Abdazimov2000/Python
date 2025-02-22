with open('log.txt', 'r') as text:
    x = text.read()

y = x.replace('New', 'Old')

with open('log.txt','w') as file:
    file.write(y)
print(y)
