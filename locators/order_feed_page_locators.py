from selenium.webdriver.common.by import By


class OrderFeedLocators:

    TITLE_ORDER_FEED = (By.XPATH, ".//h1[text() = 'Лента заказов']")  # Заголовок 'Лента заказов'.
    LIST_ALL_ORDERS = (By.XPATH, ".//div[contains(@class,'OrderHistory_textBox')]/p[contains(@class,'text_type_digits')]")  # список всех заказов
    CONTAINER_ORDERS = (By.XPATH, ".//a[contains(@class,'OrderHistory_link')]")  # Список всех заказов.
    POP_UP_ORDER_WINDOW = (By.XPATH, ".//div[contains(@class,'Modal_orderBox')]/p")  # Всплывающее окно с деталями заказа.
    ORDER_NUMBER_IN_WORK = (By.XPATH, ".//ul[contains(@class,'OrderFeed_orderListReady')] /li")  # Счетчик "Выполнено за все время"
    ALL_TIME_COUNTER_VALUE = (By.XPATH, ".//p[text()='Выполнено за все время:']/../p[contains(@class,'OrderFeed_number')]")  # Счетчик "Выполнено за все время"
    TODAY_COUNTER_VALUE = (By.XPATH, ".//p[text()='Выполнено за сегодня:']/../p[contains(@class,'OrderFeed_number')]")  # Счетчик "Выполнено за сегодня"