from pages.base import AuthPage
import pytest
import pickle
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
# from pages.base import tab_phone_is_active, tab_mail_is_active, tab_login_is_active, tab_ls_is_active
def web_browser(request, selenium):  # use this for yandex driver instead of 2 strings above
    browser = selenium   # use this for yandex driver
    # browser.set_window_size(1080, 720)
    browser.maximize_window()  # Развернем окно

    # Return browser instance to test case:
    yield browser

phone = ('+7 242 424-24-22')
login = "kopcarv2"
email = 'test@mail.ru'
ls = '123456789012'
password = 'Test_pass1'
wrong_password = 'Test_pass2'
wrong_phone = '+71234567890'
# name = 'Си'
# tab_phone_is_active = web_browser.find_element(By.XPATH,"//div[@id='t-btn-tab-phone'][@class='rt-tab rt-tab--small rt-tab--active']")
# tab_mail_is_active = WebElement(xpath= "//div[@id='t-btn-tab-mail'][@class='rt-tab rt-tab--small rt-tab--active']")
# tab_login_is_active = WebElement(xpath= "//div[@id='t-btn-tab-login'][@class='rt-tab rt-tab--small rt-tab--active']")
# tab_ls_is_active = WebElement(xpath= "//div[@id='t-btn-tab-ls'][@class='rt-tab rt-tab--small rt-tab--active']")

# page = AuthPage(web_browser)
a=[]
b=[]
c=[]
d=[]
@pytest.mark.parametrize('value, tab', [(phone, a), (email, b),(login, c), (ls, d)])
def test_phone_auth_auto_changing(web_browser, value, tab):
    page = AuthPage(web_browser)
    a = page.tab_phone_is_active
    b = page.tab_mail_is_active
    c = page.tab_login_is_active
    d = page.tab_ls_is_active

    page.tab_phone.click(0.3)  # кликаем на вкладку "Телефон"
    page.first_field.send_keys(value)  # вводим значение
    page.password_field.click(0.4)  # кликаем на вкладку "Пароль" чтобы дать возможность 1 вкладке поменяться
    assert page.tab.find()


# tab_phone_is_active = web_browser.find_element(By.XPATH, "//div[@id='t-btn-tab-phone'][@class='rt-tab rt-tab--small rt-tab--active']")
# tab_mail_is_active = web_browser.find_element(By.XPATH, "//div[@id='t-btn-tab-mail'][@class='rt-tab rt-tab--small rt-tab--active']")
# tab_login_is_active = web_browser.find_element(By.XPATH,"//div[@id='t-btn-tab-login'][@class='rt-tab rt-tab--small rt-tab--active']")
# tab_ls_is_active = web_browser.find_element(By.XPATH,"//div[@id='t-btn-tab-ls'][@class='rt-tab rt-tab--small rt-tab--active']")


"""Авторизация клиента по номеру телефона с валидными параметрами"""
def test_valid_authorisation(web_browser):  # авторизация
    page = AuthPage(web_browser)  # для удобства создаём указатель на функцию авторизации с паролем
    page.tab_phone.click(0.3)  # кликаем на вкладку "Телефон"
    page.first_field.send_keys(phone)  # вводим номер телефона
    page.password_field.send_keys(password)  # вводим пароль
    page.btn.click(1)  # жмём кнопку "Войти"
    assert page.phone_action.find()  # проверяем, что появилась настройка "Телефон" в ЛК


"""Авторизация клиента по номеру телефона с невалидным паролем"""
def test_invalid_password_authorisation(web_browser):
    page = AuthPage(web_browser)  # для удобства создаём указатель на функцию авторизации с паролем
    page.tab_phone.click(0.3)  # кликаем на вкладку "Телефон"
    page.first_field.send_keys(phone)  # вводим номер телефона
    page.password_field.send_keys(wrong_password)  # вводим невалидный пароль
    page.btn.click(1)  # жмём кнопку "Войти"
    assert not page.phone_action.find()  # проверяем, что не появилась настройка "Телефон" в ЛК


"""Авторизация клиента по номеру телефона с невалидным номером телефона """
def test_invalid_phone_authorisation(web_browser):
    page = AuthPage(web_browser)  # для удобства создаём указатель на функцию авторизации с паролем
    page.tab_phone.click(0.3)  # кликаем на вкладку "Телефон"
    page.first_field.send_keys(wrong_phone)  # вводим значение с невалидным номером телефона
    page.password_field.send_keys(password)  # вводим пароль
    page.btn.click(1)  # жмём кнопку "Войти"
    assert not page.phone_action.find()  # проверяем, что не появилась настройка "Телефон" в ЛК


"""Наличие всех вкладок"""
def test_all_tabs_are_visible(web_browser):
    page = AuthPage(web_browser)  # для удобства создаём указатель на функцию авторизации с паролем
    assert page.tab_phone.is_visible()
    assert page.tab_mail.is_visible()
    assert page.tab_login.is_visible()
    assert page.tab_ls.is_visible()

"""Проверка кнопки "Забыл пароль" на странице авторизации"""
def test_button_forgot_password(web_browser):
    page = AuthPage(web_browser)  # для удобства создаём указатель на функцию авторизации с паролем
    page.button_forgot_password.click(0.3)  # кликаем на кнопку "Забыл пароль"
    text = page.title.get_text()  # получаем текст
    assert text == "Восстановление пароля"

"""Продуктовый слоган ЛК 'Ростелеком ID'."""
def test_product_skill(web_browser):
    page = AuthPage(web_browser)
    page.open_page(web_browser)
    text = page.slogan.get_text()  # получаем текст слогана
    assert text != '' and page.left_panel.is_visible()  # проверяем, что слоган есть и левая панель отображается

"""Кнопка "Зарегистрироваться" на странице авторизации"""
def test_button_register(web_browser):
    page = AuthPage(web_browser)
    page.button_register.click(0.3)  # кликаем на кнопку "Зарегистрироваться"
    assert page.button_register_in  # проверяем, что появилась кнопка "Зарегистрироваться" на странице регистрации

"""Форма ввода имени - валидное имя"""
@pytest.mark.parametrize('name', ['Си', 'Иван', 'Маша', 'Джон', 'Александра', 'Иван-Чай'])
def test_input_name(web_browser, name):
    page = AuthPage(web_browser)
    page.button_register.click(0.3)  # кликаем на кнопку "Зарегистрироваться"
    page.input_name.send_keys(name)




# def test_authorisation(web_browser):  # запускается первым для получения печеньки
#     page = AuthPage(web_browser)
#     page.email.send_keys('api@api')
#     page.password.send_keys("api@api")
#     page.btn.click(1)  # 1 - click hold 1 second on login button
#
#     assert page.get_current_url() == 'https://petfriends.skillfactory.ru/all_pets'
#
#     with open('../my_cookies.txt', 'wb') as cookies:  # создание файла с cookies
#         pickle.dump(web_browser.get_cookies(), cookies)  # сохранение cookies в файл
#     page.quit()
#
#
# def test_petfriends(web_browser):
#     """ Authorize to Petfriends via cookies and create a screenshot when loginpage is successfull. """
#
#     page = MainPage(web_browser)
#     # Scroll down till the end using actionchains and click on the last image
#     page.scroll_down()
#     # Make the screenshot of browser window:
#     page._web_driver.save_screenshot('petfriends.png')
#
#
# def test_all_images_completely_loaded(web_browser):
#     """This is advanced test which also checks that all images completely loaded."""
#     page = MainPage(web_browser)
#     page.open_page(web_browser)

#  примеры использования JavaScript, more info: http://allselenium.info/javascript-using-python-selenium-webdriver/
#     web_browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 1
#     JavaScript = "document.getElementsByName('username')[0].click();"  # 2
#     web_browser.execute_script(JavaScript)

