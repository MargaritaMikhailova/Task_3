import allure

from data import Urls


class TestOrderPageFunctional:

    @allure.title('Проверка раздела "Лента заказов"')
    @allure.description('Проверить: если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_open_order_details_modal(self, driver, authorized_user, order_page, constructor_page):
        constructor_page.create_default_order()
        constructor_page.click_order_page_button()

        order_page.open_first_order_in_feed()
        order_page.wait_for_order_detail()

        assert f"{Urls.ORDER_PAGE}/" in order_page.get_current_url_order_page()

    @allure.title('Проверка раздела "Лента заказов"')
    @allure.description('Проверить: заказы пользователя из раздела "История заказов"отображаются на странице "Лента заказов"')
    def test_order_number_matches_history(self, authorized_user, order_page, constructor_page, login_page):
        constructor_page.create_default_order()
        login_page.close_modal_if_present()
        constructor_page.click_order_page_button()

        order_number_in_feed = order_page.get_first_order_number_in_feed()

        login_page.open_order_history()
        login_page.scroll_order_history_js()
        order_number_in_history = login_page.get_last_order_number_in_history()

        assert order_number_in_feed == order_number_in_history

    @allure.title('Проверка раздела "Лента заказов"')
    @allure.description('Проверить: при создании нового заказа счетчик "Выполнено за все время" увеличивается')
    def test_check_all_order(self, authorized_user, order_page, constructor_page):
        constructor_page.click_order_page_button()
        initial_counter = order_page.get_order_counter_all()

        constructor_page.create_default_order()
        constructor_page.click_order_page_button()

        order_page.wait_for_counter_increase(order_page.get_order_counter_all,initial_counter)
        assert order_page.get_order_counter_all() > initial_counter

    @allure.title('Проверка раздела "Лента заказов"')
    @allure.description('Проверить: при создании нового заказа счетчик "Выполнено за сегодня" увеличивается')
    def test_check_today_order(self, authorized_user, order_page, constructor_page):
        constructor_page.click_order_page_button()
        initial_counter = order_page.get_order_counter_today()

        constructor_page.create_default_order()
        constructor_page.click_order_page_button()

        order_page.wait_for_counter_increase(order_page.get_order_counter_today,initial_counter)
        assert order_page.get_order_counter_today() > initial_counter

    @allure.title('Проверка раздела "Лента заказов"')
    @allure.description('Проверить: после оформления заказа его номер появляется в разделе "В работе"')
    def test_order_appears_in_progress(
        self, authorized_user, order_page, constructor_page
    ):
        constructor_page.create_default_order()
        constructor_page.click_order_page_button()

        order_page.wait_for_order_in_progress()
        assert order_page.get_in_progress_section().is_displayed()
