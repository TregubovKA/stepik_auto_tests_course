import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #Поиск элементов для суммы
    num1 = browser.find_element(By.ID, "num1")
    num1_t = int(num1.text)

    num2 = browser.find_element(By.ID, "num2")
    num2_t = int(num2.text)

    #Расчет суммы
    y = num1_t + num2_t

    #Выбор из списка нужного результата
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(y))

    #Подтверждение результата
    submit = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
# Всегда оставлять пустую строку