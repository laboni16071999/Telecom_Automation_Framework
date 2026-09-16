class CartPage:

    def __init__(self, page):
        self.page = page

        # Cart page elements
        self.cart_title = page.locator(".title")
        self.backpack_item = page.locator("[data-test='inventory-item-name']")

        # Checkout button
        self.checkout_button = page.locator("[data-test='checkout']")

    def get_cart_title(self):
        return self.cart_title.text_content()

    def get_product_name(self):
        return self.backpack_item.text_content()

    def click_checkout(self):
        self.checkout_button.click()