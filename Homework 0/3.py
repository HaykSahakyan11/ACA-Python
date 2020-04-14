def is_simmetric(a_string):
    for i in range(len(a_string) // 2):
        if a_string[i] != a_string[-1 - i]:
            return False
    return True


a_string = "ada"
print(is_simmetric(a_string))
# print("Yes" if a_string == a_string[::-1] else "No")
