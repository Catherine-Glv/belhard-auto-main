from lesson_12.class_materials.locators import main_page_locators
from lesson_12.class_materials.pages.main_page import MainPage
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import locators1

service = Service(executable_path=r'X:\PycharmProjects\belhard-auto-main1\lesson_12\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()

main_page = MainPage(driver=driver)
main_page.navigate_to_page()

main_page.click_cookies()

main_page.click_button_account()

main_page.enter_text_for_input_search_field(text='Холодильник')

text_account = main_page.get_text(locator=main_page_locators.BUTTON_ACCOUNT_LOCATOR)
text_basket = main_page.get_text(locator=main_page_locators.BUTTON_BASKET_LOCATOR)
text_catalog = main_page.get_text(locator=main_page_locators.BUTTON_CATALOG_ITEMS)

main_page.close_browser_window()
