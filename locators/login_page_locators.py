from selenium.webdriver.common.by import By


class LoginPageLocators:
    ENTRY_LABEL = (By.XPATH, ".//*[text()='Вход']")
    EMAIL_FIELD = (By.XPATH, ".//label[text()='Email']/following-sibling::input")
    PASSWORD_FIELD = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input")
    ENTRY_BUTTON = (By.XPATH, ".//button[text()='Войти']")
    FORGOT_PASSWORD_LABEL = (By.XPATH, ".//*[text()='Восстановить пароль']")
