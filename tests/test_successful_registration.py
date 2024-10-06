from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from conftest import driver
from element_to_find import Locators


class SuccessfulRegistration:
    def test_registration(self, valid_credentials,driver):
#Инициализация драйвера
        #driver = webdriver.Chrome()
        #driver.get("https://stellarburgers.nomoreparties.site/")
#Вход по кнопке «Войти в аккаунт» на главной
        driver.find_element(*Locators.LOGIN_BUTTON).click()
#Явное ожидание кнопки Зарегистрироваться
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(*Locators.LOGIN_REGISTER))
#Кликнуть на кнопку Зарегистрироваться
        driver.find_element(*Locators.LOGIN_REGISTER).click()
#Вводим учетные данные
        driver.find_element(*Locators.LOGIN_NAME).send_keys(valid_credentials['Имя'])
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(valid_credentials['email'])
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(valid_credentials['password'])
#Кликнуть на кнопку Зарегистрироваться
        driver.find_element(*Locators.LOGIN_REGISTERED).click()
# Ожидание после регистрации
        WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located(*Locators.MAIN_LOGIN))
#Проверка на регистрацию,заполняем те же данные
        driver.find_element(*Locators.LOGIN_REGISTER).click()
        driver.find_element(*Locators.LOGIN_NAME).send_keys(valid_credentials['Имя'])
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(valid_credentials['email'])
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(valid_credentials['password'])
        driver.find_element(*Locators.LOGIN_REGISTERED).click()
        WebDriverWait(driver,10).until(expected_conditions.visibility_of_element_located(*Locators.ALREADY_REGISTERED_MESSAGE))
        already_registered_message = driver.find_element(*Locators.ALREADY_REGISTERED_MESSAGE).text
        assert "Такой пользователь уже существует" in already_registered_message

        #driver.quit()



