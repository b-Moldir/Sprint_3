from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from element_to_find import Locators

class TestSwitchPersonalAccount:
    def test_switch_personal_account(self, valid_credentials, driver):
# Вход по кнопке «Войти в аккаунт» на главной
        WebDriverWait(driver, 20).until(
            expected_conditions.text_to_be_present_in_element(Locators.LOGIN_BUTTON, "Войти в аккаунт"))
        driver.find_element(*Locators.LOGIN_BUTTON).click()
# Явное ожидание кнопки Зарегистрироваться
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_REGISTER))
# Авторизация
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(valid_credentials['email'])
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(valid_credentials['password'])
# Кликнуть по кнопке Войти
        driver.find_element(*Locators.LOGIN_ACCOUNT).click()
# Явное ожидание входа на главную страницу
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.YOUR_ORDER))
# Переход по клику Личный Кабинет
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
# Явное ожидание входа в Личный кабинет
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.PROFILE_TEXT))
# Проверка что внутри личного кабинета
        profile_text = driver.find_element(*Locators.PROFILE_TEXT).text
        assert "Профиль" == profile_text


