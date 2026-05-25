import pytest
import allure

from pages.login_page import LoginPage
from data import Urls

class TestUpdatePassword:

    @allure.title('Проверить страницу "Восстановления пароля"')
    @allure.description('Проверить: Переход на страницу восстановление пароля по кнопке "Восстановить пароль"')
    def test_update_password_link(self, driver):
        login_page = LoginPage(driver)

        login_page.click_login_page()
        login_page.wait_for_load_page()

        login_page.click_link_update_password()

        assert driver.current_url == Urls.FORGOT_PASSWORD

    
    @allure.title('Проверить страницу "Восстановления пароля"')
    @allure.description('Проверить: Ввод почты и клик по кнопке "Восстановить"')
    def test_update_password_page(self, driver, user):
        login_page = LoginPage(driver)

        login_page.click_login_page()
        login_page.wait_for_load_page()
        login_page.click_link_update_password()
        login_page.update_password_fill(user)
        
        login_page.update_button()
     
        assert driver.current_url == Urls.RESET_PASSWORD

    @allure.title('Проверить клик по кнопке показать\скрыть пароль')
    @allure.description('Проверить: клик по кнопке показать\скрыть пароль на странице "Вход"')
    def test_eyes_buttons_login(self, driver, user):
        login_page = LoginPage(driver)

        login_page.click_login_page()
        login_page.wait_for_load_page()
        login_page.fill_authorization(user)
        not_visible_password = login_page.find_password_element()
        assert not_visible_password.get_attribute("type") == "password"

        login_page.click_eyes()
        visible_password = login_page.find_password_element()
        assert visible_password.get_attribute("type") == "text"
        

    @allure.title('Проверить клик по кнопке показать\скрыть пароль')
    @allure.description('Проверить: клик по кнопке показать\скрыть пароль на странице "Регистрация"')
    def test_eyes_buttons_authorization(self, driver, user):
        login_page = LoginPage(driver)

        login_page.click_login_page()
        login_page.wait_for_load_page()
        login_page.click_link_registr()
        login_page.create_user(user)
        not_visible_password = login_page.find_password_element()
        assert not_visible_password.get_attribute("type") == "password"

        login_page.click_eyes()
        visible_password = login_page.find_password_element()
        assert visible_password.get_attribute("type") == "text"

    @allure.title('Проверить клик по кнопке показать\скрыть пароль')
    @allure.description('Проверить: клик по кнопке показать\скрыть пароль на странице "Восстановление пароля"')
    def test_eyes_buttons_reset_password(self, driver, user):
        login_page = LoginPage(driver)

        login_page.click_login_page()
        login_page.wait_for_load_page()
        login_page.click_link_update_password()
        login_page.update_password_fill(user)
        login_page.update_button()
        login_page.page_reset_password(user)

        not_visible_password = login_page.find_update_password_element()
        assert not_visible_password.get_attribute("type") == "password"

        login_page.click_eyes()
        visible_password = login_page.find_update_password_element()
        assert visible_password.get_attribute("type") == "text"



