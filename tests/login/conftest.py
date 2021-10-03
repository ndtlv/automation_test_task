import pytest

from framework import LoginPage


LOGIN = 'qa.ajax.app.automation@gmail.com'
PASSWORDS = {
    'correct_password': 'qa_automation_password',
    'wrong_password': '123456'
}


@pytest.fixture(params=list(PASSWORDS))
def user_login_fixture(page_manager, request):
    login_page = page_manager.create_page(LoginPage)
    password_type = request.param

    login, password = LOGIN, PASSWORDS[password_type]

    yield login_page, login, password, password_type == 'correct_password'

    login_page.driver.reset()
