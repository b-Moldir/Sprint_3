from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from element_to_find import Locators
from data import VALID_CREDENTIALS as vc
from data import get_driver


class TestClickConstructorLogo:
    def test_click_constructor_logo(self):
        driver = get_driver()
        # Вход по кнопке «Войти в аккаунт» на главной
        WebDriverWait(driver, 20).until(expected_conditions.text_to_be_present_in_element(Locators.LOGIN_BUTTON, "Войти в аккаунт"))
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        # Явное ожидание кнопки Зарегистрироваться
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_REGISTER))
        # Авторизация
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(vc['email'])
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(vc['password'])
        # Кликнуть по кнопке Войти
        driver.find_element(*Locators.LOGIN_ACCOUNT).click()
        # Явное ожидание входа на главную страницу
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.YOUR_ORDER))
        # Переход по клику Личный Кабинет
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        # Явное ожидание входа в Личный кабинет
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.PROFILE_TEXT))
        # Переход по клику Конструктор
        driver.find_element(*Locators.CONSTRUCTOR_TEXT).click()
        #Явное ожидание входа на главную страницу
        WebDriverWait(driver,10).until(expected_conditions.visibility_of_element_located(Locators.YOUR_ORDER))
        #Проверка что зашла на страницу
        your_order_text = driver.find_element(*Locators.YOUR_ORDER).text
        assert your_order_text == "Оформить заказ"
        # Переход по клику Личный Кабинет
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        # Явное ожидание входа в Личный кабинет
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.PROFILE_TEXT))
        # Переход по клику на логотип
        logo_button = driver.find_element(*Locators.LOGO_BUTTON)
        driver.execute_script("arguments[0].scrollIntoView(true);", logo_button)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Locators.LOGO_BUTTON))
        logo_button.click()
        #Явное ожидание входа на главную страницу
        WebDriverWait(driver,10).until(expected_conditions.visibility_of_element_located(Locators.YOUR_ORDER))
        #Проверка что зашла на страницу
        your_order_text = driver.find_element(*Locators.YOUR_ORDER).text
        assert your_order_text == "Оформить заказ"






