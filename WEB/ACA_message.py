from urllib.request import urlopen


def message_converter(url, line):
    # with urlopen(url) as response:
    with open(url, "r") as response:
        data_of_line = response.readlines()
        message_binary = data_of_line[line]
    message_binary_split = message_binary.split()
    message = list(map(lambda x: chr(int(x, 2)), message_binary_split))
    return "".join(message)


if __name__ == "__main__":
    # url = "https://aca.am/en/index.html"
    url = "response.html"
    line = 3
    print(message_converter(url, line))
