import pytest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver


@pytest.fixture(scope = 'session')  # autouse=True
def browser():  # driver
    s = Service(r"C:\Users\Администратор\AppData\Local\Yandex\YandexBrowser\Application\yandexdriver.exe")  # Путь к драйверу
    driver = webdriver.Chrome(service=s)  # Инициализируем драйвер
    chromeOptions = webdriver.ChromeOptions()  # Создаем объект options
    chromeOptions.binary_location = r"C:\Users\Администратор\AppData\Local\Yandex\YandexBrowser\Application\browser.exe"
    # driver.get('http://petfriends.skillfactory.ru/login')  # Переходим на страницу авторизации (pytest.driver)
    # driver.maximize_window()  # Развернем окно
    yield driver   # Возвращаем объект pytest.driver
    driver.quit()  # Закрываем браузер