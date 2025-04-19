import allure
from locators.main_page_locators import MainPageLocators
from locators.base_page_locators import BasePageLocators
from pages.base_page import BasePage
from urls import Urls


class MainPage(BasePage):
    driver = None
    question = ''
    order_button_top = [*BasePageLocators.ORDER_BUTTON_TOP]
    order_button_middle = [*MainPageLocators.ORDER_BUTTON_MIDDLE]
    status_order_button = [*BasePageLocators.STATUS_ORDER_BUTTON]
    status_order_field = [*BasePageLocators.STATUS_ORDER_FIELD]
    check_status_order_button = [*BasePageLocators.CHECK_STATUS_ORDER_BUTTON]

    @allure.step('Открываем главную страницу')
    def open_main_page(self):
        main_page = MainPage(self.driver)
        main_page.open_page(Urls.main_page)

    @allure.step('Клик по кнопке Заказать в середине главной страницы')
    def click_order_button_middle(self):
        main_page = MainPage(self.driver)
        main_page.scroll_to_element_by_xpath(*self.order_button_middle)
        main_page.click_on_element_by_xpath(*self.order_button_middle)

    @allure.step('Клик по кнопке Заказать в заголовке страницы')
    def click_order_button_top(self):
        main_page = MainPage(self.driver)
        main_page.wait_element_to_be_clickable_by_xpath(*self.order_button_top)
        main_page.click_on_element_by_xpath(*self.order_button_top)

    @allure.step('Открываем вопрос и получаем текст ответа на него')
    def get_answer_by_question(self, question):
        main_page = MainPage(self.driver)
        question_element = main_page.find_on_element_by_xpath(".//*[text()=\"" + question + "\"]")
        self.driver.execute_script("arguments[0].scrollIntoView();", question_element)
        main_page.wait_visibility_of_element(question_element)
        question_element.click()
        answer_element = main_page.find_on_element_by_xpath(
            ".//*[text()=\"" + question + "\"]/parent::div/following::div/p")
        main_page.wait_visibility_of_element(answer_element)
        return answer_element.text

    @allure.step('Клик по кнопке Статус заказа')
    def select_status_order_button(self):
        main_page = MainPage(self.driver)
        main_page.wait_element_to_be_clickable_by_xpath(*self.status_order_button)
        main_page.click_on_element_by_xpath(*self.status_order_button)

    @allure.step('Заполнение поля Введите номер заказа')
    def set_status_order_field(self, order_number):
        main_page = MainPage(self.driver)
        main_page.wait_element_to_be_clickable_by_xpath(*self.status_order_field)
        main_page.set_in_element_by_xpath(*self.status_order_field, value=order_number)

    @allure.step('Клик по кнопке GO!')
    def select_check_status_order_button(self):
        main_page = MainPage(self.driver)
        main_page.wait_element_to_be_clickable_by_xpath(*self.check_status_order_button)
        main_page.click_on_element_by_xpath(*self.check_status_order_button)
