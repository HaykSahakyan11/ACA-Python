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
                if line.startswith("[") and line.endswith("]"):
                    section = line[1:-1]
                else:
                    if section == None:
                        raise ValueError("File contains no section headers")
                    else:
                        try:
                            key, value = (line[:line.index("=")]).strip(), (line[line.index("=") + 1:]).strip()
                            try:
                                if float(value).is_integer():
                                    value = int(value)
                            except:
                                pass
                            d[section][key] = value
                        except ValueError as error:
                            return "ValueError: '=' {} in the {} line {} section".format(error, line, section)
        return dict(d)



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
                now = datetime.now()
                conn.sendall(now.strftime("{}".format(input_dict[data])).encode("utf-8"))
                if data == "exit":
                    print("Disconnected")
                    break
            else:
                conn.sendall("Unrecognized command {}".format(data).encode("utf-8"))
