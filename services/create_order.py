from endpoints.order_endpoints import OrderAPI
from services.gen_ingredients_data import gen_ingredients_data


def create_order(user):
    OrderAPI().create_order_with_authorization(gen_ingredients_data(), user)
