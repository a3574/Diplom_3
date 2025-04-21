from selenium.webdriver.common.by import By

class OrderFeedPageLocators:
    ORDER_NUMBER_IN_CARD = (By.XPATH, ".//li[contains(@class, 'OrderHistory_listItem__2x95r mb-6')]/a/div/p[1]")
    ORDER_COUNT_DONE_ALL_TIME = (By.XPATH, ".//p[text()='Выполнено за все время:']/following-sibling::p")
    ORDER_COUNT_DONE_TODAY = (By.XPATH, ".//p[text()='Выполнено за сегодня:']/following-sibling::p")
    WINDOW_ORDER_DETAIL = (By.XPATH, ".//div[contains(@class, 'Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10')]")
    FIRST_ORDER_NUMBER_IN_CARD = (By.XPATH, ".//li[contains(@class, 'OrderHistory_listItem__2x95r mb-6')][1]/a/div/p[1]")
    ORDER_NUMBER_IN_WORK = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi')]/li[contains(@class, 'text text_type_digits-default mb-2')]")



