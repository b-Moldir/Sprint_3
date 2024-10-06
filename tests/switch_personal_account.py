from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from conftest import driver
from element_to_find import Locators

class SwitchPersonalAccount:
    def test_switch_personal_account(self,driver,valid_credentials):
# Вход по кнопке «Войти в аккаунт» на главной
        driver.find_element(*Locators.LOGIN_BUTTON).click()
# Явное ожидание кнопки Зарегистрироваться
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(*Locators.LOGIN_REGISTER))
# Авторизация
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(valid_credentials['email'])
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(valid_credentials['password'])
# Кликнуть по кнопке Войти
        driver.find_element(*Locators.LOGIN_ACCOUNT).click()
# Явное ожидание входа на главную страницу
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(*Locators.YOUR_ORDER))
