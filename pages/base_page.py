from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import BasePageLocators
import allure

class BasePage:
    driver = None
    value = ''
    url = ''
    profile_button = [*BasePageLocators.PROFILE_BUTTON]
    order_feed_button = [*BasePageLocators.ORDER_FEED_BUTTON]
    construct_button = [*BasePageLocators.CONSTRUCTOR_BUTTON]

    def __init__(self, driver):

        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def click_on_element(self, locator):
        action = ActionChains(self.driver)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        element = self.driver.find_element(*locator)
        action.click(on_element=element).perform()

    def wait_url_changes(self, url):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_changes(url))

    def set_in_element(self, locator, value):
        element = self.driver.find_element(*locator)
        element.send_keys(value)

    def wait_visibility_of_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
    def wait_invisibility_of_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.invisibility_of_element_located(locator))

    def move_element(self, locator_source, locator_target):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator_source))
        source = self.driver.find_element(*locator_source)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator_target))
        target = self.driver.find_element(*locator_target)
        action = ActionChains(self.driver)
        action.drag_and_drop(source, target).pause(5).perform()

    def scroll_to_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_url_changes(self, url):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_changes(url))

    @allure.step('Нажатие на кнопку восстановления пароля')
    def click_on_profile_button(self):
        base_page = BasePage(self.driver)
        base_page.click_on_element(self.profile_button)

    @allure.step('Нажатие на кнопку ленты заказов')
    def click_on_order_feed_button(self):
        base_page = BasePage(self.driver)
        base_page.click_on_element(self.order_feed_button)

    @allure.step('Нажатие на кнопку Конструктор')
    def click_on_construct_button(self):
        base_page = BasePage(self.driver)
        base_page.click_on_element(self.construct_button)

