import allure
from locators.order_feed_page_locators import OrderFeedPageLocators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):
    order_number = [*OrderFeedPageLocators.ORDER_NUMBER_IN_CARD]
    order_count_done_all_time = [*OrderFeedPageLocators.ORDER_COUNT_DONE_ALL_TIME]
    order_count_done_today = [*OrderFeedPageLocators.ORDER_COUNT_DONE_TODAY]
    window_order_detail = [*OrderFeedPageLocators.WINDOW_ORDER_DETAIL]
    first_order_number = [*OrderFeedPageLocators.FIRST_ORDER_NUMBER_IN_CARD]
    order_number_in_work = [*OrderFeedPageLocators.ORDER_NUMBER_IN_WORK]

    @allure.step('Получаем номера заказов из ленты заказов.')
    def get_order_numbers(self):
        self.wait_visibility_of_element(self.order_number)
        elements = self.driver.find_elements(*self.order_number)
        elements_texts = [element.text for element in elements]
        return elements_texts

    @allure.step('Получаем кол-во заказов сделанных за все время')
    def get_order_count_done_all_time(self):
        self.wait_visibility_of_element(self.order_count_done_all_time)
        element = self.driver.find_element(*self.order_count_done_all_time)
        return element.text

    @allure.step('Получаем кол-во заказов сделанных за текущий день')
    def get_order_count_done_today(self):
        self.wait_visibility_of_element(self.order_count_done_today)
        element = self.driver.find_element(*self.order_count_done_today)
        return element.text

    @allure.step('Ожидаем видимости модального окна с деталями заказа')
    def check_visibility_window_order_detail(self):
        self.wait_visibility_of_element(self.window_order_detail)
        element = self.driver.find_element(*self.window_order_detail)
        return element

    @allure.step('Нажимаем на первую карточку заказа')
    def click_on_first_order(self):
        self.click_on_element(self.first_order_number)

    @allure.step('Получаем список заказов в работе')
    def get_order_number_in_work(self):
        self.wait_visibility_of_element(self.order_number_in_work)
        elements = self.driver.find_elements(*self.order_number_in_work)
        elements_texts = [element.text for element in elements]
        return elements_texts





