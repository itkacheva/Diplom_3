import random
import allure

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.order_feed_page_locators import OrderFeedLocators
from pages.base_page import BasePage
from urls import PagesUrls


class OrderFeedPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ждем пока загрузится страница ленты заказов')
    def wait_for_load_order_feed_page(self):
        WebDriverWait(self.driver, 10).until(expected_conditions
                                             .visibility_of_element_located(OrderFeedLocators.TITLE_ORDER_FEED))

    @allure.step('Кликаем на произвольный заказ')
    def click_random_order(self):
        order=random.choice(self.driver.find_elements(*OrderFeedLocators.CONTAINER_ORDERS))
        order.location_once_scrolled_into_view
        WebDriverWait(self.driver, 15).until(
            expected_conditions.element_to_be_clickable(order))
        order.click()

    @allure.step('Ждем всплывающее окно с деталями заказа')
    def wait_for_order_details_window(self):
        WebDriverWait(self.driver, 10).until(expected_conditions
                                             .visibility_of_element_located(OrderFeedLocators.POP_UP_ORDER_WINDOW))

    @allure.step('Проверяем что открылось окно "Детали заказа"')
    def check_show_details_window(self):
        if self.driver.find_element(*OrderFeedLocators.POP_UP_ORDER_WINDOW):
            return True
        else:
            return False

    @allure.step('Ждем пока загрузится главная страница')
    def wait_for_load_feed_orders_page(self):
        WebDriverWait(self.driver, 10).until(expected_conditions
                                             .visibility_of_element_located(OrderFeedLocators.TITLE_ORDER_FEED))

    @allure.step('Получаем  url страницы "История заказов')
    def get_feed_orders_page_url(self):
        return (PagesUrls.main_page_url+PagesUrls.history_orders_page_url)

    @allure.step('Считываем значение счетчика "Выполнено за всё время"')
    def get_count_all_time(self):
        return int(self.driver.find_element(*OrderFeedLocators.ALL_TIME_COUNTER_VALUE).text)

    @allure.step('Считываем номер заказа в блоке "В работе"')
    def get_order_number_in_work(self):
        WebDriverWait(self.driver, 10).\
            until_not(expected_conditions.text_to_be_present_in_element
                              (OrderFeedLocators.ORDER_NUMBER_IN_WORK, 'Все текущие заказы готовы!'))
        return int(self.driver.find_element(*OrderFeedLocators.ORDER_NUMBER_IN_WORK).text)

    @allure.step('Считываем значение счетчика "Выполнено за сегодня"')
    def get_count_today(self):
        return int(self.driver.find_element(*OrderFeedLocators.TODAY_COUNTER_VALUE).text)

    @allure.step('Создаем заказ с ингридиентами')
    def make_order(self,main_page):
        self.click_constructor_button()
        main_page.wait_for_load_main_page()
        main_page.add_random_ingredient_in_order()
        main_page.click_make_order_button()
        main_page.wait_for_order_details_window()
        order_number = main_page.get_order_number_details_window()
        main_page.close_order_details_window()
        main_page.click_feed_orders_button()
        return int(order_number)

    @allure.step('Получаем номера заказов из "Ленты заказов"')
    def get_list_orders(self):
        list_orders = []
        for lo in self.driver.find_elements(*OrderFeedLocators.LIST_ALL_ORDERS):
           list_orders.append(lo.text)
        return list_orders
