import pytest
from selenium.webdriver.chrome import webdriver



@pytest.fixture()
def valid_credentials():
    return {
        "имя": "Жанна",
        "email": "hello93@mail.ru",
        "password": "123456"
    }

@pytest.fixture()
def invalid_credentials():
    return {
        "имя": "Жанна",
        "email": "hello93@mail.ru",
        "password": "123"
    }


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()
