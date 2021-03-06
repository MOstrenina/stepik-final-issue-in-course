from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_EMAIL = (By.ID, "id_registration-email")
    REGISTER_FIRST_PASSWORD = (By.ID, "id_registration-password1")
    REGISTER_CONFIRM_PASSWORD = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
    NAME_OF_PRODUCT = (By.CSS_SELECTOR, ".product_main > h1")
    MESSAGE_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "div.alertinner ")
    BASKET_SUMMARY = (By.CSS_SELECTOR, "#messages > .alert:nth-child(3)")
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, "#messages > :nth-child(1) strong")
    PRODUCT_PRICE_IN_BASKET = (By.CSS_SELECTOR, "#messages > :nth-child(3) strong")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    GO_TO_THE_BASKET = (By.CSS_SELECTOR, ".btn-group > a.btn.btn-default:nth-child(1)")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
    TABLE_WITH_PRODUCTS = (By.ID, "basket_formset")
