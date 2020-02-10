from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_basket_button(self):
        # проверить наличие кнопки "Добавить в корзину"
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "Button Add to basket is not found!"

    def should_be_product_price(self):
        # проверить наличие цены
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is not found!"

    def should_be_name_of_product(self):
        # проверить наличие названия товара
        assert self.is_element_present(*ProductPageLocators.NAME_OF_PRODUCT), "Product name is not found!"

    def should_be_add_product_to_basket(self):
        # нажать на кнопку "добавить в корзину"
        press = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        press.click()

    def product_should_be_added_to_basket(self):
        # проверить, что отображается блок с нотификациями о добавлении продукта в корзину
        assert self.is_element_present(*ProductPageLocators.PRODUCT_IN_BASKET), "Product is not added!"

    def product_should_have_the_same_name(self):
        # проверить, что имя продукта равно имени продукта в корзине
        name_before_basket = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT).text
        name_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET).text
        assert name_before_basket == name_in_basket, "Names of product in the basket are not equal!"

    def basket_summary_should_not_have_null(self):
        # проверить, что цена продукта соответствует сумме товаров в корзине
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_summary = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET).text
        assert product_price == basket_summary, "Prices of product in the basket are not equal!"

