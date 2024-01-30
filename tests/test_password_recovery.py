from pages.login_page import LoginPage
from pages.main_page import MainPageBurgers
from pages.forget_password_page import *
from pages.reset_password_page import ResetPasswordPage


class TestPasswordRecovery:

    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль»')
    @allure.description('Проверяем, что система успешно совершает переход на страницу восстановления пароля')
    def test_go_password_recovery_page_by_Recover_Password_button_success(self, driver):
        mp = MainPageBurgers(driver)
        mp.wait_for_load_main_page()
        mp.click_entrance_in_account_button()

        lp = LoginPage(driver)
        lp.click_password_recovery_link()

        fp = ForgetPasswordPage(driver)
        fp.wait_for_load_login_page()

        assert driver.current_url == fp.get_forget_password_page_url()

    @allure.title('Проверка ввода почты и клик по кнопке «Восстановить» ')
    @allure.description('Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль», '
                  'ввод почты и клик по кнопке «Восстановить» ')
    def test_enter_email_and_click_Recover_button_success(self, driver, reg_user):
        mp = MainPageBurgers(driver)
        mp.wait_for_load_main_page()
        mp.click_entrance_in_account_button()

        lp = LoginPage(driver)
        lp.click_password_recovery_link()

        fp = ForgetPasswordPage(driver)
        fp.wait_for_load_login_page()
        fp.set_value_in_email(reg_user.email)
        fp.click_password_recovery_button()

        rp = ResetPasswordPage(driver)
        rp.wait_for_load_reset_password_page()

        assert driver.current_url == rp.get_reset_password_page_url() \
               and rp.get_place_holder_code_text() == 'Введите код из письма'

    @allure.title('Проверка клика по кнопке показать/скрыть пароль .')
    @allure.description('Проверяем то, что клик по кнопке показать/скрыть пароль '
                        'делает поле активным — подсвечивает его')
    def test_activity_check_input_password_success(self, driver):
        mp = MainPageBurgers(driver)
        mp.wait_for_load_main_page()
        mp.click_entrance_in_account_button()

        lp = LoginPage(driver)
        lp.wait_for_load_login_page()
        lp.click_password_recovery_link()

        fp = ForgetPasswordPage(driver)
        fp.click_password_recovery_button()

        rp = ResetPasswordPage(driver)
        rp.wait_for_load_reset_password_page()
        rp.click_show_hide_button()

        assert rp.check_active_input_password() == True and rp.check_stroke_active_input_password() == True


