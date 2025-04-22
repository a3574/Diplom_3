import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from urls import Urls


class MainPage(BasePage):
    first_ingredient_icon = [*MainPageLocators.FIRST_INGREDIENT_ICON]
    first_ingredient_window = [*MainPageLocators.FIRST_INGREDIENT_WINDOW]
    close_button_on_ingredient_window = [*MainPageLocators.CLOSE_BUTTON_ON_INGREDIENT_WINDOW]
    counter_on_first_ingredient = [*MainPageLocators.FIRST_INGREDIENT_COUNTER]
    basket_widget = [*MainPageLocators.BASKET]
    button_order = [*MainPageLocators.BUTTON_ORDER]
    order_window = [*MainPageLocators.MODAL_ORDER]
    close_button_on_order_window = [*MainPageLocators.CLOSE_BUTTON_ON_ORDER_WINDOW]
    modal_order_creation = [*MainPageLocators.MODAL_ORDER_CREATION]
    image_order_create = [*MainPageLocators.IMAGE_ORDER_CREATE]

    @allure.step('Открываем главную страницу')
    def open_main_page(self):
        self.open_page(Urls.main_page)

    @allure.step('Нажимаем на первый ингредиент')
    def click_on_first_ingredient(self):
        self.click_on_element(self.first_ingredient_icon)

    @allure.step('Нажимаем на кнопку закрытия окна деталей ингредиента')
    def click_on_close_button_on_ingredient_window(self):
        self.click_on_element(self.close_button_on_ingredient_window)

    @allure.step('Проверяем, что появилось окно с деталями ингедиента')
    def check_first_ingredient_window(self):
        self.wait_visibility_of_element(self.first_ingredient_window)
        element = self.driver.find_element(*self.first_ingredient_window)
        return element

    @allure.step('Проверяем, что появилось окно с деталями ингедиента')
    def check_close_ingredient_window(self):
        return self.wait_invisibility_of_element(self.first_ingredient_window)

    @allure.step('Получаем число из счетчика ингредиентов')
    def get_count_from_counter_on_first_ingredient(self):
        self.wait_visibility_of_element(self.counter_on_first_ingredient)
        element = self.driver.find_element(*self.counter_on_first_ingredient)
        return element.text

    @allure.step('Перемещаем ингредиент в корзину')
    def move_ingredient_to_basket(self):
        self.move_element(self.first_ingredient_icon, self.basket_widget)
        element = self.driver.find_element(*self.counter_on_first_ingredient)
        return element.text

    @allure.step('Нажимаем кнопку оформление заказа')
    def click_on_order_button(self):
        self.click_on_element(self.button_order)

    @allure.step('Получаем номер заказа')
    def get_order_number(self):
        self.wait_visibility_of_element(self.order_window)
        element = self.driver.find_element(*self.order_window)
        return element.text

    def wait_visibility_image_order_create(self):
        self.wait_visibility_of_element(self.image_order_create)





