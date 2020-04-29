import socket
from datetime import datetime
from collections import defaultdict


def parse_ini(config_path="config.ini"):
    d = defaultdict(dict)
    with open(config_path, "r") as ini:
        section = None
        for num_line, line in enumerate(ini, 1):
            line = line.strip()
            if line != "":
                if line.startswith("["):
                    if line.endswith("]") and line.count("[") == line.count("]"):
                        section = line.strip()[1:-1]
                    else:
                        return "Something wrong with brackets in {} line".format(line)
                else:
                    if section == None:
                        return "File contains no section headers"
                    else:
                        line = line.replace(" ", "")
                        try:
                            a = line[line.index("=") + 1:]
                            try:
                                if float(a).is_integer():
                                    a = int(a)
                            except:
                                pass
                            d[section][line[:line.index("=")]] = a
                        except:
                            return "There is not '=' in the {} line {} section".format(line, section)
        return dict(d)


now = datetime.now()
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    config = parse_ini()
    sock.bind((config["inet"]["ip"], config["inet"]["port"]))
    sock.listen(5)
    print("Accepting data")
    conn, addr = sock.accept()
    with conn:
        print("Connected by", addr)
        while True:
            data = conn.recv(1024)
            data = data.decode("utf-8")
            input_dict = {"exit": "Goodbye", "day": "%d", "month": "%m", "year": "%Y", "time": "%H:%M"}
            if data in input_dict:
                conn.sendall(now.strftime("{}".format(input_dict[data])).encode("utf-8"))
            else:
                conn.sendall("Unrecognized command {}".format(data).encode("utf-8"))
