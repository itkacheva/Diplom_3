import requests
from urls import *


class IngredientAPI:

    def get_list_id_ingredient(self):
        response = requests.get(PagesUrls.main_page_url + IngredientsUrls.get_ingredients)
        list_ingredients = []
        for i in response.json()["data"]:
            list_ingredients.append(i['_id'])
        return list_ingredients
