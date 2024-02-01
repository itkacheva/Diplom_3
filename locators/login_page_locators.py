from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_LINK = (By.XPATH, ".//a[@href='/register']")  # Ссылка "зарегистрироваться"
    PASSWORD_RECOVERY_LINK = (By.XPATH, ".//a[@href='/forgot-password']")  # Ссылка "Восстановить пароль"
    ENTRANCE_BUTTON = (By.XPATH, ".// button[text() = 'Войти']")  # Кнопка "Войти" на форме входа
    INPUT_EMAIL = (By.XPATH, ".//form/fieldset[1]//input")  # Поле ввода email при входе
    INPUT_PASSWORD = (By.XPATH, ".//form/fieldset[2]//input")  # Поле ввода пароля при входе
    SHOW_HIDE_BUTTON = (By.XPATH, ".//div[contains(@class, 'input__icon')]/*[name()='svg']")  # кнопка показать/скрыть в поле ввода пароля

