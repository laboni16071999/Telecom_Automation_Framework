import pytest


@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()


@pytest.fixture(scope="session")
def browser(playwright):
    browser = playwright.chromium.launch(
        headless=False,
        slow_mo=1000
    )
    yield browser

    input("Press Enter to close the browser...")

    browser.close()