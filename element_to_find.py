from selenium.webdriver.common.by import By


class Locators:
    LOGIN_BUTTON = [By.XPATH,'//section[2]//button[text()="Войти в аккаунт"]']
    LOGIN_REGISTER = [By.XPATH, '//p[1]/a[@class="Auth_link__1fOlj"]']
    LOGIN_NAME = [By.XPATH, '//label[ text()="Имя" ]/parent::div/input']
    LOGIN_EMAIL = [By.XPATH, '//label[ text()="Email" ]/parent::div/input']
    LOGIN_PASSWORD = [By.XPATH, '//label[ text()="Пароль" ]/parent::div/input']
    LOGIN_REGISTERED = [By.XPATH, '//main[@class="App_componentContainer__2JC2W"]//button[text()="Зарегистрироваться"]']
    MAIN_LOGIN = [By.XPATH, '//main[@class="App_componentContainer__2JC2W"]//div[@class="Auth_login__3hAey"]']
    ALREADY_REGISTERED_MESSAGE = [By.XPATH, '//main//p[text()="Такой пользователь уже существует"]']
    TEXT_INCORRECT = [By.XPATH, '//main[@class="App_componentContainer__2JC2W"]//p[text()="Некорректный пароль"]']
    LOGIN_ACCOUNT = [By.XPATH, '//main//button[text="Войти"]']
    YOUR_ORDER= [By.XPATH, '//section[2]//button[text()="Оформить заказ"]']
    PERSONAL_ACCOUNT = [By.XPATH, '//header[@class="AppHeader_header__X9aJA pb-4 pt-4"]//p[text()="Личный Кабинет"]']
    TITLE_ENTRANCE = [By.XPATH, '//main[@class="App_componentContainer__2JC2W"]//h2[text()="Вход"]']
    ALREADY_REGISTERED = [By.XPATH, '//main[@class="App_componentContainer__2JC2W"]//p[text() = "Уже зарегистрированы?"]']
    LOGIN_INPUT = [By.XPATH, '//main[@class="App_componentContainer__2JC2W"]//a[@class = "Auth_link__1fOlj"]']
    FORGOT_PASSWORD_TEXT = [By.XPATH, '//main//p[2][text()="Забыли пароль?"]']
    RECOVER_PASSWORD = [By.CSS_SELECTOR, 'p:nth-child(2) > a']
    RECOVERY_PASSWORD_TEXT = [By.XPATH, '//main//h2[text()="Восстановление пароля"]']
    RESTORE_XPATH = [By.XPATH, '//form[@class="Auth_form__3qKeq mb-20"]//button[text()="Восстановить"]']
    CODE_FROM_LETTER = [By.XPATH, '//label[ text()="Введите код из письма" ]/parent::div/input']
    SAVE_BUTTON = [By.XPATH, '//main[@class="App_componentContainer__2JC2W"]//button[text()="Сохранить"]']
    SWITCH_PERSONAL_ACCOUNT = 