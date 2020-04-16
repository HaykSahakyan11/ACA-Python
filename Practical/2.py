def charMatching(a_list): # same character multiple times
    dict_1 = creating_dictionary(a_list)
    # checks dictionary is empty or not
    if dict_1:
        # main_tuple elements show overall minimum count of matched characters
        main_tuple = ()
        # a_tuple elements show how many matching of corresponding character we have checking all elements in a_list
        a_tuple = ()
        # values in dict_1[0].keys() are characters in original a_list at index 0
        # keys in dict_1 are indices of elements in a_list
        # going from value in dict_1[0].keys() and than from key in dict_1 we check if character is in dict_1[key]
        # if it is not, we add 0 in a_tuple or if it is, we add count of character (dict_1[key][value],) in a_tuple
        # after each loop in the main for loop we gives minimum number of matching to main_tuple and so on for other
        # characters
        for value in dict_1[0].keys():
            for key in dict_1:
                if value not in dict_1[key]:
                    a_tuple = a_tuple + (0,)
                else:
                    a_tuple = a_tuple + (dict_1[key][value],)
            main_tuple = main_tuple + (min(a_tuple),)
            a_tuple = ()
        return (sum(main_tuple))
    # if dictionary is empty
    else:
        return 0


def creating_dictionary(a_list):
    # Function creates dictionary where keys are indices of elements in a_list,
    # (a_list = ["aba", "aaa", "aab"], a_list[0] = "aba", key = 0,1,2 and so on)
    # each key has a value which is also dictionary where keys are characters of corresponding indexed element of a_list
    # and values for this keys are counts of corresponding character
    # {0: {'a': 2, 'b': 1}, 1: {'a': 3}, 2: {'a': 2, 'b': 1}}
    dict_1 = {}
    # for each element in a list
    for i in range(len(a_list)):
        # For each element in elements of a list
        for j in range(len(a_list[i])):
            if i not in dict_1:
                dict_1[i] = {}
                if a_list[i][j] not in dict_1[i]:
                    dict_1[i][a_list[i][j]] = 1
                else:
                    dict_1[i][a_list[i][j]] += 1
            else:
                if a_list[i][j] not in dict_1[i]:
                    dict_1[i][a_list[i][j]] = 1
                else:
                    dict_1[i][a_list[i][j]] += 1
    # returns created dictionary  {0: {'a': 2, 'b': 1}, 1: {'a': 3}, 2: {'a': 2, 'b': 1}}
    return dict_1


def matchedChars(a_list):
    simplified_list = list(set([elem for elem in a_list][0]))
    count_in_list, count_in_elem = 0, 0
    for elem in simplified_list:
        for i in range(1, len(a_list)):
            if elem not in a_list[i]:
                break
            else:
                count_in_elem += 1
        count_in_list += count_in_elem // (len(a_list) - 1)
        count_in_elem = 0
    return count_in_list


a_list = ["cbaabababa", "abaabababa", "ababababab"]
print(charMatching(["aba", "aaa", "aab"])) # same character multiple times
print(matchedChars(a_list)) # same character one time
