from selenium.webdriver import ActionChains
from page_object_seleniumD.buying_process import *
from page_object_selenium.base_page import *


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    locator_dictionary = {
        "right_blocks": (By.CLASS_NAME, "right-block"),
        "price_product": (By.CLASS_NAME, "content_price"),
        "price": (By.CLASS_NAME, "price"),
        "add_to_cart_btn": (By.CSS_SELECTOR, 'a.ajax_add_to_cart_button'),
        "proceed_to_checkout": (By.CSS_SELECTOR,
                                "#layer_cart > div.clearfix > div.layer_cart_cart > div.button-container > a")
    }

    def find_cheapest_dress(self):
        """
        find the cheapest dress
        :return: add_to_cart = cheapest dress
        """
        right_blocks = self._driver.find_elements(*self.locator_dictionary["right_blocks"])
        prices = []
        index_of_min_price = 0
        for obj in right_blocks:
            price_product = obj.find_element(*self.locator_dictionary["price_product"])
            price = price_product.find_element(*self.locator_dictionary["price"]).text
            prices.append(float(price[1:]))
            lowest_price = min(prices)
            index_of_min_price = prices.index(lowest_price)

        add_to_cart = right_blocks[index_of_min_price]
        return add_to_cart

    def mouse_action(self, add_to_cart):
        """
        mouse action
        :param add_to_cart:cheapest dress from find cheapest dress
        :return:BuyingProc
        """
        actions = ActionChains(self._driver)
        actions.move_to_element(add_to_cart).perform()
        add_to_cart.find_element(*self.locator_dictionary["add_to_cart_btn"]).click()
        time.sleep(8)
        self._driver.find_element(*self.locator_dictionary["proceed_to_checkout"]).click()
        return BuyingProc(self._driver)
