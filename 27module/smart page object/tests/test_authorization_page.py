from pages.base import AuthPage
import pytest
import pickle
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
# def web_browser(request, selenium):  # use this for yandex driver instead of 2 strings above
#     browser = selenium   # use this for yandex driver
#     # browser.set_window_size(1080, 720)
#     browser.maximize_window()  # Развернем окно
#
#     # Return browser instance to test case:
#     yield browser

phone = ('+7 242 424-24-22')
login = "kopcarv2"
email = 'test@mail.ru'
ls = '123456789012'
password = 'Test_pass1'

# page = AuthPage(web_browser)

# class TestClass(web_browser):
#     page = AuthPage(web_browser)
#     # @pytest.mark.parametrize('value, tab', [(phone, page.tab_phone_is_active), (email, page.tab_mail_is_active), (login, page.tab_login_is_active),
#                                             (ls, page.tab_ls_is_active)])
#     def test_phone_auth_auto_changing(self, web_browser, test_cases):
#         page = AuthPage(web_browser)
#
#
#         page.tab_phone.click(0.3)  # кликаем на вкладку "Телефон"
#         page.first_field.send_keys(value)  # вводим значение
#         page.password_field.click(0.4)  # кликаем на вкладку "Пароль" чтобы дать возможность 1 вкладке поменяться
#     # tab_phone_is_active = web_browser.find_element(By.XPATH, "//div[@id='t-btn-tab-phone'][@class='rt-tab rt-tab--small rt-tab--active']")
#     # tab_mail_is_active = web_browser.find_element(By.XPATH, "//div[@id='t-btn-tab-mail'][@class='rt-tab rt-tab--small rt-tab--active']")
#         assert page.tab.find()
#         return metafunc.parametrize('value, tab', test_cases)




def test_valid_authorisation(web_browser):
    page = AuthPage(web_browser)
    page.tab_phone.click(0.3)  # кликаем на вкладку "Телефон"
    page.first_field.send_keys(phone)  # вводим значение
    page.password_field.send_keys(password)  # вводим пароль
    page.btn.click(1)  # 1 - click hold 1 second on login button
    assert page.phone_action.find()






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

