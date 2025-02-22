def reverse_str(s: str)->str:
    ls = []
    for x in s:
        ls.insert(0, x)
    print(''.join(ls))
reverse_str('Asadbek')
