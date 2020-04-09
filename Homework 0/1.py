# list comprehension
a_list = [[1, 2], [1, 2, 3], [1, 2]]
del_num = [1, 2]
listComprehension = [elem for elem in a_list if elem != del_num]
print(listComprehension)

##remove method
# def createNewList(a_list,del_num):
#    while del_num in a_list:
#        a_list.remove(del_num)
#    return a_list
# print(createNewList(a_list,del_num))
