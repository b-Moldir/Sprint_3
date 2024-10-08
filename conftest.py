import pytest
from selenium import webdriver


@pytest.fixture()
def valid_credentials():
    return {
        "name": "Молдир",
        "email": "moldirbektenova11555@yandex.ru",
        "password": "123456"
    }


@pytest.fixture()
def invalid_credentials():
    return {
        "name": "Молдир",
        "email": "moldirbektenova11555@yandex.ru",
        "password": "123"
    }


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()
