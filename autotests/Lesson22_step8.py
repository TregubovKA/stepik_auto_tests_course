import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By

cur_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(cur_dir, '123.txt')

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, "input[name='firstname']").send_keys("Kirill")
    input2 = browser.find_element(By.CSS_SELECTOR, "input[name='lastname']").send_keys("Tregubov")
    input3 = browser.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys("abc@mail.ru")

    input_f = browser.find_element(By.CSS_SELECTOR, "input[name='file']").send_keys(file_path)

    #Подтверждение результата
    submit = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
# Всегда оставлять пустую строку