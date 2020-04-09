def sum2(a_number, sum_number=0):
    if a_number == 1:
        return sum_number + 1
    if a_number % 2 == 1:
        sum_number += 1
    return sum2(a_number // 2, sum_number)


a_number = 264
print(sum2(a_number))
