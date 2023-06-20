import time
import math

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@pytest.mark.parametrize('link',["https://stepik.org/lesson/236895/step/1",
                                 "https://stepik.org/lesson/236896/step/1",
                                 "https://stepik.org/lesson/236897/step/1",
                                 "https://stepik.org/lesson/236898/step/1",
                                 "https://stepik.org/lesson/236899/step/1",
                                 "https://stepik.org/lesson/236903/step/1",
                                 "https://stepik.org/lesson/236904/step/1",
                                 "https://stepik.org/lesson/236905/step/1"])
def test_authorization(browser, link):
    link = f"{link}"
    # link = "https://stepik.org/lesson/236895/step/1"

    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "a.navbar__auth").click()
    browser.find_element(By.CSS_SELECTOR, "#id_login_email").send_keys("kirill.tregubov2011@yandex.ru")
    browser.find_element(By.CSS_SELECTOR, "#id_login_password").send_keys("fs8eHadq5")
    browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn").click()
    time.sleep(1)
    answer = str(math.log(int(time.time())))
    # WebDriverWait(browser, 7).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "textarea.ember-text-area")))
    browser.find_element(By.CSS_SELECTOR, "textarea.ember-text-area").send_keys(answer)
    # WebDriverWait(browser, 7).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission")))
    time.sleep(2)
    browser.find_element(By.CSS_SELECTOR, "button.submit-submission").click()
    WebDriverWait(browser, 7).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "p.smart-hints__hint")))
    result = browser.find_element(By.CSS_SELECTOR, "p.smart-hints__hint")
    ans = result.text
    assert str(ans) == "Correct!", ans


