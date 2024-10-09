from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from element_to_find import Locators
from helpers import generate_email
from data import VALID_CREDENTIALS as vc
from data import get_driver


class TestSuccessfulRegistration:
    def test_registration(self):
        driver = get_driver()
        registration_email = generate_email()
        #Вход по кнопке «Войти в аккаунт» на главной
        WebDriverWait(driver, 20).until(
            expected_conditions.text_to_be_present_in_element(Locators.LOGIN_BUTTON, "Войти в аккаунт"))
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        #Явное ожидание кнопки Зарегистрироваться
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_REGISTER))
        #Кликнуть на кнопку Зарегистрироваться
        driver.find_element(*Locators.LOGIN_REGISTER).click()
        #Вводим учетные данные
        driver.find_element(*Locators.LOGIN_NAME).send_keys(vc['name'])
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(registration_email)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(vc['password'])
        #Кликнуть на кнопку Зарегистрироваться
        driver.find_element(*Locators.LOGIN_REGISTERED).click()
        # Ожидание после регистрации
        WebDriverWait(driver,10).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_ACCOUNT))
        #Проверка на успешную регистрацию
        # Авторизация
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(registration_email)
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(vc['password'])
        # Кликнуть по кнопке Войти
        driver.find_element(*Locators.LOGIN_ACCOUNT).click()
        # Явное ожидание входа на главную страницу
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.YOUR_ORDER))
        # Проверка, что смогла зайти на страницу
        your_order_text = driver.find_element(*Locators.YOUR_ORDER).text
        assert your_order_text == "Оформить заказ"





