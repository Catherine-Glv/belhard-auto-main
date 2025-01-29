from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def _define_locator_type(self, locator: str):
        if '//' in locator:
            return By.XPATH
        return By.CSS_SELECTOR

    def __wait(self, locator: str, time_out: int = 10):
        by_type = self._define_locator_type(locator)
        element = WebDriverWait(driver=self.driver, timeout=time_out).until(
            method=EC.presence_of_element_located((by_type, locator)))

        return element

    def click(self, locator: str):
        element = self.__wait(locator=locator)

        element.click()

    def enter_text(self, locator: str, text: str):
        # by_type = self._define_locator_type(locator=locator)
        element = self.__wait(locator=locator)

        # element = self.driver.find_element(by=by_type, value=locator)
        element.send_keys(text)

    def get_text(self, locator: str):
        elements = self.__wait(locator=locator)

        return elements.text

    def open_url(self, url: str):
        self.driver.get(url=url)

    def close_browser_window(self):
        self.driver.quit()

