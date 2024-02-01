from selenium.webdriver.common.by import By


class OrderHistoryLocators:
    LIST_ORDERS_USER = (By.XPATH, ".//div[contains(@class,'OrderHistory_textBox')]/p[contains(@class,'text_type_digits')]")  # список заказов пользователя.
