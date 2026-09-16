import json


def read_login_data():
    with open("test_data/login_data.json", "r") as file:
        return json.load(file)


def get_valid_login_data():
    login_data = read_login_data()

    for result in login_data:
        if result["expected_result"] == "pass":
            return result

    raise ValueError("Valid login data not found in login_data.json")


def read_checkout_data():
    with open("test_data/checkout_data.json", "r") as file:
        return json.load(file)