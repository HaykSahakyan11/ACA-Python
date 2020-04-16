def maxSecNumber(a_list):
    max1, max2 = float('-inf'), float('-inf')
    for i in a_list:
        if max2 < i and max1 != i:
            if max1 < i:
                max1, max2 = i, max1
            else:
                max2 = i
    return 0.5 if max2 == float('-inf') or max1 == max2 else max2


############################################################################

def maximumNumber(a_list,maxnum = None):
    for i in range(len(a_list)):
        if  maxnum == None or a_list[i] > maxnum:
            maxnum = a_list[i]
    return maxnum

def maxSeconNumWithSet(a_list):
    a_list = list(set(a_list))
    if len(a_list) < 2:
        return 0.5
    maxnum1 = maximumNumber(a_list)
    a_list.remove(maxnum1)
    return maximumNumber(a_list)





a_list = [5, 5, 1, 4, 5]
#print(maxSecNumber(a_list))
print(maxSeconNumWithSet(a_list))
