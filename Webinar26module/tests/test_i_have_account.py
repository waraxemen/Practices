import time

from selenium.webdriver.common.by import By
from pages.start_page import ClickOnButton
from pages.start_page import Locators
from selenium.webdriver.support.wait import WebDriverWait


def test_i_have_account(browser):
    start_page = ClickOnButton(browser)
    start_page.click_on_registration_button()
    assert browser.find_element(By.XPATH, "//a[contains(text(),'У меня уже есть аккаунт')]")


def test_button_is_clickable(browser):
    button = ClickOnButton(browser)
    button.click_on_logo_button()
    time.sleep(1)
    assert browser.find_element(By.CLASS_NAME, "navbar-brand.header2")



