import pytest

from PageObject.login_page import LoginPage
from PageObject.products_page import ProductsPage
from PageObject.cart_page import CartPage
from PageObject.checkout_page import CheckoutPage

from utils.read_json import read_checkout_data, get_valid_login_data


checkout_data = read_checkout_data()
login_data = get_valid_login_data()

negative_checkout_data = [
    data for data in checkout_data
    if "expected_error" in data
]


@pytest.mark.parametrize("data", negative_checkout_data)
def test_checkout_validation(page, data):

    # Login
    login = LoginPage(page)
    login.login(
        login_data["username"],
        login_data["password"]
    )

    # Add product and open cart
    products = ProductsPage(page)
    products.add_backpack_to_cart()
    products.open_cart()

    # Go to checkout
    cart = CartPage(page)
    cart.click_checkout()

    # Enter checkout information
    checkout = CheckoutPage(page)
    checkout.enter_customer_information(
        data["first_name"],
        data["last_name"],
        data["postal_code"]
    )

    # Continue
    checkout.click_continue()

    # Verify error message
    assert checkout.get_error_message() == data["expected_error"]