from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://petfriends.skillfactory.ru/"
        driver.get(self.base_url)

    def open(self):
        return self.driver.get(self.base_url)

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator), message = f'("Element {locator} is not found")')




