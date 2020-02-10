from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_PRICE = (By.CLASS_NAME, "price_color")
    NAME_OF_PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main> h1")
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "#messages > .alert:nth-child(1)")
    BASKET_SUMMARY = (By.CSS_SELECTOR, "#messages > .alert:nth-child(3)")
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, "#messages > .alert-success  > .alertinner  > strong")
    PRODUCT_PRICE_IN_BASKET = (By.CSS_SELECTOR, ".alert-info .alertinner p strong")


