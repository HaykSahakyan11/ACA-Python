import json


def json_to_xml(path):
    with open(path, "r") as js_file:
        decoded_json = json.load(js_file)
    xml = []
    for i in range(len(decoded_json)):
        xml.append("<{}>".format(i))
        for key, value in decoded_json[i].items():
            xml.append("<{0}>{1}</{0}>".format(key, value))
        xml.append("</{}>".format(i))
    return "\n".join(xml)


print(json_to_xml("storage.json"))
