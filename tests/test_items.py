import time
from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_language_interface(browser):
    browser.get(link)
    time.sleep(30)
    element = browser.find_element(By.XPATH, "//*[@id='add_to_basket_form']/button")
    assert element, "Button Add to Basket is not presented"
