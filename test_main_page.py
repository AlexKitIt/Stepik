from .pages.main_page import MainPage


link = "http://selenium1py.pythonanywhere.com/"

def test_guest_can_go_to_login_page(browser):
    # browser.get(link)
    # login_link = browser.find_element_by_css_selector("#login_link")
    # login_link.click()
    page= MainPage(browser,link)
    page.open()
    # page.go_to_login_page()
    page.should_be_login_link()

