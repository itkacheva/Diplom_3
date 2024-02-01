from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    REGISTRATION_BUTTON = (By.XPATH, ".//form/button[text()='Зарегистрироваться']")  # Кнопка "Зарегистрироваться"
    INPUT_NAME = (By.XPATH, ".//form/fieldset[1]//input")  # Поле ввода Имени при регистрации
    INPUT_EMAIL = (By.XPATH, ".//form/fieldset[2]//input")  # Поле ввода email при регистрации
    INPUT_PASSWORD = (By.XPATH, ".//form/fieldset[3]//input")  # Поле ввода пароля при регистрации