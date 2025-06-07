import time
from selenium.webdriver.common.by import By

class TestItems():
    def test_add_button_displayed(self, browser):
        browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
        time.sleep(10)
        add_to_basket_button = browser.find_element(By.ID, "add_to_basket_form")
        assert add_to_basket_button.is_displayed()
