import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.login_page_locators import *
from pages.base_page import BasePage
from urls import PagesUrls


class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ждем пока загрузится страница авторизации')
    def wait_for_load_login_page(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(LoginPageLocators.ENTRANCE_BUTTON))

    @allure.step('Нажимаем на ссылку "Восстановить пароль"')
    def click_password_recovery_link(self):
        self.driver.find_element(*LoginPageLocators.PASSWORD_RECOVERY_LINK).click()

    @allure.step('Получаем  url страницы логина')
    def get_login_page_url(self):
        return (PagesUrls.main_page_url+PagesUrls.login_page_url)

    @allure.step('Нажимаем на кнопку показать/скрыть в поле ввода пароля')
    def click_show_hide_button(self):
        self.driver.find_element(*LoginPageLocators.SHOW_HIDE_BUTTON).click()

    @allure.step('Вводим значение в поле Email')
    def set_value_email(self, email):
        self.driver.find_element(*LoginPageLocators.INPUT_EMAIL).send_keys(email)

    @allure.step('Вводим значение в поле Пароль')
    def set_value_password(self, password):
        self.driver.find_element(*LoginPageLocators.INPUT_PASSWORD).send_keys(password)

    @allure.step('Нажимаем на кнопку "Войти"')
    def click_enterece_button(self):
        self.driver.find_element(*LoginPageLocators.ENTRANCE_BUTTON).click()

    @allure.step('Входим в систему')
    def login_user(self,reg_user):
        self.wait_for_load_login_page()
        self.set_value_email(reg_user.email)
        self.set_value_password(reg_user.password)
        self.click_enterece_button()

