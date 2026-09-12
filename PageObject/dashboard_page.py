class DashboardPage:

    def __init__(self, page):
        self.page = page

        self.products_title = page.locator(".title")

    def get_products_title(self):
        return self.products_title.text_content()