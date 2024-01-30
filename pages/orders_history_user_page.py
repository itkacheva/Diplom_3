import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.orders_history_user_locators import OrderHistoryLocators
from pages.base_page import BasePage


class OrdersHistoryPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Получаем список заказов пользователя')
    def get_list_orders_user(self):
        list_orders=[]
        for lo in self.driver.find_elements(*OrderHistoryLocators.LIST_ORDERS_USER):
           list_orders.append(lo.text)
        return list_orders

    @allure.step('Ждем пока загрузится страница c Историей заказов Пользователя')
    def wait_for_load_orders_history_page(self):
        WebDriverWait(self.driver, 10).until(expected_conditions
                                             .visibility_of_element_located(OrderHistoryLocators.LIST_ORDERS_USER))
