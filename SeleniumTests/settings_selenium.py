from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

s = Service(r"C:\Users\Ann\AppData\Local\Yandex\YandexBrowser\Application\yandexdriver.exe")
driver = webdriver.Chrome(service=s)
chromeOptions = webdriver.ChromeOptions()
chromeOptions.binary_location = r"C:\Users\Ann\AppData\Local\Yandex\YandexBrowser\Application\browser.exe"

