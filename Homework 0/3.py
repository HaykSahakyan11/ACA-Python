a_string = "ada"
print("False" if len([True for i in range(len(a_string) // 2) if a_string[i] == a_string[-1 - i]]) < len(
    a_string) // 2 else "True")
