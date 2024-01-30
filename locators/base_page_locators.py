from selenium.webdriver.common.by import By


class BasePageLocators:
    ACCOUNT_PERSONAL_BUTTON = (By.XPATH, ".//a[@href='/account']")  # Кнопка "Личный кабинет"
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//li/a[@href='/']")  # Кнопка "Конструктор"
    ORDERS_FEED_BUTTON = (By.XPATH, ".//a[@href='/feed']")  # Кнопка "Лист заказов"
    LOGO = (By.XPATH, ".//nav//div//a[@href='/']")  # Логотип Stellar Burgers



