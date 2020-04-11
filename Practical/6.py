def str1BYstr2(string1, string2):
    kk = {}
    # goes over all characters in a string1 to create a dictionary
    # where keys are characters of string1 , values are tuples,
    # where tuple[0] is index of character(string1) in string2,
    # tuple[1] count of character in string2
    for char in string1:
        if char not in kk:
            kk[char] = (string2.index(char), 1)
        else:
            kk[char] = (kk[char][0], kk[char][1] + 1)
    print(kk)
    finnalStr = str()
    # create final string, sorts by index of character(string1) in string2
    for key, value in sorted(kk.items(), key=lambda x: (x[1][0])):
        finnalStr = finnalStr + key * value[1]
    return finnalStr


string1 = "abaabbccabbed"
string2 = "bedac"
print(str1BYstr2(string1, string2))
