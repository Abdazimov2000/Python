def merge_list(*lists):
    y = []
    for x in lists:
        y = y + x
    print(y)
ls = [1, 2, 3, 4]
ls_2 = ['a', 'b', 'c']
merge_list(ls, ls_2)
