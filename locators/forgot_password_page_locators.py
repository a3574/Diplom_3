from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:
    RESTORE_BUTTON = (By.XPATH, ".//button[text()='Восстановить']")
    EMAIL_FIELD = (By.XPATH, ".//input")


