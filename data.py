from selenium import webdriver

VALID_CREDENTIALS = {
    "name": "Молдир",
    "email": "moldirbektenova11555@yandex.ru",
    "password": "123456"
}

INVALID_CREDENTIALS = {
    "name": "Молдир",
    "email": "moldirbektenova11555@yandex.ru",
    "password": "123"
}


def get_driver():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    return driver