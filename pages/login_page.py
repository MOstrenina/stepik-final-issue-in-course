from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, *args, email=None, password=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.email = email
        self.password = password

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверка на корректный url адрес
        current_url = self.browser.current_url
        assert current_url.count('login') == 1, "Login URL is not found!"

    def should_be_login_form(self):
        # проверка наличия формы логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not found!"

    def should_be_register_form(self):
        # проверка наличия формы регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not found!"

    def register_new_user(self):
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL).send_keys(self.email)
        self.browser.find_element(*LoginPageLocators.REGISTER_FIRST_PASSWORD).send_keys(self.password)
        self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD).send_keys(self.password)
        submit_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        submit_button.click()

