
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    # клик по элементу
    def add_to_backet(self):
        bascet_add = self.browser.find_element(*ProductPageLocators.BACKET_ADD)
        bascet_add.click()

    # проверки на все на странице
    def should_be_product_page(self):
        self.should_be_name_product_in_message()
        self.should_be_price_product_in_message()
        
    # слово "  " содержится в элемнете на странице
    def should_be_name_product_in_message(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == self.browser.find_element(*ProductPageLocators.MESSAGE_NAME).text, "В корзину добавлен не выбранный товар" 
   
    # слово "  " содержится в элемнете на странице
    def should_be_price_product_in_message(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text == self.browser.find_element(*ProductPageLocators.MESSAGE_PRICE).text, "Цена товара в корзине отличаестя от цены на странице товара" 

    # такого элемента быть не должно
    def should_not_be_element(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Элемент '...' есть на странице, хотя не должно быть"

    # элемент исчезает
    def element_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Элемент '...' не исчез, хотя должен был исчезнуть"
