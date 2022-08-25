from page_object_selenium.base_page import BasePage
from selenium.webdriver.common.by import By
from page_object_selenium import home_page


class AccountPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    locator_dictionary = {
        "home_btn": (By.CLASS_NAME, "icon-home"),
        "account_info": (By.CLASS_NAME, "info-account")}

    def home_btn(self) -> home_page:
        """
        click on home button
        :return: HomePage
        """
        self._driver.find_element(*self.locator_dictionary["home_btn"]).click()
        return home_page.HomePage(self._driver)

    def valid_authentication(self):
        return self._driver.find_element(*self.locator_dictionary["account_info"]).text
