from selenium.webdriver.common.by import By


class RegisterPageLocators:
    LOGIN_FIELD = (By.XPATH, ".//label[text()='Имя']/following-sibling::input")
    EMAIL_FIELD = (By.XPATH, ".//label[text()='Email']/following-sibling::input")
    PASSWORD_FIELD = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input")
    REGISTER_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")
    WRONG_PASSWORD_LABEL = (By.XPATH, ".//*[text()='Некорректный пароль']")
    ENTRY_LABEL = (By.XPATH, ".//*[text()='Войти']")




