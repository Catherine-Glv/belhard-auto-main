from selenium.webdriver.common.by import By
from .base_page import BasePage
from lesson_13.class_materials.saucedemo.tests.locators.login_page_locators import LoginPageLocators

class LoginPage(BasePage):

        def __init__(self, driver):
            super().__init__(driver)
            self.URL = 'https://www.saucedemo.com/'

        def open_login_page(self):
            self.open(self.URL)

        def is_login_page_opened(self):
            return self.find_element(LoginPageLocators.LOGIN_FIELD) and self.find_element(
                LoginPageLocators.PASSWORD_FIELD)

        def is_login_button_clickable(self):
            return self.find_element(LoginPageLocators.LOGIN_BUTTON).is_enabled()

        def login(self, username, password):
            self.send_keys(LoginPageLocators.LOGIN_FIELD, username)
            self.send_keys(LoginPageLocators.PASSWORD_FIELD, password)
            self.click(LoginPageLocators.LOGIN_BUTTON)

        def get_error_message(self):
            return self.find_element(LoginPageLocators.ERROR_MESSAGE).text