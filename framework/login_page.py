import pytest
from selenium.common.exceptions import TimeoutException

from framework.page import Page


class LoginPage(Page):
    def __init__(self, driver):
        super().__init__(driver=driver)

    def login(self, email: str, password: str, correct_credentials=True):
        self.click_element(self.locators.LOGIN_BUTTON_LAUNCH_SCREEN)
        self.send_data_to_element(self.locators.EMAIL, email)
        self.send_data_to_element(self.locators.PASSWORD, password)
        self.click_element(self.locators.LOGIN_BUTTON_LOGIN_SCREEN)

        if correct_credentials:
            with pytest.raises(TimeoutException):
                self.find_element(self.locators.WRONG_PASS_POPUP)
        else:
            wrong_pass_popup = self.find_element(self.locators.WRONG_PASS_POPUP)
            assert wrong_pass_popup.text == 'Wrong login or password'
