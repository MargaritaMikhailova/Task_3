import pytest

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

from locators import Buttons, Pages

        
class BasePage: 

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.long_wait = WebDriverWait(driver, 45)
        self.actions = ActionChains(driver)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_clickable_element(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def close_modal_if_present(self):
        try:
            close_btn = self.wait.until(EC.element_to_be_clickable(Buttons.MODAL_CLOSE))
            self.driver.execute_script("arguments[0].click();", close_btn)
            self.wait.until(EC.invisibility_of_element_located(Pages.MODAL_PAGE))
        except TimeoutException:
            pass

    def click(self, locator):
        element = self.find_clickable_element(locator)
        element.click()

    def click_with_scroll(self, locator):
        element = self.find_clickable_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("arguments[0].click();", element)

    def input_text(self, locator, text):
        element = self.find_clickable_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.find_element(locator).text

    def is_element_visible(self, locator):
        return self.long_wait.until(EC.visibility_of_element_located(locator))

    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    def wait_for_url_contains(self, data):
        return self.long_wait.until(EC.url_contains(data))

    def switch_to_new_window(self):
        self.long_wait.until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def click_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def drag_and_drop(self, source_locator, target_locator):
        source = self.wait.until(EC.visibility_of_element_located(source_locator))
        target = self.wait.until(EC.visibility_of_element_located(target_locator))
        self.driver.execute_script(
            """
            const source = arguments[0];
            const target = arguments[1];
            const dataTransfer = new DataTransfer();
            ['dragstart', 'dragenter', 'dragover', 'drop', 'dragend'].forEach((type) => {
                const element = type === 'dragstart' ? source : target;
                element.dispatchEvent(
                    new DragEvent(type, { bubbles: true, cancelable: true, dataTransfer })
                );
            });
            """,
            source,
            target,
        )
    
    def get_current_url_page(self) -> str:
        return self.driver.current_url


