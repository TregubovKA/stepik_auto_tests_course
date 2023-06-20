import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Сбор необходимых данных и расчет по формуле из функции
    x_element = browser.find_element(By.CSS_SELECTOR, "span[id='input_value']")
    x = x_element.text
    y = calc(x)

    # Ввод данных в поле ввода
    input1 = browser.find_element(By.CSS_SELECTOR, "input[id='answer']")
    input1.send_keys(y)

    #Выбор нужных чекбоксов и переключателей
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