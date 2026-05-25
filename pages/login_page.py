import random
import allure

from selenium.webdriver.support import expected_conditions as EC

from locators import Parameter, Buttons, Pages, Links
from pages.main_page import BasePage
from helpers import random_string, extract_order_number
from data import Urls


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Ожидание загрузки главной страницы")
    def wait_for_load_page(self):
        return self.find_element(Pages.LOGIN_PAGE)

    @allure.step("Открытие личного кабинета")
    def click_login_page(self):
        self.close_modal_if_present()
        self.click_with_scroll(Buttons.LOGIN_BUTTON)

    @allure.step("Ожидание закрытия модального окна")
    def is_modal_closed(self):
        self.wait.until(EC.invisibility_of_element_located(Pages.MODAL_PAGE))
        return True

    @allure.step('Ожидание страницы личного кабинета (URL содержит "/account")')
    def wait_for_account_page(self):
        self.wait_for_url_contains(Urls.ACCOUNT_PAGE)

    @allure.step('Ожидание страницы профиля (URL содержит "/account/profile")')
    def wait_for_profile_page(self):
        self.wait_for_account_page()
        if Urls.USER_AUTH not in self.driver.current_url:
            self.wait_for_url_contains(Urls.USER_AUTH)

    @allure.step('Ожидание страницы входа (URL содержит "/login")')
    def wait_for_login_page(self):
        return self.wait_for_url_contains(Urls.LOGIN_PAGE)

    @allure.step("Клик по кнопке «Войти»")
    def click_login_button(self):
        self.click_to_element(Buttons.LOGIN)

    @allure.step("Заполнение данных для авторизации")
    def fill_authorization(self, user):
        self.input_text(Parameter.EMAIL, user["email"])
        self.input_text(Parameter.PASSWORD, user["password"])

    @allure.step("Клик по ссылке «Зарегистрироваться»")
    def click_link_registr(self):
        self.click(Links.REGISTR_USER)

    @allure.step("Клик по ссылке «Восстановить пароль»")
    def click_link_update_password(self):
        self.click(Links.UPDATE_PASSWORD)

    @allure.step("Клик по иконке «Показать пароль»")
    def click_eyes(self):
        self.click_to_element(Buttons.EYES)

    @allure.step("Заполнение формы регистрации пользователя")
    def create_user(self, user):
        self.input_text(Parameter.EMAIL, user["email"])
        self.input_text(Parameter.PASSWORD, user["password"])
        self.input_text(Parameter.NAME, user["name"])

    @allure.step("Клик по кнопке «Зарегистрироваться»")
    def create_user_button(self):
        self.click(Buttons.REGISTR_BUTTON)

    @allure.step("Заполнение поля email для восстановления пароля")
    def update_password_fill(self, user):
        self.input_text(Parameter.EMAIL, user["email"])

    @allure.step("Клик по ссылке «Личный кабинет»")
    def login_link(self):
        self.click(Links.LOGIN_LINK)

    @allure.step("Клик по кнопке «Восстановить»")
    def update_button(self):
        self.click(Buttons.UPDATE_BUTTON)
        return self.wait_for_url_contains(Urls.RESET_PASSWORD)

    @allure.step("Заполнение нового пароля и кода восстановления")
    def page_reset_password(self, user):
        code = random_string()
        self.input_text(Parameter.UPDATE_PASSWORD, user["password"])
        self.input_text(Parameter.CODE, code)

    @allure.step("Проверка иконки «Показать пароль» в активном состоянии")
    def button_eyes_focused(self):
        return self.find_element(Buttons.EYES_FOCUSED)

    @allure.step("Поиск поля пароля в разделе «Восстановить пароль»")
    def find_update_password_element(self):
        return self.find_element(Parameter.UPDATE_PASSWORD)

    @allure.step("Поиск поля «Пароль»")
    def find_password_element(self):
        return self.find_element(Parameter.PASSWORD)

    @allure.step("Поиск раздела «История заказов» в личном кабинете")
    def history_order_page(self):
        return self.find_element(Pages.ORDER_PAGE)

    @allure.step("Переход в раздел «История заказов»")
    def history_order_button(self):
        self.close_modal_if_present()
        self.click_with_scroll(Buttons.ORDER_HISTORY_BUTTON)

    @allure.step("Клик по кнопке «Выход»")
    def logout_button_check(self):
        self.click(Buttons.LOGOUT)
        return self.wait_for_login_page()

    @allure.step("Поиск ссылки на историю заказов в личном кабинете")
    def login_history_order(self):
        self.find_element(Pages.ORDER_HISTORY_LINK)

    @allure.step('Ожидание страницы истории заказов (URL содержит "/account/order/history")')
    def open_order_history(self):
        self.click_login_page()
        self.history_order_button()
        self.wait_for_url_contains(Urls.HISTORY_ORDER)

    @allure.step("Прокрутка страницы истории заказов (JavaScript)")
    def scroll_order_history_js(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    @allure.step("Прокрутка до списка заказов в истории")
    def scroll_order_history(self):
        self.scroll_to_element(Parameter.USER_ORDER_HISTORY)

    @allure.step("Получение номера последнего заказа из истории")
    def get_last_order_number_in_history(self) -> str:
        self.wait_for_url_contains(Urls.HISTORY_ORDER)

        def order_number_ready(_):
            for order in self.driver.find_elements(*Parameter.USER_ORDER_HISTORY):
                numbers = order.find_elements(*Parameter.ORDER_DIGITS)
                if numbers:
                    number = extract_order_number(numbers[0].text)
                    if number:
                        return number
            return False

        return self.long_wait.until(order_number_ready)
