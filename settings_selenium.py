''' заходишь на https://github.com/yandex/YandexDriver/releases выбираешь в 23.1.0-stable нужную версию 64/32 винды'''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service(r"C:\Users\User\AppData\Local\Yandex\YandexBrowser\Application\yandexdriver.exe")
driver = webdriver.Chrome(service=s)
chromeOptions = webdriver.ChromeOptions()
chromeOptions.binary_location = r"C:\Users\User\AppData\Local\Yandex\YandexBrowser\Application\browser.exe"
