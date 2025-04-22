from selenium.webdriver.common.by import By


class BasePageLocators:
    ENTRY_LABEL = (By.XPATH, ".//*[text()='Вход']")
    PROFILE_BUTTON = (By.XPATH, ".//*[text()='Личный Кабинет']")
    ORDER_FEED_BUTTON = (By.XPATH, ".//*[text()='Лента Заказов']")
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//*[text()='Конструктор']")


