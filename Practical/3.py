def unicElem(int_list):
    for elem in list(map(str, int_list)):
        if len(elem) == len(set(elem)):
            return elem
    return -1


print(unicElem([101, 110, 220, 100, 103, 606, 603]))
