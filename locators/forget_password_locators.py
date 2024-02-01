from selenium.webdriver.common.by import By


class ForgetPageLocators:
    INPUT_EMAIL = (By.XPATH, ".//form/fieldset//input")  # Поле ввода email при регистрации
    RECOVERY_BUTTON = (By.XPATH, ".//form/button[text()='Восстановить']")  # Кнопка "Восстановить"