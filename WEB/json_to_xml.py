import json
with open("storage.json","r") as js_file:
    decoded_json = json.load(js_file)

xml = []
for i in range(len(decoded_json)):
    for key, value in decoded_json[i].items():
        xml.append("<{0}>{1}</{0}>".format(key,value))

print(xml)