import json


def problem_1(dictionary, indent=4):
    assert type(dictionary) == dict, "Data must be dictionary!"
    return json.dumps(dictionary, sort_keys=True, indent=indent)


def problem_2(key_searched, json_data):
    dictionary = json.loads(json_data)
    return find(key_searched, dictionary)


def find(key_searched, dictionary: dict, answer=[]):
    for key, value in dictionary.items():
        if key == key_searched:
            answer.append(dictionary[key])
        else:
            if isinstance(value, dict):
                answer = find(key_searched, value)
            elif isinstance(value, list):
                for elem in value:
                    answer = find(key_searched, elem)
    return ["'{}' not found ".format(key_searched), answer][answer != 0]


import pickle


def problem_3(obj: object, path="class_pickle.pkl"):
    with open(path, "wb") as pickle_file:
        pickle.dump(obj, pickle_file)


def problem_4(A_Class: type, json_data: json) -> object:
    return A_Class(**json.loads(json_data))


import xml.etree.ElementTree as ET


# Without "return", only prints
def problem_5(path="movies.xml"):
    tree = ET.parse(path)
    root = tree.getroot()
    for child in root:
        print("{} {} {}".format(root.tag, child.tag, child.attrib))


def problem_6(path="movies.xml"):
    tree = ET.parse(path)
    root = tree.getroot()
    return [child.tag for child in root.iter()]


def problem_7():
    tree = ET.parse("movies.xml")
    root = tree.getroot()
    return [movie.attrib for movie in root.findall(".//year/../[year='1992']")]

    # filter_obj_data = filter(lambda x: int(x.text) == 1992, root.iter("year"))
    # return [root.find(".//{}/..".format(i.tag)).attrib for i in filter_obj_data]


def problem_8():
    tree = ET.parse("movies.xml")
    root = tree.getroot()
    searched_attrib = "multiple"
    searched_attrib_answer = "Yes"
    return [movie.attrib for movie in
            root.findall(".//format/[@{}='{}']..".format(searched_attrib, searched_attrib_answer))]


def problem_9():
    tree = ET.parse("movies.xml")
    root = tree.getroot()
    searched_attrib = "title"
    searched_attrib_answer = "Back 2 the Future"
    target_answer = "Back to the Future"
    for elem in root.findall(".//movie/[@{}='{}']".format(searched_attrib, searched_attrib_answer)):
        elem.attrib[searched_attrib] = target_answer
    return tree.write("updated_movies_1.xml")


def problem_10():
    tree = ET.parse("movies.xml")
    root = tree.getroot()
    searched_attrib = "multiple"
    for elem in root.findall(".//format"):
        elem.attrib[searched_attrib] = ["No", "Yes"][len(elem.text.split(",")) > 1]
    return tree.write("updated_movies_2.xml")



def validation_dec_year_movie_year(tree):
    root = tree.getroot()
    for genre in root.findall(".//genre"):
        for dec in genre.findall(".//decade"):
            for movie in dec.findall(".//movie"):
                for year in movie.findall(".//year"):
                    dec_year_num = int(dec.attrib["years"][:-1])
                    movie_year_num = int(year.text)
                    delta = movie_year_num - dec_year_num
                    if delta > 9 or delta < 0:
                        new_dec_year = "{}s".format(movie_year_num - delta % 10)
                        x = root.find(".//decade/[@years ='{}']".format(new_dec_year))
                        if x:
                            x.insert(0,movie)
                        else:
                            new_tag = ET.SubElement(genre, "decade", attrib={"years": new_dec_year})
                            new_tag.append(movie)
                        dec.remove(movie)
                        return validation_dec_year_movie_year(tree)
    return tree



def problem_11():
    tree = ET.parse("movies.xml")
    tree = validation_dec_year_movie_year(tree)
    return tree.write("updated_movies_3.xml")
