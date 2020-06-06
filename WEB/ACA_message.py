from urllib.request import urlopen


def get_nth_line(resp, n):
    i = 1
    while i < n:
        resp.readline()
        i += 1
    return resp.readline().decode()


def message_converter(url, line):
    with urlopen(url) as response:
        message_binary = get_nth_line(response, line)
    message_binary_split = message_binary.split()
    message = list(map(lambda x: chr(int(x, 2)), message_binary_split))
    return "".join(message)


if __name__ == "__main__":
    url = "https://aca.am/en/index.html"
    line = 4
    print(message_converter(url, line))

