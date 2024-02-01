import allure

from locators.base_page_locators import BasePageLocators
from urls import PagesUrls


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Нажимаем кнопку "Личный кабинет"')
    def click_personal_area_button(self):
        self.driver.find_element(*BasePageLocators.ACCOUNT_PERSONAL_BUTTON).click()

    @allure.step('Нажимаем кнопку "Лента заказов"')
    def click_feed_orders_button(self):
        self.driver.find_element(*BasePageLocators.ORDERS_FEED_BUTTON).click()

    @allure.step('Нажимаем кнопку "Конструктор заказов"')
    def click_constructor_button(self):
        self.driver.find_element(*BasePageLocators.CONSTRUCTOR_BUTTON).click()

    @allure.step('Получаем  url главной страницы')
    def get_main_page_url(self):
        return (PagesUrls.main_page_url)






