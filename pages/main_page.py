import random
import allure

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import *
from pages.base_page import BasePage


class MainPageBurgers(BasePage):
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ждем пока загрузится главная страница')
    def wait_for_load_main_page(self):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(MainPageLocators.TITLE_CONTAINER_INGREDIENTS))

    @allure.step('Нажимаем кнопку "Войти в аккаунт"')
    def click_entrance_in_account_button(self):
        self.driver.find_element(*MainPageLocators.ENTRANCE_IN_ACCOUNT_BUTTON).click()

    @allure.step('Ищем заголовок "Соберите бургер"')
    def check_title_container_ingredients(self):
        if self.driver.find_element(*MainPageLocators.TITLE_CONTAINER_INGREDIENTS):
            return True
        else:
            return False

    @allure.step('Кликаем на произвольный ингридиент')
    def click_random_ingredient(self):
        ingredient=random.choice(self.driver.find_elements(*MainPageLocators.CONTAINER_INGREDIENTS))
        ingredient.location_once_scrolled_into_view
        WebDriverWait(self.driver, 15).until(
            expected_conditions.element_to_be_clickable(ingredient))
        ingredient.click()

    @allure.step('Добавляем произвольный ингридиент в заказ')
    def add_random_ingredient_in_order(self):

        ingredient_parent = random.choice(self.driver.find_elements(*MainPageLocators.CONTAINER_INGREDIENTS))

        ingredient = ingredient_parent.find_element(*MainPageLocators.INGREDIENT_IMG)
        area = self.driver.find_element(*MainPageLocators.BASKET)
        actions = ActionChains(self.driver)
        ingredient.location_once_scrolled_into_view
        WebDriverWait(self.driver, 15).until(expected_conditions.element_to_be_clickable(ingredient))

        actions.drag_and_drop(self.driver.find_element(*MainPageLocators.CONTAINER_INGREDIENTS), area).perform()
        actions.drag_and_drop(ingredient, area).perform()
        return int(ingredient_parent.find_element(*MainPageLocators.INGREDIENT_COUNTER).text)

    @allure.step('Ждем всплывающее окно с деталями ингридиентов')
    def wait_for_ingredient_details_window(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(MainPageLocators.TITLE_INGREDIENT_DETAILS_WINDOW))

    @allure.step('Закрываем всплывающее окно с деталями ингридиентов')
    def close_ingredient_details_window(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(MainPageLocators.CLOSE_BUTTON_DETAILS_WINDOW)).click()

    @allure.step('Проверяем заголовок модального окна "Детали ингредиента"')
    def check_ingredient_details_window(self):
        if self.driver.find_element(*MainPageLocators.TITLE_INGREDIENT_DETAILS_WINDOW):
            return True
        else:
            return False

    @allure.step('Нажимаем кнопку "Оформить заказ"')
    def click_make_order_button(self):
        self.driver.find_element(*MainPageLocators.MAKE_ORDER_BUTTON).click()

    @allure.step('Ждем всплывающее окно с деталями заказа')
    def wait_for_order_details_window(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(MainPageLocators.TITLE_ORDER_DETAILS_WINDOW))

    @allure.step('Проверяем заголовок модального окна "Детали заказа"')
    def check_order_details_window(self):
        if self.driver.find_element(*MainPageLocators.TITLE_ORDER_DETAILS_WINDOW):
            return True
        else:
            return False

    @allure.step('Закрываем всплывающее окно с деталями заказа')
    def close_order_details_window(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(MainPageLocators.CLOSE_BUTTON_DETAILS_WINDOW)).click()

    @allure.step('Получаем номер заказа из окна с деталями заказа')
    def get_order_number_details_window(self):
        WebDriverWait(self.driver, 10).until_not(expected_conditions.text_to_be_present_in_element(MainPageLocators.ORDER_NUMBER_DETAILS_WINDOW, '9999'))
        return (self.driver.find_element(*MainPageLocators.ORDER_NUMBER_DETAILS_WINDOW).text)

