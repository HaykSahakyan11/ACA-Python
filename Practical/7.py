def isCircleShifted(list1, list2):
    if set(list1) != set(list2):
        return False
    # Function gives True  if all elements in list1 shifted by same number or step otherwise False
    # Assumes if there is a pattern of moving (step),
    # we can find it by taking 1st elem (index [0]) in list1 and checking what happens with it in list2 (list2.index(list1[0])).
    # And if we shift all elements of list1 by same step and get that shifted list1 is equal to list2 return True
    step = list2.index(list1[0])
    for i in range(step):
        list1.insert(0, list1.pop())
    return list1 == list2


list1, list2 = [1, 3, 4, 5, 2], [5, 2, 1, 3, 4]
print(isCircleShifted(list1, list2))
