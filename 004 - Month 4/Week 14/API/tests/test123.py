import requests

files = {
    'username': (None, 'test5555@gmail.com'),
    'password': (None, '123456'),
}

response = requests.post('http://127.0.0.1:8000/login', files=files)
