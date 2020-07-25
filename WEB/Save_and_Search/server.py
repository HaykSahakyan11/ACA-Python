import importlib
from wsgiref.simple_server import make_server
from typing import Iterable
import os
from pathlib import Path
from urllib.parse import parse_qs
import csv
import os.path
import pandas as pd
from flask import  Flask


class HTTPError(Exception):
    def __init__(self, reason, code):
        self.code = code
        self.reason = reason
        super().__init__(reason)


# Updates a database by created data dictionary
# if there is not created database, it creates a new with headers or columns names
# if database has been created , it only updates database
def database_update(data: dict):
    db_is_created = os.path.isfile('database.csv')
    with open('database.csv', mode='a', newline="") as db_file:
        db_writer = csv.writer(db_file, delimiter=',')
        user_first_name = data['user_first_name']
        user_last_name = data['user_last_name']
        user_age = data['user_age']
        user_gender = data['user_gender']

        if not db_is_created:
            f = ["user_first_name", "user_last_name", "user_age", "user_gender"]
            db_writer.writerow(f)
        db_writer.writerow([*user_first_name, *user_last_name, *user_age, *user_gender])


def get_create(env):
    with open(Path("html/create.html"), "rb") as fd:
        return fd.read()


def post_create(env):
    expected_keys = {'user_first_name', 'user_last_name', 'user_gender', 'user_age'}
    payload = env['wsgi.input'].read(int(env['CONTENT_LENGTH']))
    data = parse_qs(payload.decode())
    database_update(data)
    if len(data) != len(expected_keys):
        raise HTTPError('Bad Request', 404)
    for key in expected_keys:
        if key not in data:
            raise HTTPError('Bad Request', 404)
    return get_create(env)


# As I did not know how change, add html data dynamically,
# I use this function to create response in html
# matched_data is pandas dataframe
def __searched_answer_creation(matched_data):
    matched_data = matched_data.reset_index(drop=True)
    answer_headers = """
        <tr>
            <th>First Name</th>
            <th>Last Name</th>
            <th>Age</th>
            <th>Gender</th>
        </tr>
        """
    for answer_body in matched_data.values:
        answer_headers += \
            """<tr>
            <th>{}</th>
            <th>{}</th>
            <th>{}</th>
            <th>{}</th>
        </tr>
        """.format(*answer_body)
    return """<table>{}</table>""".format(answer_headers)


def get_search(env):
    query_string = parse_qs(env['QUERY_STRING'])

    # check whether query is empty or not , in other words subpage is visited only or created a query in this subpage
    if query_string:
        search_param = query_string['search_param'][0]

        # creates pandas dataframe database and extracts new dataframe matched_data
        database = pd.read_csv('database.csv')
        matched_data = database.loc[
            (database['user_first_name'] == search_param) | (database['user_last_name'] == search_param)]

        # if no matches
        if matched_data.empty:
            return "There is not such 'first name' or 'last name' in the database".encode()

        else:
            created_answer = __searched_answer_creation(matched_data)
            return created_answer.encode()

    with open(Path("html/search.html"), "rb") as fd:
        return fd.read()


def post_search(env):
    pass


def not_found(env):
    raise HTTPError("Not Found", 404)


# as there is no need to describe other functions, "not_found" function is used instead of particular functions
ROUTING_TABLE = {
    '/create': {
        'GET': get_create,
        "POST": post_create
    },
    '/search': {
        'GET': get_search,
        'POST': not_found
    }
}


def app(env: dict, start_response: callable) -> Iterable:
    print(env.items())
    route = env['PATH_INFO']
    method = env['REQUEST_METHOD']
    try:
        handler = ROUTING_TABLE.get(route, {}).get(method, not_found)
        response = handler(env)
        start_response('200 OK', [('Content-type', 'text/html')])
        return [response]
    except HTTPError as herr:
        start_response(f'{herr.code} {herr.reason}', [('Content-type', 'text/html')])
        return [f'<h2>{herr.code}{herr.reason}</h2>'.encode()]


if __name__ == "__main__":
    with make_server("", 8000, app) as httpd:
        print("Serving on port 8000")
        httpd.serve_forever()
