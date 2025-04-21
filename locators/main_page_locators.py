from selenium.webdriver.common.by import By

class MainPageLocators:
    FIRST_INGREDIENT_ICON = (By.XPATH, ".//*[contains(@class, 'BurgerIngredients_ingredients__list__2A-mT')][1]/*[contains(@class, 'BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8')][1]")
    FIRST_INGREDIENT_COUNTER = (By.XPATH, ".//*[contains(@class, 'BurgerIngredients_ingredients__list__2A-mT')][1]/a[1]/div[1]/p[1]")
    FIRST_INGREDIENT_WINDOW = (By.XPATH, ".//*[text()='Детали ингредиента']")
    CLOSE_BUTTON_ON_INGREDIENT_WINDOW = (By.XPATH, ".//section[contains(@class, 'Modal_modal_opened__3ISw4 Modal_modal__P3_V5')]/div/button[contains(@class, 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK')]")
    BASKET = (By.CLASS_NAME, 'BurgerConstructor_basket__list__l9dp_')
    BUTTON_ORDER = (By.XPATH, ".//button[text()='Оформить заказ']")
    MODAL_ORDER = (By.XPATH, ".//*[contains(@class, 'Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8')]")
    CLOSE_BUTTON_ON_ORDER_WINDOW = (By.XPATH, ".//button[contains(@class, 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK')]")
    MODAL_ORDER_CREATION = (By.XPATH, ".//*[contains(@class, 'Modal_modal__P3_V5')]")
    IMAGE_ORDER_CREATE = (By.XPATH, ".//*[contains(@class,'Modal_modal__image__2nh17')]")





