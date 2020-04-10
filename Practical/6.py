def str1BYstr2(string1, string2):
    kk = {}
    for char in string1:
        if char not in kk:
            kk[char] = (string2.index(char), 1)
        else:
            kk[char] = (kk[char][0], kk[char][1] + 1)
    finnalStr = str()
    for key, value in sorted(kk.items(), key=lambda x: (x[1][0])):
        finnalStr = finnalStr + key * value[1]
    return finnalStr


string1 = "abaabbccabbed"
string2 = "bedac"
print(str1BYstr2(string1, string2))
