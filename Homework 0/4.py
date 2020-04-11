def sumDigits(a_number):
    return sum(list(map(int, str(a_number))))


a_number = 1005
print(sumDigits(a_number))
