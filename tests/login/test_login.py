def test_user_login(user_login_fixture):
    login_page, login, password, correct_password = user_login_fixture

    login_page.login(login, password, correct_credentials=correct_password)
