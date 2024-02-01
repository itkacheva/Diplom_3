import requests

from services.gen_fake_email import *
from services.gen_random_string import *
from urls import *


class UserAPI:
    def __init__(self):
        self.name = ''
        self.password = ''
        self.email = ''
        self.accessToken = ''
        self.user_data = {}

    def create_user_with_fake_data(self):
        user_data = self._gen_user_fake_data()
        response = requests.post(PagesUrls.main_page_url + UserEndpointsUrls.create_user_url, data=user_data)
        if response.status_code == 200:
            self.name = user_data["name"]
            self.password = user_data["password"]
            self.email = user_data["email"]
            self.accessToken = response.json()["accessToken"]
            self.user_data = user_data
        return response

    def _gen_user_fake_data(self):
        user_data = {"name": 'D3_3p_' + generate_random_string(10),
                     "password": 'D3_3p_' + generate_random_string(10),
                     "email": 'D3_3p_' + gen_fake_email()}
        return user_data

    def delete_user(self):
        self.login_user()
        headers = {'Authorization': self.accessToken}
        response = requests.delete(PagesUrls.main_page_url + UserEndpointsUrls.delete_user_url, headers=headers)
        return response

    def login_user(self):
        user_data = {"name": self.name,
                     "password": self.password,
                     "email": self.email}
        response = requests.post(PagesUrls.main_page_url + UserEndpointsUrls.login_user_url, data=user_data)
        if response.status_code == 200:
            self.accessToken = response.json()["accessToken"]
        return response