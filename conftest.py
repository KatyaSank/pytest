import pytest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from webdriver_manager.core.utils import ChromeType

# from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture
def driver():
    s = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
    driver = webdriver.Chrome(service=s)
    driver.implicitly_wait(5)

    yield driver

    # driver.close()
    driver.quit()


# def pytest_addoption(parser):
#     parser.addoption("--address", action="store", default="http://192.168.122.244/", help="HuntBox web address")
#     parser.addoption("--browser", action="store", default="firefox", help="Browser name")


