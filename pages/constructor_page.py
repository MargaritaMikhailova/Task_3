

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

from locators import Pages, Buttons, Parameter
from pages.main_page import BasePage
from data import Ingredients, Urls
from helpers import counter_by_ingredient, extract_order_number, ingredient_by_name


class ConstructorPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def wait_for_load_page(self):
        return self.find_element(Pages.LOGIN_PAGE)

    def click_bun_tab(self):
        self.click_to_element(Buttons.BUN_BUTTON)

    def click_souce_tab(self):
        self.click_to_element(Buttons.SOUCE_BUTTON)

    def click_filling_tab(self):
        self.click_to_element(Buttons.FILLING_BUTTON)

    def click_constructor_page(self):
        self.close_modal_if_present()
        self.click_with_scroll(Buttons.CONSTRUCTOR_PAGE)

    def click_burger_ingredients(self, ingredient_name: str = Ingredients.BUN):
        self.click_to_element(ingredient_by_name(ingredient_name))
        return self.find_element(Pages.MODAL_PAGE)

    def create_order_button(self):
        self.click(Buttons.CREATE_ORDER)
        self.long_wait.until(EC.visibility_of_element_located(Pages.MODAL_PAGE))

    def clean_order_button(self):
        self.click(Buttons.CLEAN_BUTTON)

    def get_menu_element(self):
        return self.find_element(Pages.BURGER_MENU_PAGE)

    def get_order_bucket_element(self):
        return self.find_element(Pages.BURDER_CONSTRUCTOR_BUCKET)

    def drag_and_drop_element(self, ingredient_name: str = Ingredients.BUN):
        self.drag_and_drop(ingredient_by_name(ingredient_name), Pages.BURDER_CONSTRUCTOR_BUCKET)

    def create_default_order(self):
        self.click_constructor_page()
        self.click_bun_tab()
        self.drag_and_drop_element(Ingredients.BUN)
        self.click_souce_tab()
        self.drag_and_drop_element(Ingredients.SOUCE)
        self.create_order_button()

    def click_order_page_button(self):
        self.close_modal_if_present()
        self.click_with_scroll(Buttons.ORDER_PAGE_BUTTON)
        self.wait.until(EC.url_contains(Urls.ORDER_PAGE))
        self.long_wait.until(EC.presence_of_element_located(Pages.FEED_ORDER_LIST))

    def get_ingredient_counter(self, ingredient_name: str = Ingredients.BUN) -> int:
        try:
            text = self.get_text(counter_by_ingredient(ingredient_name))
            return int(text) if text.isdigit() else 0
        except TimeoutException:
            return 0

    def wait_for_ingredient_counter_increase(self, ingredient_name: str, initial_value: int):
        def counter_increased(_):
            return self.get_ingredient_counter(ingredient_name) > initial_value

        self.long_wait.until(counter_increased)

    def modal_window_order(self):
        return self.wait.until(EC.visibility_of_element_located(Pages.MODAL_PAGE))

    def get_order_number(self) -> str:
        element = self.wait.until(EC.visibility_of_element_located(Parameter.ORDER_NUMBER))
        return extract_order_number(element.text)

    def is_modal_displayed(self):
        try:
            self.wait.until(EC.visibility_of_element_located(Pages.MODAL_PAGE))
            return True
        except Exception:
            return False

