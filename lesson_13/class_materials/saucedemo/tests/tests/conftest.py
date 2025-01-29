import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope='function')
def setup():
    service = Service(executable_path=r'X:\PycharmProjects\belhard-auto-main1\lesson_12\chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()
