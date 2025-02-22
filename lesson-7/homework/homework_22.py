def count_vowels(s: str)->str:
    ls = ['a', 'e', 'i', 'u', 'o']
    ls_2 = []
    for x in s:
        if x.lower() in ls:
            ls_2.append(x)
    y = len(ls_2)
    print(y)
count_vowels('Asadbek')
