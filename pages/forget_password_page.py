import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


from locators.forget_password_locators import ForgetPageLocators
from pages.base_page import BasePage
from urls import PagesUrls


class ForgetPasswordPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ждем пока загрузится страница ввода email, для воостановления забытого пароля')
    def wait_for_load_login_page(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(ForgetPageLocators.INPUT_EMAIL))

    @allure.step('Нажимаем на кнопку "Восстановить"')
    def click_password_recovery_button(self):
        self.driver.find_element(*ForgetPageLocators.RECOVERY_BUTTON).click()

    @allure.step('Получаем  url страницы ввода email, для воостановления забытого пароля')
    def get_forget_password_page_url(self):
        return (PagesUrls.main_page_url+PagesUrls.forget_password_page_url)

    @allure.step('Вводим значение в поле EMAIL')
    def set_value_in_email(self, email):
        self.driver.find_element(*ForgetPageLocators.INPUT_EMAIL).send_keys(email)
