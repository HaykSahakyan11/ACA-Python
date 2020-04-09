a, b = 10, 15


# comprehension
def max_div(a, b):
    return [i for i in range(min(a, b), 0, -1) if a % i == 0 and b % i == 0][0]


# recursion
def max_divisor(a, b, c=min(a, b)):
    if c == 1:
        return 1
    else:
        if a % c == 0 and b % c == 0:
            return c
        else:
            return max_divisor(a, b, c - 1)


# print(max_div(a, b)) #comprehension
print(max_divisor(a, b))  # recursion
