print('3 ta son kiriting va men sizga eng kattasini topib beraman.')
x = int(input('Birinchi son: '))
y = int(input('Ikkinchi son: '))
z = int(input('Ikkinchi son: '))
if x > y and x > z:
    print(f"Eng katta son {x}.")
elif y > z and y > x:
    print(f"Eng katta son {y}.")
else:
    print(f"Eng katta son {z}.")
