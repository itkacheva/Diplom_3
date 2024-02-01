from pages.order_feed_page import OrderFeedPage
from pages.login_page import LoginPage
from pages.main_page import MainPageBurgers
from pages.forget_password_page import *


class TestMainFanctional:

    @allure.title('Проверка перехода по клику на «Конструктор»')
    @allure.description('Проверяем, что система успешно совершает переход в режим "Конструктор"')
    def test_go_to_constructor_page_success(self, driver):
        mp = MainPageBurgers(driver)
        mp.wait_for_load_main_page()
        mp.click_feed_orders_button()
        mp.click_constructor_button()

        assert driver.current_url == mp.get_main_page_url() \
               and mp.check_title_container_ingredients() == True

    @allure.title('Проверка перехода по клику на «Лента заказов»')
    @allure.description('Проверяем, что система успешно совершает переход в режим «Лента заказов»')
    def test_go_to_history_orders_page_success(self, driver):
        mp = MainPageBurgers(driver)
        mp.wait_for_load_main_page()
        mp.click_feed_orders_button()

        oh = OrderFeedPage(driver)
        oh.wait_for_load_feed_orders_page()

        assert driver.current_url == oh.get_feed_orders_page_url()

    @allure.title('Проверка всплывающего окна с деталями по клику на ингридиент')
    @allure.description('Проверяем,что если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_pop_up_window_by_click_success(self, driver):
        mp = MainPageBurgers(driver)
        mp.wait_for_load_main_page()
        mp.click_random_ingredient()
        mp.wait_for_ingredient_details_window()

        assert mp.check_ingredient_details_window() == True

    @allure.title('Проверка закрытия всплывающего окна с деталями ингридиента по клику на крестик')
    @allure.description('Проверяем,что если кликнуть на крестик,всплывающее окно с деталями ингридиента закрывается')
    def test_close_pop_up_window_success(self, driver):
        mp = MainPageBurgers(driver)
        mp.wait_for_load_main_page()
        mp.click_random_ingredient()
        mp.wait_for_ingredient_details_window()
        mp.close_ingredient_details_window()

        assert mp.check_title_container_ingredients()

    @allure.title('Проверка увеличения счетчика при добавлении ингредиента в заказ')
    @allure.description('Добавляем ингридиент в заказ и проверяем, что счетчик увеличился')
    def test_counter_increase_success(self, driver):
        mp = MainPageBurgers(driver)
        mp.wait_for_load_main_page()
        counter = (mp.add_random_ingredient_in_order())

        assert int(counter) > 0

    @allure.title('Проверяем, что залогиненный пользователь может оформить заказ.')
    @allure.description('Осуществляем вход в систему и создаем заказ')
    def test_add_order_by_auth_user_success(self, driver, reg_user):
        mp = MainPageBurgers(driver)
        mp.wait_for_load_main_page()
        mp.click_personal_area_button()

        lp = LoginPage(driver)
        lp.login_user(reg_user)

        mp.wait_for_load_main_page()
        mp.add_random_ingredient_in_order()
        mp.click_make_order_button()
        mp.wait_for_order_details_window()

        assert mp.check_order_details_window() == True