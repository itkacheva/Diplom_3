import time

from pages.order_feed_page import OrderFeedPage
from pages.login_page import LoginPage
from pages.main_page import MainPageBurgers
from pages.forget_password_page import *
from pages.personal_area_page import PersonalAreaPage


class TestPersonalArea:

    @allure.title('Проверка перехода в личный кабинет по клику на «Личный кабинет»')
    @allure.description('Проверяем, что система успешно совершает переход в личный кабинет')
    def test_go_personal_arear_page_by_Personal_Arear_button_success(self, driver, reg_user):
        mp = MainPageBurgers(driver)
        mp.wait_for_load_main_page()
        mp.click_personal_area_button()

        lp = LoginPage(driver)
        lp.set_value_email(reg_user.email)
        lp.set_value_password(reg_user.password)
        lp.click_enterece_button()

        pa = PersonalAreaPage(driver)
        pa.click_personal_area_button()
        time.sleep(3)
        data = pa.get_personal_area_data()

        assert reg_user.name == data["name"] and reg_user.email.upper() == data["email"].upper()

    @allure.title('Проверка перехода переход в раздел «История заказов»')
    @allure.description('Проверяем, что система успешно совершает '
                        'переход из личного кабинета в раздел «История заказов»')
    def test_go_history_orders_page_from_Personal_Arear_success(self, driver, reg_user):
        mp = MainPageBurgers(driver)
        mp.wait_for_load_main_page()
        mp.click_personal_area_button()

        lp = LoginPage(driver)
        lp.set_value_email(reg_user.email)
        lp.set_value_password(reg_user.password)
        lp.click_enterece_button()

        pa = PersonalAreaPage(driver)
        pa.click_personal_area_button()
        pa.click_feed_orders_button()

        of = OrderFeedPage(driver)
        of.wait_for_load_feed_orders_page()

        assert driver.current_url == of.get_feed_orders_page_url()

    @allure.title('Проверка выхода из аккаунта')
    @allure.description('Проверяем, что система успешно совершает выход из аккунта по кнопке "Выход"')
    def test_exit_from_Personal_Arear_success(self, driver, reg_user):
        mp = MainPageBurgers(driver)
        mp.wait_for_load_main_page()
        mp.click_personal_area_button()

        lp = LoginPage(driver)
        lp.set_value_email(reg_user.email)
        lp.set_value_password(reg_user.password)
        lp.click_enterece_button()

        pa = PersonalAreaPage(driver)
        pa.click_personal_area_button()
        pa.wait_for_personal_area_page()
        pa.click_exit_button()

        lp.wait_for_load_login_page()

        assert driver.current_url == lp.get_login_page_url()
