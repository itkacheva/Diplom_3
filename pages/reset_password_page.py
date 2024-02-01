import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.reset_password_page_locators import *
from pages.base_page import BasePage
from urls import PagesUrls


class ResetPasswordPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ждем пока загрузится страница сброса пароля')
    def wait_for_load_reset_password_page(self):
        WebDriverWait(self.driver, 10).until(expected_conditions
                                             .visibility_of_element_located(ResetPageLocators.SAVE_BUTTON))

    @allure.step('Нажимаем кнопку "Сохранить"')
    def click_entrance_in_account_button(self):
        self.driver.find_element(*ResetPageLocators.SAVE_BUTTON).click()

    @allure.step('Получаем текст плейсхолдера в поле "Код из письма"')
    def get_place_holder_code_text(self):
        return (self.driver.find_element(*ResetPageLocators.INPUT_CODE_PLACE_HOLDER).text)

    @allure.step('Получаем  url страницы логина')
    def get_reset_password_page_url(self):
        return (PagesUrls.main_page_url+PagesUrls.reset_password_page_url)

    @allure.step('Нажимаем на кнопку показать/скрыть в поле ввода пароля')
    def click_show_hide_button(self):
        self.driver.find_element(*ResetPageLocators.SHOW_HIDE_BUTTON).click()

    @allure.step('Проверяем обводку активного поля "Пароль"')
    def check_stroke_active_input_password(self):
        if self.driver.find_element(*ResetPageLocators.STROKE_ACTIVE_INPUT_PASSWORD):
            return True
        else:
            return False

    @allure.step('Проверяем, что поле "Пароль" стало активным ')
    def check_active_input_password(self):
        if self.driver.find_element(*ResetPageLocators.ACTIVE_INPUT_PASSWORD):
            return True
        else:
            return False