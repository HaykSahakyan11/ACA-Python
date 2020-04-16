def implication3(a, b, c):
    return not a or (b and c)


def expr_value1(*args):
    a_list = [args[0][i] for i in range(len(args[0]))]
    return calculation(a_list)


def calculation(b_list):
    func = ["*", "/", "-", "+"]
    for i in range(len(func)):
        if func[i] == "*":
            while "*" in b_list:
                ind = b_list.index("*")
                a, b = b_list[ind - 1], b_list[ind + 1]
                b_list = b_list[:ind - 1] + [float(a) * float(b)] + b_list[ind + 2:]
        print(b_list)
        if func[i] == "/":
            while "/" in b_list:
                ind = b_list.index("/")
                a, b = b_list[ind - 1], b_list[ind + 1]
                b_list = b_list[:ind - 1] + [float(a) / float(b)] + b_list[ind + 2:]
        print(b_list)
        if func[i] == "-":
            while "-" in b_list:
                ind = b_list.index("-")
                a, b = b_list[ind - 1], b_list[ind + 1]
                b_list = b_list[:ind - 1] + [float(a) - float(b)] + b_list[ind + 2:]
        print(b_list)
        if func[i] == "+":
            while "+" in b_list:
                ind = b_list.index("+")
                a, b = b_list[ind - 1], b_list[ind + 1]
                b_list = b_list[:ind - 1] + [float(a) + float(b)] + b_list[ind + 2:]

    return b_list[0]



