import time
from selenium.webdriver.common.by import By
from page_object_selenium.base_page import BasePage


class BuyingProc(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    locator_dictionary = {
        "summary_checkout": (By.CLASS_NAME, "standard-checkout"),
        "address_checkout": (By.CSS_SELECTOR, "#center_column > form > p > button"),
        "cgv_mark": (By.ID, "cgv"),
        "shipping_checkout": (By.CSS_SELECTOR, "#form > p > button"),
        "pay_by_check": (By.CSS_SELECTOR, "#HOOK_PAYMENT > div:nth-child(2) > div > p > a"),
        "payment_confirm": (By.CSS_SELECTOR, "#cart_navigation > button")
    }

    def order_process(self):
        """
        doing all the order process after you add item to cart
        :return:
        """
        self._driver.find_element(*self.locator_dictionary["summary_checkout"]).click()
        time.sleep(2)
        self._driver.find_element(*self.locator_dictionary["address_checkout"]).click()
        time.sleep(2)
        self._driver.find_element(*self.locator_dictionary["cgv_mark"]).click()
        time.sleep(2)
        self._driver.find_element(*self.locator_dictionary["shipping_checkout"]).click()
        time.sleep(2)
        self._driver.find_element(*self.locator_dictionary["pay_by_check"]).click()
        time.sleep(2)
        self._driver.find_element(*self.locator_dictionary["payment_confirm"]).click()
        time.sleep(2)
        return self._driver
