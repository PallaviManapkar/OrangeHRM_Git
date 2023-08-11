import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
@pytest.fixture
def setup(browser):
        # options = Options()
        # options.binary_location = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
        # driver = webdriver.Firefox(options=options)
    if browser == "Chrome":
        driver = webdriver.Chrome()
    elif browser == "Edge":
        driver = webdriver.Edge()
    elif browser == "Safari":
        driver = webdriver.Safari()
    else:
        win_options = webdriver.ChromeOptions()
        win_options.add_argument("headless")
        driver = webdriver.Chrome(options=win_options)
        driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    yield driver
    driver.quit()

