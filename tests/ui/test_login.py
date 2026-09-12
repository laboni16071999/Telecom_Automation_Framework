import pytest


from PageObject.login_page import LoginPage
from PageObject.dashboard_page import DashboardPage
from utils.read_json import read_login_data


# Read all test data from JSON file
login_data = read_login_data()


@pytest.mark.parametrize("data", login_data)
def test_login(page, data):

    # Create Login Page object
    login_page = LoginPage(page)

    # Create meaningful test IDs
    
    test_data = [
        pytest.param(data, id=data["test_case"])
        for data in login_data
    ]

    # Perform login using data from JSON
    login_page.login(
        data["username"],
        data["password"]
    )

    # Validate expected result
    if data["expected_result"] == "success":

        # Create Dashboard Page object
        dashboard_page = DashboardPage(page)

        # Validate successful login
        assert dashboard_page.get_products_title() == data["expected_message"]

    else:

        # Validate error message for failed login
        assert login_page.get_error_message() == data["expected_message"]