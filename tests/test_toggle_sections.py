from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import VALID_CREDENTIALS as vc
from element_to_find import Locators



class TestToggleSections:
    def test_toggle_bun(self, driver):
        # Вход по кнопке «Войти в аккаунт» на главной
        WebDriverWait(driver, 20).until(
            expected_conditions.text_to_be_present_in_element(Locators.LOGIN_BUTTON, "Войти в аккаунт"))
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        # Явное ожидание кнопки Зарегистрироваться
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_REGISTER))
        # Авторизация
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(vc['email'])
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(vc['password'])
        # Кликнуть по кнопке Войти
        driver.find_element(*Locators.LOGIN_ACCOUNT).click()
        # Явное ожидание в разделе Булки
        WebDriverWait(driver,10).until(expected_conditions.text_to_be_present_in_element(Locators.BUN_TEXT, "Булки"))
        # Проверка что в разделе Булки
        bun_text = driver.find_element(*Locators.BUN_TEXT).text
        assert bun_text == "Булки"

    def test_toggle_sauce(self, driver):
        # Вход по кнопке «Войти в аккаунт» на главной
        WebDriverWait(driver, 20).until(
            expected_conditions.text_to_be_present_in_element(Locators.LOGIN_BUTTON, "Войти в аккаунт"))
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
        # Переход к разделу Соусы
        driver.find_element(*Locators.SAUCES_XPATH).click()
        # Явное ожидание в разделе Соусы
        WebDriverWait(driver,10).until(expected_conditions.text_to_be_present_in_element(Locators.SAUCES_TEXT,"Соусы"))
        #Проверка что зашла в разделе Соусы
        sauces_text = driver.find_element(*Locators.SAUCES_TEXT).text
        assert sauces_text == "Соусы"

    def test_toggle_filling(self, driver):
        # Вход по кнопке «Войти в аккаунт» на главной
        WebDriverWait(driver, 20).until(
            expected_conditions.text_to_be_present_in_element(Locators.LOGIN_BUTTON, "Войти в аккаунт"))
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
        # Переход к разделу Начинки
        driver.find_element(*Locators.FILLINGS_XPATH).click()
        # Явное ожидание в разделе Начинки
        WebDriverWait(driver,10).until(expected_conditions.text_to_be_present_in_element(Locators.FILLINGS_TEXT,"Начинки"))
        #Проверка что зашла в разделе Начинки
        fillings_text = driver.find_element(*Locators.FILLINGS_TEXT).text
        assert fillings_text == "Начинки"






