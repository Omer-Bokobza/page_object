from page_object_playwright.base_page import BasePage
from page_object_playwright import home_page


class AccountPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

    locator_dictionary = {
        "home_btn": ".icon-home",
        "account_info": ".info-account"}

    def home_btn(self) -> home_page:
        """
        click on home button
        :return: HomePage
        """
        self._page.locator(self.locator_dictionary["home_btn"]).click()
        return home_page.HomePage(self._page)

    def valid_authentication(self):
        return self._page.locator(self.locator_dictionary["account_info"]).inner_html()
