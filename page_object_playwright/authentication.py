from page_object_playwright.account_page import *
from playwright.async_api import Page
from page_object_playwright.base_page import BasePage


class AuthenticationPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

    locator_dictionary = {
        "email": "#email",
        "password": "#passwd",
        "login": ".icon-lock",
        "alert": "#center_column > div.alert.alert-danger > ol > li",
    }

    def do_login(self, email, password) -> AccountPage:
        """
        :param email: get email
        :param password: get password
        :return: AccountPage
        """
        self._page.locator(self.locator_dictionary["email"]).fill(email)
        self._page.locator(self.locator_dictionary["password"]).fill(password)
        self._page.locator(self.locator_dictionary["login"]).click()

        return AccountPage(self._page)

    def error_message(self):
        """
        find the alert texts
        :return: text with alerts
        """
        text = self._page.locator(self.locator_dictionary["alert"]).inner_text()
        return text

