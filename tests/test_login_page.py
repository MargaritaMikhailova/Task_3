import pytest
import allure

from pages.login_page import LoginPage
from data import Urls

class TestLoginPage:

    @allure.title('Проверить Личный кабинет')
    @allure.description('Проверить: переход по клику в личный кабинет авторизованным пользователем')
    def test_login_page_auth_user(self, driver, user, authorized_user, login_page):
        login_page.close_modal_if_present()
        login_page.wait_for_load_page()
        login_page.click_login_page()
        login_page.wait_for_profile_page()
  
     
        assert driver.current_url == Urls.USER_AUTH

    @allure.title('Проверить Личный кабинет')
    @allure.description('Проверить: переход в раздел "История заказов"')
    def test_order_page_history(self, driver, user, authorized_user, login_page):
        login_page.close_modal_if_present()
        login_page.wait_for_load_page()
        login_page.click_login_page()
        login_page.close_modal_if_present()
        login_page.history_order_button()
        login_page.history_order_page()


        assert driver.current_url == Urls.HISTORY_ORDER

    @allure.title('Проверить Личный кабинет')
    @allure.description('Проверить: выход из аккаунта')
    def test_logot_page(self, driver, user, authorized_user, login_page):
        login_page.close_modal_if_present()
        login_page.wait_for_load_page()
        login_page.click_login_page()
        login_page.close_modal_if_present()
        login_page.logout_button_check()


        assert driver.current_url == Urls.LOGIN_PAGE