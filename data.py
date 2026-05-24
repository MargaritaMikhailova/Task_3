class Urls:
    MAIN_PAGE = "https://qa-stellarburgers.education-services.ru"
    BASE_PAGE = f"{MAIN_PAGE}"
    LOGIN_PAGE = f"{MAIN_PAGE}/login"
    CREATE_USER_API = f"{MAIN_PAGE}/api/auth/register"
    USER = f"{MAIN_PAGE}/api/auth/user"
    FORGOT_PASSWORD = f"{MAIN_PAGE}/forgot-password"
    RESET_PASSWORD = f"{MAIN_PAGE}/reset-password"
    ACCOUNT_PAGE = f"{MAIN_PAGE}/account"
    USER_AUTH = f"{MAIN_PAGE}/account/profile"
    HISTORY_ORDER = f"{MAIN_PAGE}/account/order-history"
    ORDER_PAGE = f"{MAIN_PAGE}/feed"
    CONSTRUCTOR_PAGE = f"{MAIN_PAGE}/"


class Domain:
    DOMAIN = "mail.com"


class Ingredients:
    BUN = "Краторная булка"
    SOUCE = "Соус с шипами Антарианского плоскоходца"
    FILLING = "Хрустящие минеральные кольца"


class Indentificator_order:
    FEED_ALL = "Выполнено за все время:"
    FEED_TODAY = "Выполнено за сегодня:"
