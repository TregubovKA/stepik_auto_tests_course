from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestReg(unittest.TestCase):
    def test_reg1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля

        input1 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.first")
        input1.send_keys("Kirill")
        input2 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.second")
        input2.send_keys("Tregubov")
        input3 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.third")
        input3.send_keys("kirill.tregubov2011@yandex.ru")
        input4 = browser.find_element(By.CSS_SELECTOR, "div.second_block input.form-control.first")
        input4.send_keys("+79109109101")
        input5 = browser.find_element(By.CSS_SELECTOR, "div.second_block input.form-control.second")
        input5.send_keys("KLG")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


    def test_reg2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля

        input1 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.first")
        input1.send_keys("Kirill")
        input2 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.second")
        input2.send_keys("Tregubov")
        input3 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.form-control.third")
        input3.send_keys("kirill.tregubov2011@yandex.ru")
        input4 = browser.find_element(By.CSS_SELECTOR, "div.second_block input.form-control.first")
        input4.send_keys("+79109109101")
        input5 = browser.find_element(By.CSS_SELECTOR, "div.second_block input.form-control.second")
        input5.send_keys("KLG")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


if __name__ == '__main__':
    unittest.main()
