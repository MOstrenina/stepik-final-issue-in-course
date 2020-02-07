from pages.product_page import ProductPage
import time
from time import sleep


def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_button()
    page.should_be_name_of_product()
    page.should_be_product_price()
    page.should_be_add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.product_should_be_added_to_basket()
    page.product_should_have_the_same_name()
    page.basket_summary_should_not_have_null()


