import pytest
import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from urls import Urls


class TestPersonalAccount:

    @allure.title('Тест на переход в личный кабиннет по клику на кнопку «Личный кабинет» в верхнем баре')
    @allure.description('Открываем главную страницу. Нажимаем на кнопку «Личный кабинет». Ожидаем что открытая страница будет страница логина.')
    def test_ckick_on_profile_button_change_url_to_profile_success(self, get_client_data):
        main_page = MainPage(self.driver)
        main_page.open_main_page()
        main_page.click_on_profile_button()
        main_page.wait_url_changes(Urls.main_page)
        login_page = LoginPage(self.driver)
        login_page.click_on_email_field()
        login_page.set_email_field(get_client_data.email)
        login_page.click_on_password_field()
        login_page.set_password_field(get_client_data.password)
        login_page.click_on_entry_button()
        login_page.wait_url_changes(Urls.login_page)
        main_page.click_on_profile_button()
        main_page.wait_url_changes(Urls.main_page)
        main_page.wait_url_changes(Urls.account_page)
        assert main_page.get_current_url() == Urls.profile_page
    @allure.title('Тест на переход в раздел «История заказов»')
    @allure.description('Успешно заходим в личный кабинет. В личном кабинете нажимаем кнопку «Лента заказов». Проверяем что страница поменялась на ленту заказов.')
    def test_ckick_on_history_order_change_url_to_feed_success(self, get_client_data):
        main_page = MainPage(self.driver)
        main_page.open_main_page()
        main_page.click_on_profile_button()
        main_page.wait_url_changes(Urls.main_page)
        login_page = LoginPage(self.driver)
        login_page.click_on_email_field()
        login_page.set_email_field(get_client_data.email)
        login_page.click_on_password_field()
        login_page.set_password_field(get_client_data.password)
        login_page.click_on_entry_button()
        login_page.wait_url_changes(Urls.login_page)
        main_page.click_on_profile_button()
        main_page.wait_url_changes(Urls.main_page)
        main_page.wait_url_changes(Urls.account_page)
        profile_page = ProfilePage(self.driver)
        profile_page.click_on_order_history_button()
        profile_page.wait_url_changes(Urls.profile_page)
        assert profile_page.get_current_url() == Urls.order_history_page

    @allure.title('Тест на выход из аккаунта')
    @allure.description('Успешно заходим в личный кабинет. В личном кабинете нажимаем кнопку «Выход». Проверяем что страница поменялась на страницу логина.')
    def test_ckick_on_exit_change_url_to_feed_success(self, get_client_data):
        main_page = MainPage(self.driver)
        main_page.open_main_page()
        main_page.click_on_profile_button()
        main_page.wait_url_changes(Urls.main_page)
        login_page = LoginPage(self.driver)
        login_page.click_on_email_field()
        login_page.set_email_field(get_client_data.email)
        login_page.click_on_password_field()
        login_page.set_password_field(get_client_data.password)
        login_page.click_on_entry_button()
        login_page.wait_url_changes(Urls.login_page)
        main_page.click_on_profile_button()
        main_page.wait_url_changes(Urls.main_page)
        main_page.wait_url_changes(Urls.account_page)
        profile_page = ProfilePage(self.driver)
        profile_page.click_on_exit_button()
        profile_page.wait_url_changes(Urls.profile_page)
        assert profile_page.get_current_url() == Urls.login_page





