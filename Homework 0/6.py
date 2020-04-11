a, b = 10, 15


# comprehension
def max_div(a, b):
    return [i for i in range(min(a, b), 0, -1) if a % i == 0 and b % i == 0][0]


# recursion
def max_divisor(a, b):
    if b > 0:
        a, b = b, a % b
        return max_divisor(a, b)
    return a


# same as above function but gives error
def n_div(a, b):
    return n_div(lambda a, b: b, a % b) if b > 0 else a


# print(max_div(a, b)) #comprehension
print(max_divisor(a, b))  # recursion
