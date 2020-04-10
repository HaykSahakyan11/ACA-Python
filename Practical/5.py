def find_factorial(a_number):
    n = 0
    num = 1
    while num <= a_number:
        n += 1
        num *= n
    return num


a_number = 100
print(find_factorial(a_number))
