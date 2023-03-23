from selenium.webdriver.common.by import By
from base_page import BasePage


class Locators:
    LOCATOR_START_HEADER_LOGO = (By.CLASS_NAME, "navbar-brand.header2")
    LOCATOR_START_REGISTRATION_BUTTON = (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]")
    LOCATOR_START_REGISTRATION_FORM_EMAIL = (By.ID, "email")



class ClickOnButton(BasePage):
    def click_on_registration_button(self):
        self.find_element(Locators.LOCATOR_START_REGISTRATION_BUTTON, timeout=10).click()

    def click_on_logo_button(self):
        self.find_element(Locators.LOCATOR_START_HEADER_LOGO, timeout=10).click()

    def enter_email(self, email):
        field = self.find_element(Locators.LOCATOR_START_REGISTRATION_FORM_EMAIL, timeout=10).click.clear().send_keys(email)
        return field

