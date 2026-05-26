import pytest
import requests

from data import Urls
from factory import WebdriverFactory
from helpers import random_string, random_string_email
from pages.constructor_page import ConstructorPage
from pages.login_page import LoginPage
from pages.order_page import OrderPage

@pytest.fixture(params=["firefox", "chrome"])
def driver(request):
    browser_name = request.param
    driver = WebdriverFactory.get_webdriver(browser_name)
    driver.get(Urls.MAIN_PAGE)

    yield driver

    driver.quit()

@pytest.fixture
def user():
    payload = {
    'email' : random_string_email(),
    'password' : random_string(),
    'name' : random_string()
    }

    create_resp = requests.post(Urls.CREATE_USER_API, json=payload, timeout=30)
    assert create_resp.status_code == 200, create_resp.text
    token = create_resp.json().get("accessToken")

    user_data = {
        "email": payload["email"],
        "password": payload["password"],
        "name": payload["name"],
        "token": token,
        "create_response": create_resp
     
    }

    yield user_data

    try:
        headers = {"Authorization": token}
        requests.delete(Urls.USER, headers=headers, timeout=30)
    except Exception:
        pass


@pytest.fixture
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture
def constructor_page(driver):
    return ConstructorPage(driver)


@pytest.fixture
def order_page(driver):
    return OrderPage(driver)


@pytest.fixture
def authorized_user(login_page, user):
    login_page.click_login_page()
    login_page.wait_for_load_page()
    login_page.fill_authorization(user)
    login_page.click_login_button()
    return user
