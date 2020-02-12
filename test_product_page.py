from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
import pytest
from mimesis import Person  # с помощью этой библиотеки будем генерировать email и password


@pytest.mark.parametrize('link', ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, link):
    final_link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}'
    page = ProductPage(browser, final_link)
    page.open()
    page.should_be_add_to_basket_button()
    page.should_be_name_of_product()
    page.should_be_product_price()
    page.should_be_add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.product_should_be_added_to_basket()
    page.item_price_should_be_the_same()
    page.product_should_have_the_same_name()


@pytest.mark.xfail(reason="message is required in this case")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_button()
    page.should_be_add_product_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="fixing this bug right now")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_button()
    page.should_be_add_product_to_basket()
    page.message_should_be_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_a_basket_url()
    basket_page.should_not_be_a_table_with_items()
    basket_page.should_be_message_empty_basket()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    # регистрация пользователя
    def setup(self, browser):
        login = Person()
        # генерируем логин и пароль с помощью методов класса Person библиотеки mimesis
        email = login.email(domains=['@gmail.com'])
        password = login.password(length=9, hashed=False)
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url, email=email, password=password)
        login_page.register_new_user()
        login_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_add_to_basket_button()
        page.should_be_name_of_product()
        page.should_be_product_price()
        page.should_be_add_product_to_basket()
        page.product_should_be_added_to_basket()
        page.product_should_have_the_same_name()
        page.item_price_should_be_the_same()

    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()
        page.should_be_add_to_basket_button()
        page.should_be_add_product_to_basket()
        page.should_not_be_success_message()

