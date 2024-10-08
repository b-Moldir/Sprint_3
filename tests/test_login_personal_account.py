from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from element_to_find import Locators


class TestLoginPersonalAccount:
    def test_personal_account(self, valid_credentials, driver):
#Вход по кнопке «Личный кабинет» на главной
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
#Явное ожидание появление надписи "Вход"
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.TITLE_ENTRANCE))
# Авторизация
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(valid_credentials['email'])
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(valid_credentials['password'])
# Кликнуть по кнопке Войти
        driver.find_element(*Locators.LOGIN_ACCOUNT).click()
#Явное ожидание входа на главную страницу
        WebDriverWait(driver,10).until(expected_conditions.visibility_of_element_located(Locators.YOUR_ORDER))
#Проверка что зашла на страницу
        your_order_text = driver.find_element(*Locators.YOUR_ORDER).text
        assert your_order_text == "Оформить заказ"

