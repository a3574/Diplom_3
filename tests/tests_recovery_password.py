import pytest
import allure
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from urls import Urls


class TestRecoveryPassword:
    @allure.title('Тест на то что клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его.')
    @allure.description(
        'Открываем страницу логина. Нажимаем на кнопку показать/скрыть пароль. Проверяем, что поле пароль стало активным.')
    def test_ckick_by_button_visible_password_set_password_field_active(self):
        login_page = LoginPage(self.driver)
        login_page.open_login_page()
        login_page.click_on_visible_button()
        assert login_page.check_email_field_status()

    @allure.title('Тест на переход на страницу восстановления пароля по кнопке Восстановить пароль')
    @allure.description(
        'Открыываем страницу логина. Заполняем поле Email. Кликаем по кнопке Восстановить пароль. Проверяем изменился ли URL на страницу https://stellarburgers.nomoreparties.site/forgot-password')
    def test_ckick_by_button_recovery_change_url_to_reset_success(self, get_client_data):
        forgot_password_page = ForgotPasswordPage(self.driver)
        forgot_password_page.open_forgot_password_page()
        forgot_password_page.set_email_field(get_client_data.email)
        forgot_password_page.click_on_restore_button()
        forgot_password_page.wait_url_changes(Urls.forgot_password_page)
        assert forgot_password_page.get_current_url() == Urls.reset_password_page

    @allure.title('Тест на переход на страницу восстановления пароля по кнопке Восстановить пароль')
    @allure.description(
        'Открываем страницу логина. Кликаем по кнопке Восстановить пароль. Проверяем изменился ли URL на страницу https://stellarburgers.nomoreparties.site/forgot-password')
    def test_open_recovery_page_by_button_success(self):
        login_page = LoginPage(self.driver)
        login_page.open_login_page()
        login_page.click_on_forgot_password_label()
        login_page.wait_url_changes(Urls.login_page)
        assert login_page.get_current_url() == Urls.forgot_password_page





