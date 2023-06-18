from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_items(browser):
    browser.get(link)
    assert browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket"), 'basket button not found'