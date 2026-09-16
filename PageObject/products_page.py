class ProductsPage:

    def __init__(self, page):
        self.page = page

        self.products_title = page.locator(".title")
        self.backpack = page.locator("[data-test='add-to-cart-sauce-labs-backpack']")
        self.cart_icon = page.locator(".shopping_cart_link")

    def get_products_title(self):
        return self.products_title.text_content()

    def add_backpack_to_cart(self):
        self.backpack.click()

    def open_cart(self):
        self.cart_icon.click()