def newList(a_list):
    for elem in a_list:
        while a_list.count(elem) > 1:
            a_list.remove(elem)
    return a_list


a_list = [[1, 2], [1, 2], [1, 2, 3]]
print(newList(a_list))
