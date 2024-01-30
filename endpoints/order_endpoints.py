import requests

from urls import *


class OrderAPI:

    def create_order_without_authorization(self, order_data):
        response = requests.post(PagesUrls.main_page_url + OrderEndpointsUrls.create_order_url, data=order_data)
        return response

    def create_order_with_authorization(self, order_data, user):
        response_login = user.login_user()
        headers = {
            'Authorization': response_login.json()["accessToken"]
        }
        response = requests.post(PagesUrls.main_page_url + OrderEndpointsUrls.create_order_url, data=order_data, headers=headers)
        return response

    def get_data_order_by_user_name_with_authorization(self, user):
        response_login = user.login_user()
        headers = {
            'Authorization': response_login.json()["accessToken"]
        }
        response = requests.get(PagesUrls.main_page_url + OrderEndpointsUrls.get_data_order_url, headers=headers)
        return response

    def get_data_order_by_user_name_without_authorization(self):
        response = requests.get(PagesUrls.main_page_url + OrderEndpointsUrls.get_data_order_url)
        return response
