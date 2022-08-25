from page_object_selenium.authentication import *
from page_object_selenium.main_page import *


class HomePage(BasePage):
    locator_dictionary = {
        "sign_in": (By.CLASS_NAME, "login"),
        "search_box": (By.ID, "search_query_top"),
        "search_btn": (By.CSS_SELECTOR, "#searchbox > button")
    }

    def __init__(self, driver):
        super().__init__(driver)

    def sign_in_btn(self):
        """
        click on sign in button
        :return:
        """
        self._driver.find_element(*self.locator_dictionary["sign_in"]).click()
        return AuthenticationPage(self._driver)

    def search_box(self, search_text):
        """
        send text to search box and click on search button
        :param search_text:
        :return:MainPage
        """
        self._driver.find_element(*self.locator_dictionary["search_box"]).send_keys(search_text)
        self._driver.find_element(*self.locator_dictionary["search_btn"]).click()
        return MainPage(self._driver)
