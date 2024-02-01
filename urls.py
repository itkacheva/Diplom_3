class PagesUrls:
    main_page_url = "https://stellarburgers.nomoreparties.site/"
    login_page_url = "login"
    reset_password_page_url = "reset-password"
    forget_password_page_url = "forgot-password"
    personal_rea_page_url = "account/profile"
    history_orders_page_url = "feed"


class UserEndpointsUrls:
    login_page_url = "login"
    create_user_url = "api/auth/register"
    login_user_url = "api/auth/login"
    delete_user_url = "api/auth/user"


class OrderEndpointsUrls:
    create_order_url = "api/orders"
    get_data_order_url = "api/orders"


class IngredientsUrls:
    get_ingredients = "api/ingredients"