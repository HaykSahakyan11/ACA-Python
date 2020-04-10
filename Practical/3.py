def unicElem(int_list):
    a = [elem for elem in list(map(str, int_list)) if len(elem) == len({i for i in list(elem)})]
    return a[0] if a else -1


int_list = [101, 110, 220, 100, 103, 606, 603]
print(unicElem(int_list))
