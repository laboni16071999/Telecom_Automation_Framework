import json


def read_login_data():
    with open("test_data/login_data.json", "r") as file:
        return json.load(file)