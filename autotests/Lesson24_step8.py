import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button = browser.find_element(By.ID, "book")
    button.click()

    # button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    # confirm = browser.switch_to.alert.accept()
    # new_page = browser.window_handles[1]
    # browser.switch_to.window(new_page)

    #Поиск элементов
    x = browser.find_element(By.ID, "input_value")
    x_t = int(x.text)

    input_a = browser.find_element(By.CSS_SELECTOR, "input[name='text']").send_keys(str(calc(x_t)))

    #Подтверждение результата
    submit = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
# Всегда оставлять пустую строку