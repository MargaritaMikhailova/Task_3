import pytest
import allure


from data import Urls, Ingredients


class TestMainFunctional:

    @allure.title('Проверка основного функционала')
    @allure.description('Проверить: переход по клику на "Конструктор"')
    def test_link_constructor_exist(self, driver, user, authorized_user, constructor_page, login_page):
        constructor_page.click_constructor_page()

        assert constructor_page.get_current_url_constructor_page() == Urls.CONSTRUCTOR_PAGE

    @allure.title('Проверка основного функционала')
    @allure.description('Проверить: переход по клику на "Лента заказов"')
    def test_link_order_exist(self, driver, user, authorized_user, constructor_page, login_page):
        constructor_page.click_order_page_button()

        assert constructor_page.get_current_url_constructor_page() == Urls.ORDER_PAGE

    @allure.title('Проверка основного функционала')
    @allure.description('Проверить: если кликнуть на элемент появится всплывающее окно с деталями')
    def test_check_constructor_modal(self, driver, user, authorized_user, constructor_page, login_page):
        constructor_page.click_constructor_page()

        modal_window = constructor_page.click_burger_ingredients()

        assert modal_window.is_displayed()

    @allure.title('Проверка основного функционала')
    @allure.description('Проверить: всплывающее окно закрывается кликом по крестику')
    def test_check_constructor_modal_not_displayed(self, driver, user, authorized_user, constructor_page, login_page):
        constructor_page.click_constructor_page()
        constructor_page.click_burger_ingredients()
        login_page.close_modal_if_present()

        assert login_page.is_modal_closed()

    @allure.title('Проверка основного функционала')
    @allure.description('Проверить: при добавлении ингредиента в заказ увеличивается каунтер данного ингредиента')
    def test_check_ingredient_counter_increases(self, driver, user, authorized_user, constructor_page, login_page):
        constructor_page.click_constructor_page()
        initial_counter = constructor_page.get_ingredient_counter(Ingredients.BUN)
        constructor_page.drag_and_drop_element(Ingredients.BUN)
        constructor_page.wait_for_ingredient_counter_increase(Ingredients.BUN, initial_counter)

        assert constructor_page.get_ingredient_counter(Ingredients.BUN) > initial_counter

    @allure.title('Проверка основного функционала')
    @allure.description('Проверить: залогиненный пользователь может оформить заказ')
    def test_check_create_order(self, driver, user, authorized_user, constructor_page, login_page):
        constructor_page.click_constructor_page()
        constructor_page.drag_and_drop_element(Ingredients.BUN)
        constructor_page.drag_and_drop_element(Ingredients.SOUCE)
        constructor_page.create_order_button()

        modal_order_window = constructor_page.modal_window_order()

        assert modal_order_window.is_displayed()
        order_number = constructor_page.get_order_number()
        print(f"Номер заказа:{order_number}")



        
   
