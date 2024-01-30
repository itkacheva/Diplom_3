import pytest
from selenium import webdriver
from endpoints.user_endpoints import UserAPI
from urls import *


@pytest.fixture()
def driver(request):
    browser = request.config.getoption("--browser")
    if 'chrome' in browser.lower():
        driver = webdriver.Chrome()
    elif 'firefox' in browser.lower():
        driver = webdriver.Firefox()
    else:
        raise ValueError('Указан неверный браузер')
    driver.maximize_window()
    driver.get(PagesUrls.main_page_url)
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store")


@pytest.fixture()
def reg_user():
    user = UserAPI()
    user.create_user_with_fake_data()
    yield user
    user.delete_user()