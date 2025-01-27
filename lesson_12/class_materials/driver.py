import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import locators1

# options = Options()

service = Service(executable_path=r'X:\PycharmProjects\belhard-auto-main1\lesson_12\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get(url='https://www.21vek.by/')

# cookies
# button_approve = driver.find_element(by=By.XPATH, value=locators.BUTTON_COOKIES_APPROVE)

# время ожидания (появление элементов)
button_approve = WebDriverWait(driver=driver, timeout=10).until(
    EC.presence_of_element_located((By.XPATH, locators1.BUTTON_COOKIES_APPROVE)))
button_approve.click()

# find_element

button_account = driver.find_element(by=By.XPATH, value=locators1.BUTTON_ACCOUNT_LOCATOR)
text_account = button_account.text
button_account.click()

# send_keys

field_input = driver.find_element(by=By.XPATH, value=locators1.FIELD_INPUT_ITEM)
field_input.send_keys('Холодильник')

button_basket = driver.find_element(by=By.XPATH, value=locators1.BUTTON_BASKET_LOCATOR)
text_basket = button_basket.text

button_catalog = driver.find_element(by=By.XPATH, value=locators1.BUTTON_CATALOG_ITEMS)
text_catalog = button_catalog.text

driver.quit()
