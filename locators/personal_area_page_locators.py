from selenium.webdriver.common.by import By


class PersonalAreaPageLocators:
    INPUT_NAME = (By.XPATH, ".//div//li[1]//input")  # Поле ввода Имени в профиле (в личном кабинете)
    INPUT_EMAIL = (By.XPATH, ".//div//li[2]//input")  # Поле ввода email  в профиле (в личном кабинете)
    INPUT_PASSWORD = (By.XPATH, ".//div//li[3]//input")  # Поле ввода Пароля  в профиле (в личном кабинете)
    EXIT_BUTTON = (By.XPATH, ".//button[text()='Выход']")  # Кнопка "Выход" в личном кабинете
    HISTORY_ORDERS_LINK = (By.XPATH, ".//a[@href='/account/order-history']")  # Ссылка "История заказов"
