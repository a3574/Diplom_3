import allure
from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from pages.base_page import BasePage
from urls import Urls


class ForgotPasswordPage(BasePage):
    driver = None
    restore_button = [*ForgotPasswordPageLocators.RESTORE_BUTTON]
    email_field = [*ForgotPasswordPageLocators.EMAIL_FIELD]

    @allure.step('Открываем страницу восстановления пароля')
    def open_forgot_password_page(self):
        forgot_password_page = ForgotPasswordPage(self.driver)
        forgot_password_page.open_page(Urls.forgot_password_page)

    @allure.step('Нажатие на кнопку Восстановить')
    def click_on_restore_button(self):
        forgot_password_page = ForgotPasswordPage(self.driver)
        forgot_password_page.click_on_element(self.restore_button)

    @allure.step('Заполнение поля Email')
    def set_email_field(self, email):
        forgot_password_page = ForgotPasswordPage(self.driver)
        forgot_password_page.set_in_element(self.email_field, value=email)




