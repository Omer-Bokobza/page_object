import logging
import time
import pytest
from playwright.sync_api import sync_playwright
from page_object_playwright.home_page import HomePage



# add your specific path to filename to get the log text file
log_format = "%(Levelname)s %(asctime)s - %(message)s"
logging.basicConfig(level=logging.DEBUG, filename="log_file", format=log_format, filemode='w')
log = logging.getLogger()


@pytest.fixture
def user():
    data = {
        "email": "asdasd@wxz.com",
        "password": "123456"
    }
    return data

@pytest.fixture
def open_home_page():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()
        page.goto("http://automationpractice.com/index.php")
        yield HomePage(page)
        time.sleep(2)
        # page.close()


def test_empty_email(open_home_page, user):
    """
    test empty email enter
    """
    log.info("test empty email")
    home_page = open_home_page
    authentication_page = home_page.sign_in_btn()
    authentication_page.do_login("", user["password"])
    alert = authentication_page.error_message()
    assert "An email address required" in alert
    log.debug("test was successful you didn't log in")


def test_empty_password(open_home_page, user):
    """
    test empty password enter
    """
    log.info("test empty password")
    home_page = open_home_page
    authentication_page = home_page.sign_in_btn()
    authentication_page.do_login(user["email"], "")
    alert = authentication_page.error_message()
    assert "Password is required" in alert
    log.debug("test was successful you didn't log in")



def test_wrong_email(open_home_page, user):
    """
        test wrong email enter
    """
    log.info("test wrong email")
    home_page = open_home_page
    authentication_page = home_page.sign_in_btn()
    authentication_page.do_login("asdasdwxz.com", user["password"])
    alert = authentication_page.error_message()
    assert "Invalid email address" in alert
    log.debug("test was successful you didn't log in")



def test_wrong_password(open_home_page, user):
    """
    test wrong password enter
    """
    log.info("test wrong password")
    home_page = open_home_page
    authentication_page = home_page.sign_in_btn()
    authentication_page.do_login(user["email"], "000")
    alert = authentication_page.error_message()
    assert "Invalid password" in alert
    log.debug("test was successful you didn't log in")



def test_user(open_home_page, user):
    """
    test none-existing user
    """
    log.info("test none-existing user")
    home_page = open_home_page
    authentication_page = home_page.sign_in_btn()
    authentication_page.do_login("asdzgfgfgh@yahoo.com", "13467985")
    alert = authentication_page.error_message()
    assert "Authentication failed" in alert
    log.debug("test was successful you didn't log in")

#Last test to fix
def test_buy_dress(open_home_page, user):
    """
    test find the cheapest dress and buy it
    :param open_home_page:open home page
    :param user:gets the user details
    :return:buy the cheapest dress
    """
    log.info("test buying cheapest dress")
    home_page = open_home_page
    authentication_page = home_page.sign_in_btn()
    account_page = authentication_page.do_login(user["email"], user["password"])
    home_page = account_page.home_btn()
    search_result = home_page.search_box("summer")
    time.sleep(3)
    cheapest_dress = search_result.find_cheapest_dresss()
    time.sleep(5)
    final_process = search_result.mouse_actionn(cheapest_dress)
    end_of_sail = final_process.order_process()
    last_text = end_of_sail.locator("#center_column > p.alert.alert-success")
    assert "Your order on My Store is complete." in last_text.inner_text()
    log.debug("test was successful you bought the cheapest summer dress")
