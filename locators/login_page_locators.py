from selenium.webdriver.common.by import By


class LoginPageLocators:
    ENTRY_LABEL = (By.XPATH, ".//*[text()='Вход']")
    EMAIL_FIELD = (By.XPATH, ".//label[text()='Email']/following-sibling::input")
    PASSWORD_FIELD = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input")
    FORGOT_PASSWORD_LABEL = (By.XPATH, ".//a[text()='Восстановить пароль']")
    VISIBLE_BUTTON = (By.XPATH, ".//*[contains(@class, 'input__icon input__icon-action')]")
    ENTRY_BUTTON = (By.XPATH, ".//*[text()='Войти']")
    EMAIL_ACTIVE_FIELD = (By.XPATH, ".//*[contains(@class, 'input pr-6 pl-6 input_type_password input_size_default input_status_active')]")




