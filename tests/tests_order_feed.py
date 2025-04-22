import pytest
import allure
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from pages.order_history_page import OrderHistoryPage
from pages.order_feed_page import OrderFeedPage
from pages.main_page import MainPage
from urls import Urls


class TestOrderFeed:
    @allure.title('Тест на то, что после оформления заказа его номер появляется в разделе В работе.')
    @allure.description(
        'Логинимся на сайте, оформляем заказ, ожидаем что его номер окажется в ленте заказов в блоке в работе.')
    def test_new_order_up_in_order_in_work_success(self, get_client_data):
        main_page = MainPage(self.driver)
        login_page = LoginPage(self.driver)
        order_feed_page = OrderFeedPage(self.driver)
        profile_page = ProfilePage(self.driver)
        order_history_page = OrderHistoryPage(self.driver)
        login_page.open_login_page()
        login_page.click_on_email_field()
        login_page.set_email_field(get_client_data.email)
        login_page.click_on_password_field()
        login_page.set_password_field(get_client_data.password)
        login_page.click_on_entry_button()
        login_page.wait_url_changes(Urls.login_page)
        main_page.click_on_construct_button()
        main_page.move_ingredient_to_basket()
        main_page.click_on_order_button()
        login_page.open_login_page()
        main_page.click_on_profile_button()
        main_page.wait_url_changes(Urls.main_page)
        profile_page.click_on_order_history_button()
        profile_page.wait_url_changes(Urls.profile_page)
        order_number_in_history = order_history_page.get_order_number()
        order_history_page.click_on_order_feed_button()
        order_history_page.wait_url_changes(Urls.order_history_page)
        assert order_number_in_history[1:] in order_feed_page.get_order_number_in_work()

    @allure.title('Тест на то, что если кликнуть на заказ, откроется всплывающее окно с деталями')
    @allure.description(
        'Заходим на сайт. Переходим в раздел ленты заказов. Проверяем, что при нажатии на первый заказ откроется окно с его деталями.')
    def test_new_order_up_order_count_all_time_success(self):
        main_page = MainPage(self.driver)
        order_feed_page = OrderFeedPage(self.driver)
        main_page.open_main_page()
        main_page.click_on_order_feed_button()
        main_page.wait_url_changes(Urls.main_page)
        order_feed_page.click_on_first_order()
        assert order_feed_page.check_visibility_window_order_detail()

    @allure.title('Тест на то, что при создании нового заказа счётчик Выполнено за всё время увеличивается.')
    @allure.description(
        'Логинимся на сайте, сохраняем начальное кол-во заказов за все время, создаем новый заказ и проверяем, что текущее значение счетчика заказов за все время больше, чем сохраненое значение.')
    def test_new_order_up_order_count_all_time_success(self, get_client_data):
        main_page = MainPage(self.driver)
        login_page = LoginPage(self.driver)
        order_feed_page = OrderFeedPage(self.driver)
        login_page.open_login_page()
        login_page.click_on_email_field()
        login_page.set_email_field(get_client_data.email)
        login_page.click_on_password_field()
        login_page.set_password_field(get_client_data.password)
        login_page.click_on_entry_button()
        login_page.wait_url_changes(Urls.login_page)
        main_page.click_on_order_feed_button()
        main_page.wait_url_changes(Urls.main_page)
        initial_order_count_done_all_time = order_feed_page.get_order_count_done_all_time()
        order_feed_page.click_on_construct_button()
        order_feed_page.wait_url_changes(Urls.order_feed_page)
        main_page.move_ingredient_to_basket()
        main_page.click_on_order_button()
        main_page.wait_visibility_image_order_create()
        login_page.open_login_page()
        main_page.click_on_order_feed_button()
        main_page.wait_url_changes(Urls.main_page)
        assert order_feed_page.get_order_count_done_all_time() > initial_order_count_done_all_time

    @allure.title('Тест на то, что при создании нового заказа счётчик Выполнено за сегодня увеличивается.')
    @allure.description(
        'Логинимся на сайте, сохраняем начальное кол-во заказов в день, создаем новый заказ и проверяем, что текущее значение счетчика заказов в день больше, чем сохраненое значение.')
    def test_new_order_up_order_count_today_success(self, get_client_data):
        main_page = MainPage(self.driver)
        login_page = LoginPage(self.driver)
        order_feed_page = OrderFeedPage(self.driver)
        login_page.open_login_page()
        login_page.click_on_email_field()
        login_page.set_email_field(get_client_data.email)
        login_page.click_on_password_field()
        login_page.set_password_field(get_client_data.password)
        login_page.click_on_entry_button()
        login_page.wait_url_changes(Urls.login_page)
        main_page.click_on_order_feed_button()
        main_page.wait_url_changes(Urls.main_page)
        initial_order_count_done_today = order_feed_page.get_order_count_done_today()
        order_feed_page.click_on_construct_button()
        order_feed_page.wait_url_changes(Urls.order_feed_page)
        main_page.move_ingredient_to_basket()
        main_page.click_on_order_button()
        main_page.wait_visibility_image_order_create()
        login_page.open_login_page()
        main_page.click_on_order_feed_button()
        main_page.wait_url_changes(Urls.main_page)
        assert order_feed_page.get_order_count_done_today() > initial_order_count_done_today

    @allure.title(
        'Тест на то, что заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов».')
    @allure.description(
        'Логинимся на сайте, оформляем заказ, потом проверяем, что заказ из истории заказов в профиле есть в ленте заказов.')
    def test_find_order_number_from_history_on_feed_success(self, get_client_data):
        main_page = MainPage(self.driver)
        login_page = LoginPage(self.driver)
        profile_page = ProfilePage(self.driver)
        order_history_page = OrderHistoryPage(self.driver)
        order_feed_page = OrderFeedPage(self.driver)
        login_page.open_login_page()
        login_page.click_on_email_field()
        login_page.set_email_field(get_client_data.email)
        login_page.click_on_password_field()
        login_page.set_password_field(get_client_data.password)
        login_page.click_on_entry_button()
        login_page.wait_url_changes(Urls.login_page)
        main_page.click_on_construct_button()
        main_page.move_ingredient_to_basket()
        main_page.click_on_order_button()
        main_page.wait_visibility_image_order_create()
        login_page.open_login_page()
        main_page.click_on_profile_button()
        main_page.wait_url_changes(Urls.main_page)
        profile_page.click_on_order_history_button()
        profile_page.wait_url_changes(Urls.profile_page)
        order_number_in_history = order_history_page.get_order_number()
        order_history_page.click_on_order_feed_button()
        order_history_page.wait_url_changes(Urls.order_history_page)
        assert order_number_in_history in order_feed_page.get_order_numbers()





