from page_object_selenium.account_page import *


class AuthenticationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    locator_dictionary = {
        "email": (By.CSS_SELECTOR, "#email"),
        "password": (By.CSS_SELECTOR, "#passwd"),
        "login": (By.CLASS_NAME, "icon-lock"),
        "alert": (By.CLASS_NAME, "alert"),

    }

    def do_login(self, email, password) -> AccountPage:
        """
         :param email: get email
         :param password: get password
         :return: AccountPage
         """
        self._driver.find_element(*self.locator_dictionary["email"]).send_keys(email)
        self._driver.find_element(*self.locator_dictionary["password"]).send_keys(password)
        self._driver.find_element(*self.locator_dictionary["login"]).click()

        return AccountPage(self._driver)

    def error_message(self):
        """
        find the alert texts
        :return: text with alerts
        """
        text = self._driver.find_element(*self.locator_dictionary["alert"]).text
        return text

