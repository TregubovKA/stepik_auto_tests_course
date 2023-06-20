import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: '--browser_name=chrome' or '--browser_name=firefox'")

    parser.addoption('--language', action='store', default="ru",
                     help="Choose language: '--language=en' or '--language=ru'")

@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test..")
    user_language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {"intl.accept_languages": user_language})
        browser = webdriver.Chrome(options=options)
        browser.implicitly_wait(20)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        options_f = OptionsFirefox()
        options_f.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(options=options_f)
        browser.implicitly_wait(20)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    browser.quit()
