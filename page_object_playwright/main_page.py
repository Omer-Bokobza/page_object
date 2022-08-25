import time
from page_object_playwright.base_page import *
from page_object_playwright.buying_process import BuyingProc


class MainPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    locator_dictionary = {
        "right_blocks": ".right-block",
        "price_product": ".content_price",
        "price": ".price",
        "add_to_cart_btn": "text='Add to cart'",
        "proceed_to_checkout": "text='Proceed to checkout'"

    }

    def find_cheapest_dresss(self):
        """
        find the cheapest dress
        :return: add_to_cart = cheapest dress
        """
        index_of_min_price = 0
        right_blocks = self._page.query_selector_all(self.locator_dictionary["right_blocks"])
        prices = []
        for obj in right_blocks:
            price_product = obj.query_selector(self.locator_dictionary["price_product"])
            price = price_product.query_selector(self.locator_dictionary["price"]).inner_text()
            prices.append(float(price[1:]))
            lowest_price = min(prices)
            index_of_min_price = prices.index(lowest_price)

        add_to_cart = right_blocks[index_of_min_price]
        return add_to_cart

    def mouse_actionn(self, add_to_cart) -> BuyingProc:
        """
        mouse action
        :param add_to_cart:cheapest dress from find cheapest dress
        :return:BuyingProc
        """
        print(add_to_cart)
        self._page.wait_for_timeout(3000)
        add_to_cart.hover()
        time.sleep(2)
        add_to_cart.query_selector(self.locator_dictionary["add_to_cart_btn"]).click()
        time.sleep(8)
        self._page.locator(self.locator_dictionary["proceed_to_checkout"]).click()
        return BuyingProc(self._page)
