def factorial(a_number):
    return 1 if a_number == 1 or a_number == 0 else a_number * factorial(a_number - 1)



def fac_For_loop(a_number):
    factor = 1
    for i in range(1,a_number+1):
        factor *= i
    return factor

print(factorial(3))
print(fac_For_loop(3))


