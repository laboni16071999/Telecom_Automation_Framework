from PageObject.login_page import LoginPage


def test_login(page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    page.wait_for_timeout(5000)