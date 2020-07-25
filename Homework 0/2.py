def newList1(a_list):
    return [a_list[i] for i in range(len(a_list)) if a_list[i] not in a_list[i + 1::]]


def newList(a_list):
    for elem in a_list:
        print(elem)
        print(a_list)
        while a_list.count(elem) > 1:
            a_list.remove(elem)
    return a_list


a_list = [[1, 2], [1, 2, 3], [1, 3], [1, 2, 3], [1, 2], [1, 3]]
print(newList1(a_list))  # short
# print(newList(a_list)) # sxala ashxatum
