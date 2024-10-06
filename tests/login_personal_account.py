from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from conftest import driver
from element_to_find import Locators


class LoginPersonalAccount:
    def test_personal_account(self, valid_credentials, driver):
        #Инициализация драйвера
        #driver = webdriver.Chrome()
        #driver.get("https://stellarburgers.nomoreparties.site/")
        #Вход по кнопке «Личный кабинет» на главной
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()


#Явное ожидание появление надписи "Вход"
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(*Locators.TITLE_ENTRANCE))
# Авторизация
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(valid_credentials['email'])
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(valid_credentials['password'])
# Кликнуть по кнопке Войти
        driver.find_element(*Locators.LOGIN_ACCOUNT).click()
# Явное ожидание входа на главную страницу
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(*Locators.MAIN_BURGER_TEXT))
# Проверка что зашла на страницу
        main_burger_text = driver.find_element(*Locators.MAIN_BURGER_TEXT).text
        assert main_burger_text == "Соберите бургер"

