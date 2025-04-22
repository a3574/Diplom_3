import allure
from locators.order_history_page_locators import OrderHistoryPageLocators
from pages.base_page import BasePage


class OrderHistoryPage(BasePage):
    order_number = [*OrderHistoryPageLocators.ORDER_NUMBER_IN_HISTORY]

    @allure.step('Получаем номер заказа из вкладки История заказов в личном кабинете')
    def get_order_number(self):
        self.wait_visibility_of_element(self.order_number)
        element = self.driver.find_element(*self.order_number)
        return element.text





