from pages.product_page import ProductPage
import pytest
import time
from time import sleep


@pytest.mark.parametrize('link', ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
def test_guest_can_add_product_to_basket(browser, link):
    final_link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}/'
    page = ProductPage(browser, final_link)
    page.open()
    page.should_be_add_to_basket_button()
    page.should_be_name_of_product()
    page.should_be_product_price()
    page.should_be_add_product_to_basket()
    page.solve_quiz_and_get_code()
    #time.sleep(5)
    page.product_should_be_added_to_basket()
    page.product_should_have_the_same_name()
    page.basket_summary_should_not_have_null()


