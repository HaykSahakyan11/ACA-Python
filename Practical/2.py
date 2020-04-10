def charMatching(a_list):
    dict_1 = creating_dictionary(a_list)
    if dict_1:
        main_tuple = ()
        a_tuple = ()
        for value in dict_1[0].keys():
            for key in dict_1:
                if value not in dict_1[key]:
                    a_tuple = a_tuple + (0,)
                else:
                    a_tuple = a_tuple + (dict_1[key][value],)
            main_tuple = main_tuple + (min(a_tuple),)
            a_tuple = ()
        return (sum(main_tuple))
    else:
        return 0


def creating_dictionary(a_list):
    dict_1 = {}
    for i in range(len(a_list)):
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
    return dict_1


print(charMatching(["cba", "cba", "cab"]))
