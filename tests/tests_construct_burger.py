import pytest
import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage
from urls import Urls


class TestConstructBurger:

    @allure.title('Тест на переход по клику на «Лента заказов».')
    @allure.description('Открываем главную страницу. Нажимаем на кнопку «Лента заказов». Ожидаем что откроется страница ленты заказов.')
    def test_ckick_on_order_button_change_url_to_order_success(self):
        main_page = MainPage(self.driver)
        main_page.open_main_page()
        main_page.click_on_order_feed_button()
        main_page.wait_url_changes(Urls.main_page)
        assert self.driver.current_url == Urls.feed_page

    @allure.title('Тест на то, что залогиненный пользователь может оформить заказ.')
    @allure.description(
        'Открываем главную страницу. Перетасикваем ингредиент в корзину и нажимаем на заказать. Ожидаем, что откроется окно заказа в котором будет номер заказа')
    def test_autorized_user_can_do_order_success(self, get_client_data):
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
        main_page.click_on_construct_button()
        main_page.move_ingredient_to_basket()
        main_page.click_on_order_button()
        assert main_page.get_order_number()

    @allure.title('Тест на то, что при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента.')
    @allure.description('Открываем главную страницу. Перетаскиваем ингредиент в заказ. Проверяем, что на ингредиенте изменилось количество.')
    def test_click_on_ingredient_open_ingredient_card_success(self):
        main_page = MainPage(self.driver)
        main_page.open_main_page()
        start_count = main_page.get_count_from_counter_on_first_ingredient()
        main_page.move_ingredient_to_basket()
        assert start_count != main_page.get_count_from_counter_on_first_ingredient()
    
    @allure.title('Тест на то, что всплывающее окно ингридента закрывается кликом по крестику.')
    @allure.description('Открываем главную страницу. Нажимаем на пиктограмму ингредиента. Ожидаем что откроется окно с ингредиентом')
    def test_click_on_ingredient_open_ingredient_card_success(self):
        main_page = MainPage(self.driver)
        main_page.open_main_page()
        main_page.click_on_first_ingredient()
        main_page.click_on_close_button_on_ingredient_window()
        assert main_page.check_close_ingredient_window() is None
  
    @allure.title('Тест на то, что при клике на ингредиент, появится всплывающее окно с деталями.')
    @allure.description('Открываем главную страницу. Нажимаем на пиктограмму ингредиента. Ожидаем что откроется окно с ингредиентом в названии которого есть Детали ингредиента')
    def test_ckick_on_ingredient_open_ingredient_card_success(self):
        main_page = MainPage(self.driver)
        main_page.open_main_page()
        main_page.click_on_first_ingredient()
        assert main_page.check_first_ingredient_window()

    @allure.title('Тест на переход переход по клику на «Конструктор»')
    @allure.description('Открываем страницу логина. Нажимаем на кнопку «Конструктор». Ожидаем что откроется главная страница.')
    def test_ckick_on_construct_button_change_url_to_construct_success(self):
        login_page = LoginPage(self.driver)
        login_page.open_login_page()
        login_page.click_on_construct_button()
        login_page.wait_url_changes(Urls.login_page)
        assert self.driver.current_url == Urls.main_page




