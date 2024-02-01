from selenium.webdriver.common.by import By


class ResetPageLocators:
    INPUT_PASSWORD = (By.XPATH, ".//form/fieldset//input[@type='password']")  # Не активное поле ввода нового пароля
    STROKE_ACTIVE_INPUT_PASSWORD = (By.XPATH, ".//div[contains(@class,'input_status_active')]")  # Обводка активного поля ввода нового пароля
    ACTIVE_INPUT_PASSWORD = (By.XPATH, ".//label[contains(@class,'input__placeholder-focused')]")  # Признак активности поле ввода нового пароля
    INPUT_CODE = (By.XPATH, ".//form/fieldset//input[@type='text']")  # Поле ввода кода из письма
    INPUT_CODE_PLACE_HOLDER = (By.XPATH, ".//form/fieldset[2]//label")  # Плейсхолдер для поле ввода кода из письма
    SAVE_BUTTON = (By.XPATH, ".//form/button[text()='Сохранить']")  # Кнопка "Сохранить"
    SHOW_HIDE_BUTTON = (By.XPATH, ".//div[contains(@class, 'input__icon')]/*[name()='svg']")  # кнопка показать/скрыть в поле ввода пароля

