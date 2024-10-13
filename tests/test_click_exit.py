from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from element_to_find import Locators
from data import VALID_CREDENTIALS as vc



class TestClickExit:
    def test_click_exit(self,driver):
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
        # Кликнуть по кнопке Выйти
        driver.find_element(*Locators.EXIT_BUTTON).click()
        # Явное ожидание страницы Войти
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.TITLE_ENTRANCE))
        #Проверка что странице Войти
        title_entrance_text = driver.find_element(*Locators.TITLE_ENTRANCE).text
        assert title_entrance_text == "Вход"


