from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from element_to_find import Locators
from data import VALID_CREDENTIALS as vc




class TestLoginPersonalAccount:
    def test_login_to_account(self, driver):
        # Вход по кнопке «Войти в аккаунт» на главной
        WebDriverWait(driver, 20).until(
            expected_conditions.text_to_be_present_in_element(Locators.LOGIN_BUTTON, "Войти в аккаунт"))
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        # Явное ожидание кнопки Зарегистрироваться
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.LOGIN_REGISTER))
        # Авторизация
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(vc['email'])
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(vc['password'])
        # Кликнуть по кнопке Войти
        driver.find_element(*Locators.LOGIN_ACCOUNT).click()
        # Явное ожидание входа на главную страницу
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.YOUR_ORDER))
        # Проверка, что смогла зайти на страницу
        your_order_text = driver.find_element(*Locators.YOUR_ORDER).text
        assert your_order_text == "Оформить заказ"

    def test_personal_account(self, driver):
        #Вход по кнопке «Личный кабинет» на главной
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        #Явное ожидание появление надписи "Вход"
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.TITLE_ENTRANCE))
        # Авторизация
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(vc['email'])
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(vc['password'])
        # Кликнуть по кнопке Войти
        driver.find_element(*Locators.LOGIN_ACCOUNT).click()
        #Явное ожидание входа на главную страницу
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.YOUR_ORDER))
        # Проверка, что смогла зайти на страницу
        your_order_text = driver.find_element(*Locators.YOUR_ORDER).text
        assert your_order_text == "Оформить заказ"

    def test_registration_form(self, driver):
        # Вход по кнопке «Войти в аккаунт» на главной
        WebDriverWait(driver, 20).until(
                expected_conditions.text_to_be_present_in_element(Locators.LOGIN_BUTTON, "Войти в аккаунт"))
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        # Явное ожидание кнопки Зарегистрироваться
        WebDriverWait(driver, 5).until(
                expected_conditions.visibility_of_element_located(Locators.LOGIN_REGISTER))
        # Кликнуть на кнопку Зарегистрироваться
        driver.find_element(*Locators.LOGIN_REGISTER).click()
        # Явное ожидание текста "Уже зарегистрированы?"
        WebDriverWait(driver, 5).until(
                expected_conditions.visibility_of_element_located(Locators.ALREADY_REGISTERED))
        # Кликнуть по кнопке Войти
        driver.find_element(*Locators.LOGIN_INPUT).click()
        # Авторизация
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(vc['email'])
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(vc['password'])
        # Кликнуть по кнопке Войти
        driver.find_element(*Locators.LOGIN_ACCOUNT).click()
        # Явное ожидание входа на главную страницу
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.YOUR_ORDER))
        # Проверка, что смогла зайти на страницу
        your_order_text = driver.find_element(*Locators.YOUR_ORDER).text
        assert your_order_text == "Оформить заказ"

    def test_login_recover_password(self, driver):
        # Вход по кнопке «Войти в аккаунт» на главной
        WebDriverWait(driver, 20).until(
            expected_conditions.text_to_be_present_in_element(Locators.LOGIN_BUTTON, "Войти в аккаунт"))
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        # Явное ожидание текста «Забыли пароль?»
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.FORGOT_PASSWORD_TEXT))
        # Кликнуть по кнопке «Восстановить пароль»
        driver.find_element(*Locators.RECOVER_PASSWORD).click()
        # Явное ожидание надписи «Восстановление пароля»
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.RECOVERY_PASSWORD_TEXT))
        # Кликнуть по кнопке Войти
        driver.find_element(*Locators.LOGIN_INPUT).click()
        # Явное ожидание надписи «Вход»
        WebDriverWait(driver, 5).until(
            expected_conditions.text_to_be_present_in_element(Locators.TITLE_ENTRANCE, "Вход"))
        # Авторизация
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(vc['email'])
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(vc['password'])
        # Кликнуть по кнопке Войти
        driver.find_element(*Locators.LOGIN_ACCOUNT).click()
        # Явное ожидание входа на главную страницу
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.YOUR_ORDER))
        # Проверка, что смогла зайти на страницу
        your_order_text = driver.find_element(*Locators.YOUR_ORDER).text
        assert your_order_text == "Оформить заказ"

