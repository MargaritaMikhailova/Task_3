import pytest

from selenium import webdriver

class WebdriverFactory:
    @staticmethod
    def get_webdriver(browserName):
        if browserName == "firefox":
            return webdriver.Firefox()
        elif browserName == "chrome":
            return webdriver.Chrome()
