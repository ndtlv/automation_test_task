from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.locators import LandingPageLocators


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.locators = LandingPageLocators()

    def find_element(self, element_data: tuple):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(element_data))
        return self.driver.find_element(*element_data)

    def click_element(self, element_data: tuple):
        element = self.find_element(element_data)
        element.click()

    def send_data_to_element(self, element_data: tuple, data: str):
        element = self.find_element(element_data)
        element.send_keys(data)
