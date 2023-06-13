import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #Поиск элементов
    x = browser.find_element(By.ID, "input_value")
    x_t = int(x.text)

    y = calc(x_t)

    #input = browser.find_element(By.ID, "answer").send_keys(str(y))

    input = browser.find_element(By.ID, "answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input)
    input.send_keys(str(y))

    # Выбор нужных чекбоксов и переключателей
    checkbox = browser.find_element(By.CSS_SELECTOR, "input[id='robotCheckbox']")
    checkbox.click()

    radio = browser.find_element(By.CSS_SELECTOR, "input[id='robotsRule']")
    radio.click()

    #Подтверждение результата
    submit = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
# Всегда оставлять пустую строку