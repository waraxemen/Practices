from pages.base import AuthPage, MainPage
import pickle


def test_authorisation(web_browser):  # запускается первым для получения печеньки
    page = AuthPage(web_browser)
    page.email.send_keys('api@api')
    page.password.send_keys("api@api")
    page.btn.click(1)  # 1 - click hold 1 second on login button

    assert page.get_current_url() == 'https://petfriends.skillfactory.ru/all_pets'

    with open('../my_cookies.txt', 'wb') as cookies:  # создание файла с cookies
        pickle.dump(web_browser.get_cookies(), cookies)  # сохранение cookies в файл
    page.quit()


def test_petfriends(web_browser):
    """ Authorize to Petfriends via cookies and create a screenshot when loginpage is successfull. """

    page = MainPage(web_browser)
    # Scroll down till the end using actionchains and click on the last image
    page.scroll_down()
    # Make the screenshot of browser window:
    page._web_driver.save_screenshot('petfriends.png')


def test_all_images_completely_loaded(web_browser):
    """This is advanced test which also checks that all images completely loaded."""
    page = MainPage(web_browser)
    page.open_page(web_browser)

#  примеры использования JavaScript, more info: http://allselenium.info/javascript-using-python-selenium-webdriver/
#     web_browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 1
#     JavaScript = "document.getElementsByName('username')[0].click();"  # 2
#     web_browser.execute_script(JavaScript)

