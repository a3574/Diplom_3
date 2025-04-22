from selenium.webdriver.common.by import By

class ProfilePageLocators:
    LOGIN_FIELD = (By.XPATH, ".//label[text()='Имя']/following-sibling::input")
    EMAIL_FIELD = (By.XPATH, ".//label[text()='Email']/following-sibling::input")
    PASSWORD_FIELD = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input")
    CONSTRUCTOR_LABEL = (By.XPATH, ".//*[text()='Конструктор']")
    EXIT_BUTTON = (By.XPATH, ".//button[text()='Выход']")
    ORDER_HISTORY_BUTTON = (By.XPATH, ".//*[text()='История заказов']")




