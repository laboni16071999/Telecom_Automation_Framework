import pytest
from config.config import BASE_URL


@pytest.fixture
def page(browser):
    page = browser.new_page()
    page.goto(BASE_URL)
    yield page
    page.close()


@pytest.fixture(scope="session")
def browser(playwright):
    browser = playwright.chromium.launch(
        headless=False,
        slow_mo=1000
    )

    yield browser

    browser.close()