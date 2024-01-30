from selenium.webdriver.common.by import By


class MainPageLocators:
    ENTRANCE_IN_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")  # Кнопка "Войти в аккаунт"
    MAKE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")  # Кнопка "Войти в аккаунт"
    TITLE_CONTAINER_INGREDIENTS = (By.XPATH, "// h1[text() = 'Соберите бургер']")  # Заголовок 'Соберите бургер'.
    TITLE_INGREDIENT_DETAILS_WINDOW = (By.XPATH, "//h2[contains(@class,'Modal_modal__title_modified')]")  # заголовок модального окна "Детали ингридиента"
    ORDER_NUMBER_DETAILS_WINDOW = (By.XPATH, "//h2[contains(@class,'text_type_digits-large')]")  # номер заказа из модального окна "Детали ингридиента"
    BASKET = (By.XPATH, "//ul[contains(@class,'BurgerConstructor_basket')]")  # область корзины
    CONTAINER_INGREDIENTS = (By.XPATH, ".//a[contains(@class, 'BurgerIngredient_ingredient')]")  # контейнер ингридиенnов
    INGREDIENT_IMG = (By.XPATH, ".//img[contains(@class, 'BurgerIngredient_ingredient')]") # конкретный ингридиент
    INGREDIENT_COUNTER = (By.XPATH, ".//p[contains(@class, 'counter_counter')]")  # счетчик для конкретного ингридиента
    CLOSE_BUTTON_DETAILS_WINDOW = (By.XPATH, ".//button[contains(@class, 'Modal_modal__close')]")  # кнопка "Закрыть" заголовок модального окна "Детали ингридиента" и "Детали заказа"
    TITLE_ORDER_DETAILS_WINDOW = (By.XPATH, "//div[contains(@class,'Modal_modal__contentBox')]/p[contains(@class,'text_type_main')]")  # заголовок модального окна "Идентификатор заказа"
