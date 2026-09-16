from PageObject.login_page import LoginPage
from PageObject.products_page import ProductsPage
from PageObject.cart_page import CartPage


def test_add_product_to_cart(page):

    # Step 1: Login
    login_page = LoginPage(page)
    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    # Step 2: Add Sauce Labs Backpack
    products_page = ProductsPage(page)
    products_page.add_backpack_to_cart()

    # Step 3: Open Cart
    products_page.open_cart()

    # Step 4: Create Cart Page object
    cart_page = CartPage(page)

    # Step 5: Verify Cart page
    assert cart_page.get_cart_title() == "Your Cart"

    # Step 6: Verify Backpack is present
    assert cart_page.get_product_name() == "Sauce Labs Backpack"
