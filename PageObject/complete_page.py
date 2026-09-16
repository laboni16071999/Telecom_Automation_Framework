class CompletePage:

    def __init__(self, page):
        self.page = page

        self.success_message = page.locator(".complete-header")

    def get_success_message(self):
        return self.success_message.text_content()