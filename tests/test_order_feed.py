import allure

from pages.login_page import LoginPage
from pages.main_page import MainPageBurgers
from pages.order_feed_page import OrderFeedPage
from pages.orders_history_user_page import OrdersHistoryPage
from pages.personal_area_page import PersonalAreaPage
from services.create_order import create_order
from services.list_compare import list_compare


class TestOrderFeed:

    @allure.title('Раздел «Лента заказов». Проверка открытия всплывающего окна с деталями заказа')
    @allure.description('Проверяем, что система успешно совершает переход в режим "Конструктор"')
    def test_open_pop_up_order_window_success(self, driver):

        mp = MainPageBurgers(driver)
        mp.wait_for_load_main_page()
        mp.click_feed_orders_button()

        ofp = OrderFeedPage(driver)
        ofp.wait_for_load_order_feed_page()
        ofp.click_random_order()
        ofp.wait_for_order_details_window()

        assert ofp.check_show_details_window() == True


    @allure.title('Раздел «Лента заказов». '
                  'Проверка отображания заказов из раздела «История заказов» на странице «Лента заказов»')
    @allure.description('Проверяем, что система отображает историю заказов пользователя на странице "Лента заказов')
    def test_check_history_orders_into_orders_food_success(self, driver, reg_user):
        create_order(reg_user)

        mp = MainPageBurgers(driver)
        mp.wait_for_load_main_page()
        mp.click_personal_area_button()

        lp = LoginPage(driver)
        lp.login_user(reg_user)
        mp.click_personal_area_button()

        pap = PersonalAreaPage(driver)
        pap.wait_for_personal_area_page()
        pap.click_history_orders()

        ohp = OrdersHistoryPage(driver)
        ohp.wait_for_load_orders_history_page()
        list_orders_user = ohp.get_list_orders_user()
        ohp.click_feed_orders_button()

        ofp = OrderFeedPage(driver)
        ofp.wait_for_load_feed_orders_page()
        list_orders_all=ofp.get_list_orders()

        assert list_compare(list_orders_user, list_orders_all)

    @allure.title('Раздел «Лента заказов». Проверка увеличения счётчик "Выполнено за всё время" при создании заказа')
    @allure.description('Проверяем, что система увеличивает значение счетчика при оформлении нового заказа')
    def test_check_increasing_counter_all_time_value_success(self, driver, reg_user):
        mp = MainPageBurgers(driver)
        mp.wait_for_load_main_page()
        mp.click_personal_area_button()

        lp = LoginPage(driver)
        lp.login_user(reg_user)

        mp.click_feed_orders_button()

        ofp = OrderFeedPage(driver)
        ofp.wait_for_load_feed_orders_page()
        current_count=ofp.get_count_all_time()

        ofp.make_order(mp)
        mp.click_feed_orders_button()
        ofp.wait_for_load_feed_orders_page()
        new_count = ofp.get_count_all_time()

        assert (new_count - current_count) == 1

    @allure.title('Раздел «Лента заказов». Проверка увеличения счётчик "Выполнено за сегодня" при создании заказа')
    @allure.description('Проверяем, что система увеличивает значение счетчика при оформлении нового заказа')
    def test_check_increasing_counter_today_value_success(self, driver, reg_user):
        mp = MainPageBurgers(driver)
        mp.wait_for_load_main_page()
        mp.click_personal_area_button()

        lp = LoginPage(driver)
        lp.login_user(reg_user)

        mp.click_feed_orders_button()

        ofp = OrderFeedPage(driver)
        ofp.wait_for_load_feed_orders_page()
        current_count=ofp.get_count_today()

        ofp.make_order(mp)
        mp.click_feed_orders_button()
        ofp.wait_for_load_feed_orders_page()
        new_count = ofp.get_count_today()

        assert (new_count - current_count) == 1

    @allure.title('Раздел «Лента заказов». Проверка номера заказа в разделе "В работе"')
    @allure.description('Проверяем, что после оформления заказа его номер появляется в разделе В работе')
    def test_check_order_number_success(self, driver, reg_user):
        mp = MainPageBurgers(driver)
        mp.wait_for_load_main_page()
        mp.click_personal_area_button()

        lp = LoginPage(driver)
        lp.login_user(reg_user)

        mp.click_feed_orders_button()

        ofp = OrderFeedPage(driver)
        ofp.wait_for_load_feed_orders_page()

        number_order1 = ofp.make_order(mp)
        mp.click_feed_orders_button()
        ofp.wait_for_load_feed_orders_page()
        number_order2 = ofp.get_order_number_in_work()

        assert number_order1 == number_order2

