from datetime import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from conftest import driver
from element_to_find import Locators


class IncorrectPassword:
    def test_password(self, invalid_credentials, driver):
#Инициализация драйвера
        #options = Options()
        # options.add_argument('--headless')
# Указание пути к драйверу
        #service = Service("C:\Program Files\WebDriver\bin")
        #driver = webdriver.Chrome(service=service, options=options)
#Вход по кнопке «Войти в аккаунт» на главной
        driver.find_element(*Locators.LOGIN_BUTTON).click()
#Явное ожидание кнопки Зарегистрироваться
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(*Locators.LOGIN_REGISTER))
#Кликнуть на кнопку Зарегистрироваться
        driver.find_element(*Locators.LOGIN_REGISTER).click()
#Вводим учетные данные
        driver.find_element(*Locators.LOGIN_NAME).send_keys(invalid_credentials["Имя"])
        driver.find_element(*Locators.LOGIN_EMAIL).send_keys(invalid_credentials['email'])
        driver.find_element(*Locators.LOGIN_PASSWORD).send_keys(invalid_credentials['password'])
#Кликнуть на кнопку Зарегистрироваться
        driver.find_element(*Locators.LOGIN_REGISTERED).click()
#Ожидание сообщение об ошибке
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(*Locators.TEXT_INCORRECT))
#Проверка на неверный пароль
        text_incorrect_password = driver.find_element(*Locators.TEXT_INCORRECT).text
        assert "Некорректный пароль" in text_incorrect_password
        driver.quit()
