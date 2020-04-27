from collections import defaultdict


def bisect_position(a_list, num):
    middle = len(a_list) // 2
    if len(a_list) == 0:
        return 0
    if len(a_list) == 1:
        return 1 if num > a_list[0] else 0
    if num > a_list[middle]:
        return middle + 1 + bisect_position(a_list[middle + 1:], num)
    else:
        return bisect_position(a_list[:middle], num)


def all_sum(num):
    # a_list = []
    # for i in range(1, num // 2 + 1):
    #    a_list.append((i, num - i))
    # return a_list
    return [(i, num - i) for i in range(1, num // 2 + 1)]


def duplicate_characters(a_string):
    a_set = set()
    data = defaultdict(int)
    for char in a_string.replace(" ", ""):
        data[char[0]] += 1
        if data[char] > 1:
            a_set.add(char)
    return a_set


def compare_lists(list1, list2):
    set1, set2 = set(list1), set(list2)
    if set1 != set2:
        return False
    for i in set1:
        if list1.count(i) != list2.count(i):
            return False
    return True


def heapq(a_list, num, is_new=True):
    if is_new:  # to check the function is called 1st time or it is recursive called
        a_list.append(num)
        num_ind = len(a_list) - 1
    else:
        num_ind = a_list.index(num)
    parent_num_ind = (num_ind - 1) // 2
    parent_num = a_list[parent_num_ind]
    if num_ind > 0 and parent_num > a_list[num_ind]:
        a_list[parent_num_ind], a_list[num_ind] = a_list[num_ind], a_list[parent_num_ind]
        heapq(a_list, num, False)
    return a_list


def sort_list(a_list, type="ascending"):
    if type == "descending":
        return sort_alg(a_list)[::-1]
    else:
        return sort_alg(a_list)


def sort_alg(a_list):
    if len(a_list) <= 1:
        return a_list
    else:
        mid = len(a_list) // 2
        left = sort_alg(a_list[:mid])
        right = sort_alg(a_list[mid:])
        new_list = []
        while len(left) and len(right) > 0:
            if left[0] < right[0]:
                new_list.append(left.pop(0))
            else:
                new_list.append(right.pop(0))
        new_list.extend(left)
        new_list.extend(right)
        return new_list
