from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_a_basket_url(self):
        # проверка, что робот перешел на страницу корзины
        current_url = self.browser.current_url
        assert current_url.count('basket') == 1, "Basket URL is not found!"

    def should_be_message_empty_basket(self):
        # проверка наличия сообщения об отсутствии товаров в корзине
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            "Message about empty basket is not presented!"

    def should_be_a_table_with_items(self):
        # проверка наличия таблицы с товарами
        assert self.is_element_present(*BasketPageLocators.TABLE_WITH_PRODUCTS), "Items are not found!"

    def should_not_be_a_table_with_items(self):
        # проверка отсутствия таблицы с товарами
        assert self.is_not_element_present(*BasketPageLocators.TABLE_WITH_PRODUCTS), \
            "Items are found, but should not be!"

