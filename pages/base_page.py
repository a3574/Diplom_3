from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import re


class BasePage:
    driver = None
    value = ''
    url = ''
    xpath = ''
    tab = 0

    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def click_on_element_by_xpath(self, *element):
        element = self.driver.find_element(*element)
        element.click()

    def set_in_element_by_xpath(self, *element, value):
        element = self.driver.find_element(*element)
        element.send_keys(value)

    def scroll_to_element_by_xpath(self, *element):
        element = self.driver.find_element(*element)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def get_text_element_by_xpath(self, *element):
        element = self.driver.find_element(*element)
        element_text = re.findall(r'\b\d+\b', element.text)
        return element_text

    def wait_element_to_be_clickable_by_xpath(self, *element):
        element = self.driver.find_element(*element)
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(element))

    def wait_visibility_of_element(self, element):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of(element))

    def find_on_element_by_xpath(self, xpath):
        element = self.driver.find_element(By.XPATH, xpath)
        return element

    def wait_url_changes(self, url):
        WebDriverWait(self.driver, 3).until(expected_conditions.url_changes(url))

    def wait_title_contains(self, value):
        WebDriverWait(self.driver, 3).until(expected_conditions.title_contains(value))

    def switch_to_tab(self, tab):
        self.driver.switch_to.window(self.driver.window_handles[tab])
