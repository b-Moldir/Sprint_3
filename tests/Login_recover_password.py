from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from conftest import driver
from element_to_find import Locators
class RecoverPassword:
    def test_login_recover_password(self, valid_credentials,driver):
# Вход по кнопке «Войти в аккаунт» на главной
        driver.find_element(*Locators.LOGIN_BUTTON).click()
# Явное ожидание текста «Забыли пароль?»
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(*Locators.FORGOT_PASSWORD_TEXT))
# Кликнуть по кнопке «Восстановить пароль»
        driver.find_element(*Locators.RECOVER_PASSWORD).click()
# Явное ожидание надписи «Восстановление пароля»
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(*Locators.RECOVERY_PASSWORD_TEXT))
# Заполнить поле емайл
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(valid_credentials['email'])
# Кликнуть по кнопке «Восстановить»
        driver.find_element(*Locators.RESTORE_XPATH).click()
# Явное ожидание поле  «Введите новый пароль»
        WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located(*Locators.LOGIN_PASSWORD))
# Заполнить поле пароль
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys("456123")
# Заполнить поле "Введите код из письма"
        driver.find_element(*Locators.CODE_FROM_LETTER).-------
# Кликнуть по кнопке «Сохранить»
        driver.find_element(*Locators.SAVE_BUTTON).click()
