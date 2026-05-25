import random

from selenium.webdriver.support import expected_conditions as EC

from locators import Parameter, Buttons, Pages, Links
from pages.main_page import BasePage
from helpers import random_string, extract_order_number
from data import Urls


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def wait_for_load_page(self):
        return self.find_element(Pages.LOGIN_PAGE)

    def click_login_page(self):
        self.close_modal_if_present()
        self.click_with_scroll(Buttons.LOGIN_BUTTON)

    def is_modal_closed(self):
        self.wait.until(EC.invisibility_of_element_located(Pages.MODAL_PAGE))
        return True

    def click_personal_account(self):
        self.close_modal_if_present()
        self.click_with_scroll(Buttons.LOGIN_BUTTON)

    def wait_for_account_page(self):
        self.wait_for_url_contains(Urls.ACCOUNT_PAGE)

    def wait_for_profile_page(self):
        self.wait_for_account_page()
        if Urls.USER_AUTH not in self.driver.current_url:
            self.wait_for_url_contains(Urls.USER_AUTH)

    def wait_for_login_page(self):
        return self.wait_for_url_contains(Urls.LOGIN_PAGE)

    def click_login_button(self):
        self.click_to_element(Buttons.LOGIN)

    def fill_authorization(self, user):
        self.input_text(Parameter.EMAIL, user["email"])
        self.input_text(Parameter.PASSWORD, user["password"]) 

    def click_link_registr(self):
        self.click(Links.REGISTR_USER)

    def click_link_update_password(self):
        self.click(Links.UPDATE_PASSWORD)

    def click_eyes(self):
        self.click_to_element(Buttons.EYES)
    
    def create_user(self, user):
        self.input_text(Parameter.EMAIL, user["email"])
        self.input_text(Parameter.PASSWORD, user["password"]) 
        self.input_text(Parameter.NAME, user["name"])
    
    def create_user_button(self):
        self.click(Buttons.REGISTR_BUTTON)

    def update_password_fill(self, user):
        self.input_text(Parameter.EMAIL, user["email"])

    def login_link(self):
        self.click(Links.LOGIN_LINK)

    def update_button(self):
        self.click(Buttons.UPDATE_BUTTON)
        return self.wait_for_url_contains(Urls.RESET_PASSWORD)

    def page_reset_password(self, user):
        code = random_string()
        self.input_text(Parameter.UPDATE_PASSWORD, user["password"])
        self.input_text(Parameter.CODE, code) 

    def button_eyes_focused(self):
        return self.find_element(Buttons.EYES_FOCUSED)
    
    def find_update_password_element(self):
        return self.find_element(Parameter.UPDATE_PASSWORD)
    
    def find_password_element(self):
        return self.find_element(Parameter.PASSWORD)
    
    def history_order_page(self):
        return self.find_element(Pages.ORDER_PAGE)
    
    def history_order_button(self):
        self.close_modal_if_present()
        self.click_with_scroll(Buttons.ORDER_HISTORY_BUTTON)

    def logout_button_check(self):
        self.click(Buttons.LOGOUT)
        return self.wait_for_login_page()
    
    def login_history_order(self):
        self.find_element(Pages.ORDER_HISTORY_LINK)

    def open_order_history(self):
        self.click_personal_account()
        self.history_order_button()
        self.wait_for_url_contains(Urls.HISTORY_ORDER)

    def scroll_order_history_js(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_order_history(self):
        self.scroll_to_element(Parameter.USER_ORDER_HISTORY)

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
    