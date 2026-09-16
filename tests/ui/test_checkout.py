import pytest

from PageObject.login_page import LoginPage
from PageObject.products_page import ProductsPage
from PageObject.cart_page import CartPage
from PageObject.checkout_page import CheckoutPage
from PageObject.overview_page import OverviewPage
from PageObject.complete_page import CompletePage

from utils.read_json import read_checkout_data, get_valid_login_data


# Read test data
checkout_data = read_checkout_data()
login_data = get_valid_login_data()

# Select only successful checkout test data
positive_checkout_data = [
    data for data in checkout_data
    if "expected_message" in data
]


@pytest.mark.parametrize("data", positive_checkout_data)
def test_complete_order(page, data):

    # Login
    login = LoginPage(page)
    login.login(
        login_data["username"],
        login_data["password"]
    )

    # Products page
    products = ProductsPage(page)
    products.add_backpack_to_cart()
    products.open_cart()

    # Cart page
    cart = CartPage(page)
    cart.click_checkout()

    # Checkout page
    checkout = CheckoutPage(page)

    checkout.enter_customer_information(
        data["first_name"],
        data["last_name"],
        data["postal_code"]
    )

    checkout.click_continue()

    # Validate checkout overview
    assert checkout.get_checkout_title() == "Checkout: Overview"
    assert checkout.get_product_name() == data["expected_product"]
    assert checkout.get_product_price() == data["expected_price"]
    assert checkout.get_payment_info() == data["expected_payment"]
    assert checkout.get_shipping_info() == data["expected_shipping"]
    assert checkout.get_total_amount() == data["expected_total"]
    # Overview page
    overview = OverviewPage(page)
    overview.click_finish()

    # Complete page
    complete = CompletePage(page)

    # Verify successful order
    assert complete.get_success_message() == data["expected_message"]