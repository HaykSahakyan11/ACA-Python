a, b = 10, 15


def euclid_algo(a, b):
    a, b = (a - b, b) if a > b else (a, b - a)
    return euclid_algo(a, b) if a != b else a


# more effective than euclid_algorithm
def m_div(a, b):
    if b > 0: a, b = b, a % b
    return m_div(a, b) if b > 0 else a


# comprehension
def max_div(a, b):
    return [i for i in range(min(a, b), 0, -1) if a % i == 0 and b % i == 0][0]


# print(max_div(a, b)) #comprehension
# print(euclid_algo(a, b))
print(m_div(a, b))
