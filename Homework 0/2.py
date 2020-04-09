a_list = [[1, 2], [1, 2], [1, 2, 3]]
new_list = []
[new_list.append(elem) for elem in a_list if elem not in new_list]
print(new_list)
