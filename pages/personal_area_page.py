import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.personal_area_page_locators import PersonalAreaPageLocators
from pages.base_page import BasePage


class PersonalAreaPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Получаем данные пользователя в личном кабинете')
    def get_personal_area_data(self):
        data = {
            "name": self.driver.find_element(*PersonalAreaPageLocators.INPUT_NAME).get_attribute("value"),
            "email": self.driver.find_element(*PersonalAreaPageLocators.INPUT_EMAIL).get_attribute("value"),
            "password": self.driver.find_element(*PersonalAreaPageLocators.INPUT_PASSWORD).get_attribute("value")
        }
        return (data)

    @allure.step('Нажимаем на кнопку "Выход"')
    def click_exit_button(self):
        self.driver.find_element(*PersonalAreaPageLocators.EXIT_BUTTON).click()

    @allure.step('Ждем пока загрузится страница личного кабинета')
    def wait_for_personal_area_page(self):
        WebDriverWait(self.driver, 10).until(expected_conditions
                                             .visibility_of_element_located(PersonalAreaPageLocators.INPUT_PASSWORD))

    @allure.step('Нажимаем на раздел "История заказов"')
    def click_history_orders(self):
        self.driver.find_element(*PersonalAreaPageLocators.HISTORY_ORDERS_LINK).click()
