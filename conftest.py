import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        options = ChromeOptions()
        driver = webdriver.Chrome(options=options)

    elif browser == "edge":
        options = EdgeOptions()
        driver = webdriver.Edge(options=options)

    else:
        raise ValueError("Browser not supported: " + browser)

    yield driver
    driver.quit()
