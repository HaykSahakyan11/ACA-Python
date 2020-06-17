from urllib.request import urlopen, Request
from urllib.parse import urlencode
data = {"user_first_name": 'name111', 'user_last_name': "last name 1", "user_gender": "men", "user_age" : 29}
response = urlopen(Request('http://127.0.0.1:8000/create', urlencode(data).encode()))
