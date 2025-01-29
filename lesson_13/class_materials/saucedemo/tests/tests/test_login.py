import pytest
from lesson_13.class_materials.saucedemo.tests.locators.login_page_locators import LoginPageLocators
from lesson_13.class_materials.saucedemo.tests.pages.login_page import LoginPage
import allure

@pytest.mark.usefixtures('setup')
class TestLogin:
    def test_login_page_opened(self, setup):
        login_page = LoginPage(setup)
        login_page.open_login_page()
        assert login_page.is_login_page_opened(), 'Страница логина не открылась'

    def test_login_fields_visible(self, setup):
        login_page = LoginPage(setup)
        login_page.open_login_page()
        assert login_page.find_element(LoginPageLocators.LOGIN_FIELD), 'Поле логина отсутствует'
        assert login_page.find_element(LoginPageLocators.PASSWORD_FIELD), 'Поле пароля отсутствует'

    def test_login_button_clickable(self, setup):
        login_page = LoginPage(setup)
        login_page.open_login_page()
        assert login_page.is_login_button_clickable(), 'Кнопка входа не кликабельна'

    def test_happy_path_login(self, setup):
        login_page = LoginPage(setup)
        login_page.open_login_page()
        login_page.login('standard_user', 'secret_sauce')
        expected_url = 'https://www.saucedemo.com/inventory.html'
        assert setup.current_url == expected_url, f'Ожидался URL {expected_url}, но получили {setup.current_url}'

    def test_negative_login(self, setup):
        login_page = LoginPage(setup)
        login_page.open_login_page()
        login_page.login('1231241', 'qqqqqqqqqq')
        error_text = login_page.get_error_message()
        assert 'Invalid credentials' in error_text, 'Сообщение об ошибке не отображается'
