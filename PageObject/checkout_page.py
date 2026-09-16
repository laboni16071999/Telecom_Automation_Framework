class CheckoutPage:

    def __init__(self, page):
        self.page = page

        # Checkout information fields
        self.first_name = page.locator("[data-test='firstName']")
        self.last_name = page.locator("[data-test='lastName']")
        self.postal_code = page.locator("[data-test='postalCode']")

        # Continue button
        self.continue_button = page.locator("[data-test='continue']")

        # Checkout overview title
        self.checkout_title = page.locator(".title")

        #check product name
        self.product_name = page.locator("[data-test='inventory-item-name']")

        #check product price
        self.product_price = page.locator("[data-test='inventory-item-price']")
        #check payment_info
        self.payment_info = page.locator("[data-test='payment-info-value']")
        #check Shipping_info
        self.shipping_info = page.locator("[data-test='shipping-info-value']")
        #check total_amount
        self.total_amount = page.locator("[data-test='total-label']")

        # Checkout error message
        self.error_message = page.locator("[data-test='error']")

    def enter_customer_information(self, first_name, last_name, postal_code):
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.postal_code.fill(postal_code)

    def click_continue(self):
        self.continue_button.click()

    def get_checkout_title(self):
        return self.checkout_title.text_content()

    def get_product_name(self):
        return self.product_name.text_content()

    def get_product_price(self):
        return self.product_price.text_content()

    def get_payment_info(self):
        return self.payment_info.text_content()

    def get_shipping_info(self):
        return self.shipping_info.text_content()

    def get_total_amount(self):
        return self.total_amount.text_content()

    def get_error_message(self):
        return self.error_message.text_content()