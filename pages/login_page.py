import allure
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
from urls import Urls


class LoginPage(BasePage):
    entry_label = [*LoginPageLocators.ENTRY_LABEL]
    entry_button = [*LoginPageLocators.ENTRY_BUTTON]
    email_field = [*LoginPageLocators.EMAIL_FIELD]
    email_active_field = [*LoginPageLocators.EMAIL_ACTIVE_FIELD]
    forgot_password_label = [*LoginPageLocators.FORGOT_PASSWORD_LABEL]
    password_field = [*LoginPageLocators.PASSWORD_FIELD]
    visible_button = [*LoginPageLocators.VISIBLE_BUTTON]

    @allure.step('Открываем страницу логина')
    def open_login_page(self):
        self.open_page(Urls.login_page)

    @allure.step('Нажатие на кнопку восстановления пароля')
    def click_on_forgot_password_label(self):
        self.click_on_element(self.forgot_password_label)

    @allure.step('Нажатие на кнопку показать/скрыть пароль')
    def click_on_visible_button(self):
        self.click_on_element(self.visible_button)

    @allure.step('Проверяем, что поле Email стало активным')
    def check_email_field_status(self):
        self.wait_visibility_of_element(self.email_field)
        element = self.driver.find_element(*self.email_field)
        return element

    @allure.step('Нажатие на поле Email')
    def click_on_email_field(self):
        self.click_on_element(self.email_field)

    @allure.step('Нажатие на поле Email')
    def set_email_field(self, email):
        self.set_in_element(self.email_field, email)

    @allure.step('Нажатие на поле Password')
    def click_on_password_field(self):
        self.click_on_element(self.password_field)

    @allure.step('Нажатие на поле Password')
    def set_password_field(self, password):
        self.set_in_element(self.password_field, password)

    @allure.step('Нажатие на поле Password')
    def click_on_entry_button(self):
        self.click_on_element(self.entry_button)




