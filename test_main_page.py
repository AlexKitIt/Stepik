
from .pages.login_page import LoginPage
from .pages.main_page import MainPage


link = "http://selenium1py.pythonanywhere.com/"


def test_guest_can_go_to_login_page(browser):
    # browser.get(link)
    # login_link = browser.find_element_by_css_selector("#login_link")
    # login_link.click()
    page= MainPage(browser)
    page.open(link)
    page.go_to_login_page()
    # page.should_be_login_link()
    login_page= LoginPage(browser)
    login_page.should_be_login_page()
    


