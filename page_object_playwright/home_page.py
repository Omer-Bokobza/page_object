from page_object_playwright.authentication import AuthenticationPage
from page_object_playwright.base_page import BasePage
from page_object_playwright.main_page import MainPage


class HomePage(BasePage):
    locator_dictionary = {
        "sign_in": ".login",
        "search_box": '#search_query_top',
        "search_btn": "#searchbox > button"
    }

    def __init__(self, page):
        super().__init__(page)

    def sign_in_btn(self) -> AuthenticationPage:
        """
        click on sign in button
        :return:
        """
        self._page.locator(self.locator_dictionary["sign_in"]).click()
        return AuthenticationPage(self._page)

    def search_box(self, search_text) -> MainPage:
        """
        send text to search box and click on search button
        :param search_text:
        :return:MainPage
        """
        self._page.locator(self.locator_dictionary["search_box"]).fill(search_text)
        self._page.locator(self.locator_dictionary["search_btn"]).click()
        return MainPage(self._page)
