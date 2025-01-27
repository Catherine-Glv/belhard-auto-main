from .base_page import BasePage
from lesson_12.class_materials.locators import main_page_locators as locator


class MainPage(BasePage):

    URL = 'https://www.21vek.by/'

    def click_cookies(self):
        self.click(locator=locator.BUTTON_COOKIES_APPROVE)

    def click_button_account(self):
        self.click(locator=locator.BUTTON_ACCOUNT_LOCATOR)

    def enter_text_for_input_search_field(self, text: str):
        self.enter_text(locator=locator.FIELD_INPUT_ITEM, text=text)

    def navigate_to_page(self,):
        self.open_url(url=self.URL)
