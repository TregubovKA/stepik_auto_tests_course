import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    treasure = browser.find_element(By.ID, "treasure")
    check_treasure = treasure.get_attribute("valuex")

    answer = calc(check_treasure)

    # Ввод данных в поле ввода
    input = browser.find_element(By.ID, "answer")
    input.send_keys(answer)

    # Выбор нужных чекбоксов и переключателей
    checkbox = browser.find_element(By.CSS_SELECTOR, "input[id='robotCheckbox']")
    checkbox.click()

    radio = browser.find_element(By.CSS_SELECTOR, "input[id='robotsRule']")
    radio.click()

    submit = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
# Всегда оставлять пустую строку