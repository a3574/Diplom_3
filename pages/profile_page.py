import allure
from locators.profile_page_locators import ProfilePageLocators
from pages.base_page import BasePage
from urls import Urls


class ProfilePage(BasePage):
    driver = None
    exit_button = [*ProfilePageLocators.EXIT_BUTTON]
    order_history_button = [*ProfilePageLocators.ORDER_HISTORY_BUTTON]

    @allure.step('Нажатие на кнопку выход')
    def click_on_exit_button(self):
        self.click_on_element(self.exit_button)

    @allure.step('Нажатие на кнопку выход')
    def click_on_order_history_button(self):
        self.click_on_element(self.order_history_button)




