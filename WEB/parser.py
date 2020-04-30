from collections import defaultdict


def parse_ini(config_path="config.ini"):
    d = defaultdict(dict)
    with open(config_path, "r") as ini:
        section = None
        for num_line, line in enumerate(ini, 1):
            if line != "":
                line = line.strip()
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