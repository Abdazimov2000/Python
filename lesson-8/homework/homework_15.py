file_name = 'class.txt'
try:
    with open(file_name, 'r') as text:
        x = text.read()
        print(x)
except FileNotFoundError:
    print(f"There is not file named {file_name}.")
