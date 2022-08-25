import time
from page_object_playwright.base_page import BasePage


class BuyingProc(BasePage):

    def __init__(self, page):
        super().__init__(page)

    locator_dictionary = {
        "summary_checkout": ".standard-checkout",
        "address_checkout": "#center_column > form > p > button",
        "cgv_mark": "input#cgv",
        "shipping_checkout": "#form > p > button",
        "pay_by_check": "#HOOK_PAYMENT > div:nth-child(2) > div > p > a",
        "payment_confirm": "#cart_navigation > button"
    }

    def order_process(self):
        """
        doing all the order process after you add item to cart
        :return:
        """
        self._page.locator(self.locator_dictionary["summary_checkout"]).click()
        time.sleep(2)
        self._page.locator(self.locator_dictionary["address_checkout"]).click()
        time.sleep(2)
        self._page.locator(self.locator_dictionary["cgv_mark"]).click()
        time.sleep(2)
        self._page.locator(self.locator_dictionary["shipping_checkout"]).click()
        time.sleep(2)
        self._page.locator(self.locator_dictionary["pay_by_check"]).click()
        time.sleep(2)
        self._page.locator(self.locator_dictionary["payment_confirm"]).click()
        time.sleep(2)
        return self._page
