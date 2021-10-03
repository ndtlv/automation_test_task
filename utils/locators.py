from selenium.webdriver.common.by import By


class LandingPageLocators(object):
    LOGIN_BUTTON_LAUNCH_SCREEN = (By.ID, 'com.ajaxsystems:id/login')
    EMAIL = (By.ID, 'com.ajaxsystems:id/login')
    PASSWORD = (By.ID, 'com.ajaxsystems:id/password')
    BACK = (By.ID, 'com.ajaxsystems:id/back')
    FORGOT_PASSWORD = (By.ID, 'com.ajaxsystems:id/back')
    LOGIN_BUTTON_LOGIN_SCREEN = (By.ID, 'com.ajaxsystems:id/next')
    WRONG_PASS_POPUP = (By.ID, 'com.ajaxsystems:id/snackbar_text')


