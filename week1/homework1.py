def all_positive(*args):
    new_nums = list(filter(lambda x: x < 0, args))
    for i in new_nums:
        return True
    return False


"""Version 2"""


# def all_positive(*args):
#    return len(list(filter(lambda x: x < 0, args))) and True

def xor3(*args):
    a, b, c = args
    return [False, True][not (a and b) and (a or b)]


def discriminant(a, b, c):
    g = lambda a, b, c: (b ** 2 - 4 * a * c)
    return g(a, b, c)

"""Version 2"""
#discriminant = lambda a,b,c:(b ** 2 - 4 * a * c)


def mirror_string(a_string):
    newstring = str()
    for elem in a_string:
        a = ord(elem)
        if 65 <= a <= 90:
            newstring = f"{newstring}{chr(90 - a + 65)}"
        elif 97 <= a <= 122:
            newstring = f"{newstring}{chr(122 - a + 97)}"
        else:
            newstring = f"{newstring}{chr(a)}"
    return newstring


def bit_concat(a_list):
    new_list = []
    for i in range(len(a_list)):
        start, stop = 6 - i * 2, 8 - i * 2
        new_list.append(("{:08b}".format(a_list[i]))[start:stop])
    return int("".join(new_list[::-1]), 2)


# def bit_concat(a_list):
#    return int("".join([("{:08b}".format(a_list[i]))[6 - i * 2:8 - i * 2] for i in range(len(a_list))][::-1]), 2)


def binary_sum(str1, str2):
    return int(str1, 2) + int(str2, 2)
