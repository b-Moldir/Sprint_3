from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from element_to_find import Locators


class TestIncorrectPassword:
    def test_password(self, invalid_credentials, driver):

#Вход по кнопке «Войти в аккаунт» на главной

        WebDriverWait(driver, 20).until(expected_conditions.text_to_be_present_in_element(Locators.LOGIN_BUTTON, "Войти в аккаунт"))
        driver.find_element(*Locators.LOGIN_BUTTON).click()
#Явное ожидание кнопки Зарегистрироваться
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_REGISTER))
#Кликнуть на кнопку Зарегистрироваться
        driver.find_element(*Locators.LOGIN_REGISTER).click()
#Вводим учетные данные
        driver.find_element(*Locators.LOGIN_NAME).send_keys(invalid_credentials['name'])
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(invalid_credentials['email'])
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(invalid_credentials['password'])
#Кликнуть на кнопку Зарегистрироваться
        driver.find_element(*Locators.LOGIN_REGISTERED).click()
#Ожидание сообщение об ошибке
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.TEXT_INCORRECT))
#Проверка на неверный пароль
        text_incorrect_password = driver.find_element(*Locators.TEXT_INCORRECT).text
        assert "Некорректный пароль" in text_incorrect_password
