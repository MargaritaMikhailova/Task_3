import re

import allure
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

from locators import Buttons, Pages, Parameter
from pages.main_page import BasePage
from helpers import extract_order_number


class OrderPage(BasePage):

    @allure.step("Открыть первый заказ в ленте")
    def open_first_order_in_feed(self):
        first_order = self.long_wait.until(
            EC.element_to_be_clickable(Buttons.FIRST_ORDER_IN_FEED)
        )
        self.driver.execute_script("arguments[0].click();", first_order)
        self.long_wait.until(EC.url_matches(r".*/feed/.+"))

    @allure.step("Получить раздел «В процессе»")
    def get_in_progress_section(self):
        return self.find_element(Pages.FEED_IN_PROGRESS_CONTAINER)

    @allure.step("Ожидание заказа в разделе «В процессе»")
    def wait_for_order_in_progress(self):
        self.long_wait.until(EC.presence_of_element_located(Pages.FEED_IN_PROGRESS_ORDER))

    @allure.step("Ожидание деталей заказа")
    def wait_for_order_detail(self):
        return self.long_wait.until(EC.presence_of_element_located(Pages.ORDER_DETAIL))

    @allure.step("Получение номера первого заказа в ленте")
    def get_first_order_number_in_feed(self) -> str:
        self.long_wait.until(EC.presence_of_element_located(Pages.FEED_ORDER_LIST))

        def order_number_ready(_):
            for order in self.driver.find_elements(*Pages.FEED_ORDER):
                numbers = order.find_elements(*Parameter.ORDER_DIGITS)
                if numbers:
                    number = extract_order_number(numbers[0].text)
                    if number:
                        return number
            return False

        return self.long_wait.until(order_number_ready)

    @allure.step("Парсинг значения счётчика")
    def parse_counter_value(self, text: str) -> int:
        digits = re.sub(r"\D", "", text)
        return int(digits) if digits else 0

    @allure.step("Получение значения счётчика")
    def get_counter(self, locator) -> int:
        try:
            element = self.driver.find_element(*locator)
            return self.parse_counter_value(element.text)
        except NoSuchElementException:
            return 0

    @allure.step("Получение счётчика «Всего»")
    def get_order_counter_all(self) -> int:
        return self.get_counter(Pages.FEED_COUNTER_ALL)

    @allure.step("Получение счётчика «За сегодня»")
    def get_order_counter_today(self) -> int:
        return self.get_counter(Pages.FEED_COUNTER_TODAY)

    @allure.step("Ожидание увеличения счётчика")
    def wait_for_counter_increase(self, get_counter, initial_value: int):
        def counter_grew(_):
            return get_counter() > initial_value

        self.long_wait.until(counter_grew)
