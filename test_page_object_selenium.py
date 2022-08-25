import time
import pytest
import logging
from page_object_selenium.home_page import HomePage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


# add your specific path to filename to get the log text file
log_format = "%(Levelname)s %(asctime)s - %(message)s"
logging.basicConfig(level=logging.DEBUG, filename="log_file", format=log_format, filemode='w')
log = logging.getLogger()

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_driver_path = "C:/Users/omerb/Desktop/Sela/chromedriver.exe"


@pytest.fixture
def user():
    data = {
        "email": "asdasd@wxz.com",
        "password": "123456"
    }
    return data


@pytest.fixture()
def open_home_page():
    driver = webdriver.Chrome(chrome_driver_path, chrome_options=chrome_options)
    driver.maximize_window()
    driver.get('http://automationpractice.com/index.php')
    yield HomePage(driver)
    time.sleep(1)
    driver.quit()


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
    log.info("test buying cheapest dress")
    home_page = open_home_page
    authentication_page = home_page.sign_in_btn()
    account_page = authentication_page.do_login(user["email"], user["password"])
    home_page = account_page.home_btn()
    search_result = home_page.search_box("summer")
    cheapest_dress = search_result.find_cheapest_dress()
    final_process=search_result.mouse_action(cheapest_dress)
    end_of_sail = final_process.order_process()
    last_text = end_of_sail.find_element(By.CSS_SELECTOR, "#center_column > p.alert.alert-success")
    assert "Your order on My Store is complete." in last_text.text
    log.debug("test was successful you bought the cheapest summer dress")