import time
from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_product_page_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(30)
    basket_button = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
    assert basket_button != None, "Basket button was not found"
