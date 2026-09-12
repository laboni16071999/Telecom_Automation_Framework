import os


ENVIRONMENT = os.getenv("ENVIRONMENT", "qa").lower()

ENVIRONMENT_URLS = {
    "qa": "https://www.saucedemo.com/",
    "uat": "https://www.saucedemo.com/",
    "prod": "https://www.saucedemo.com/"
}

BASE_URL = ENVIRONMENT_URLS.get(ENVIRONMENT)

if BASE_URL is None:
    raise ValueError(
        f"Invalid environment: {ENVIRONMENT}. "
        f"Choose from: {list(ENVIRONMENT_URLS.keys())}"
    )