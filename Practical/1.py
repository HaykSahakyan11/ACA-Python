def vowelIndex(a_string):
    vowels = ["a", "u", "i", "o", "e", "A", "U", "I", "O", "E", ]
    index_vowels = []
    # tries to find vowels indices in a_string
    for i in range(len(a_string)):
        if a_string[i] in vowels:
            index_vowels.append(i)
    return index_vowels  # a list with vowels indices


def reverseVowels(a_string):
    vowelInd = vowelIndex(a_string)
    new_string = str()
    # as we know where are vowels (their indices), we can mutate
    # i is char in a string
    for i in range(len(a_string)):
        # if is vowel
        if i in vowelInd:
            new_string = new_string + a_string[vowelInd[len(vowelInd) - vowelInd.index(i) - 1]]
        # if i is not vowel
        else:
            new_string = new_string + a_string[i]
    return new_string


print(reverseVowels("aecu"))
