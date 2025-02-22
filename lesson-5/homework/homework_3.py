letter = input('Inseert a letter: ')
x = ['a', 'e', 'i', 'o', 'u']
if len(letter) != 1:
    print('You did not insert a letter.')
else:
    if letter in x:
        print(f"Your letter {letter} is vowel.")
    else:
        print(f"Your letter {letter} is consonant.")
