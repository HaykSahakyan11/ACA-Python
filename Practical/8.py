def maxSecNumber(a_list):
    max1, max2 = float('-inf'), float('-inf')
    for i in a_list:
        if max2 < i and max1 != i:
            if max1 < i:
                max1, max2 = i, max1
            else:
                max2 = i
    return 0.5 if max2 == float('-inf') or max1 == max2 else max2


a_list = [5, 5, 1, 4, 5]
print(maxSecNumber(a_list))
