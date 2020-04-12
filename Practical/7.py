def isCircle(list1, list2):
    step = list2.index(list1[0])
    if step < 0:
        step = abs(step)
        for i in range(step):
            list1.append(list1.pop(0))
    else:
        for i in range(step):
            list1.insert(0, list1.pop())
    print(list1, list2)
    return list1 == list2


list1, list2 = [1, 2, 3], [3, 2, 1]
print(isCircle(list1, list2))
