def factorial(a_number):
    return 1 if a_number == 1 or a_number == 0 else a_number * factorial(a_number - 1)


print(factorial(5))
