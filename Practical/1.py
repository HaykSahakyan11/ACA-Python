def vowelIndex(a_string):
    vowels = ["a", "u", "i", "o", "e"]
    index_vowels = []
    for i in range(len(a_string)):
        if a_string[i] in vowels:
            index_vowels.append(i)
    return index_vowels


def reverseVowels(a_string):
    vowelInd = vowelIndex(a_string)
    new_string = str()
    for i in range(len(a_string)):
        if i in vowelInd:
            new_string = new_string + a_string[vowelInd[len(vowelInd) - vowelInd.index(i) - 1]]
        else:
            new_string = new_string + a_string[i]
    return new_string


a_string = "aecu"
print(reverseVowels(a_string))
