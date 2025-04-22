from selenium.webdriver.common.by import By

class OrderHistoryPageLocators:
    ORDER_NUMBER_IN_HISTORY = (By.XPATH, ".//li[contains(@class, 'OrderHistory_listItem__2x95r mb-6')]/a/div/p[1]")



