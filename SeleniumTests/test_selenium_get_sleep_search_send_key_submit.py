from settings_selenium import *

def test_search_example():
    driver.get('https://google.com')
    time.sleep(2)
    search_input = driver.find_element(By.NAME, 'q')
    search_input.clear()
    search_input.send_keys('first test')
    time.sleep(2)
    search_button = driver.find_element(By.NAME, 'btnK')
    search_button.submit()  # метод click() не сработает (так как кнопка скрыта другим элементом)
    time.sleep(2)
    driver.save_screenshot('result.png')
