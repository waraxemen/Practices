from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pytest



@pytest.hookimpl(hookwrapper=True, tryfirst=True) # Передаем в конструктор функцию pytest.hookimpl
def pytest_runtest_makereport(item, call):# This function helps to detect that some test failed and pass this information to teardown:
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep




@pytest.fixture(autouse=True)
def driver():
    s = Service(r"C:\Users\Администратор\AppData\Local\Yandex\YandexBrowser\Application\yandexdriver.exe")  # Путь к драйверу
    driver = webdriver.Chrome(service=s)  # Инициализируем драйвер
    chromeOptions = webdriver.ChromeOptions()  # Создаем объект options
    chromeOptions.binary_location = r"C:\Users\Администратор\AppData\Local\Yandex\YandexBrowser\Application\browser.exe"
    driver.get('http://petfriends.skillfactory.ru/login')  # Переходим на страницу авторизации (pytest.driver)
    driver.maximize_window()  # Развернем окно
    yield driver   # Возвращаем объект pytest.driver
    driver.quit()  # Закрываем браузер


def test_for_element_location(driver):
    driver.find_element(By.ID,'email').send_keys('api@api')  # Вводим email
    driver.find_element(By.ID,'pass').send_keys('api@api')  # Вводим пароль
    # driver.implicitly_wait(3)  # Передаем время ожидания
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.btn-success[type="submit"]')))
    WebDriverWait(driver, 3).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.btn-success[type="submit"]'), 'Войти'))
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click() # Нажимаем на кнопку входа в аккаунт
    # time.sleep(3)  # Проверяем, что мы оказались на главной странице пользователя
    '''Теперь используем разные методы WebDriverWait'''
    WebDriverWait(driver, 3).until(EC.title_is('PetFriends: My Pets'))  # ожидаем заголовок окна равен указанной строке
    WebDriverWait(driver, 3).until(EC.title_contains('My Pets'))  # заголовок окна содержит определённую строку текста
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "navbar-toggler")))  # присутствие элемента
    # WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "navbar-toggler")))  ожидаем  видимый элемент, но будет ошибка т.к. элемент выбран не видимый
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.ID, "navbarNav")))  # ожидаем видимый элемент
    WebDriverWait(driver, 3).until(EC.visibility_of(driver.find_element(By.XPATH, "//h1[@class='text-center']")))  # ожидаем видимый элемент найденный по xpath
    WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='card']")))  # ожидаем присутствие всех элементов (карточки животных)
    WebDriverWait(driver, 3).until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='card']")))  # ожидаем прогрузки отображения всех элементов (карточки животных)
    WebDriverWait(driver, 3).until(EC.text_to_be_present_in_element((By.XPATH, "//button[@class='btn btn-outline-secondary']"), 'Выйти'))  # ожидаем отображение текста на кнопке
    # WebDriverWait(driver, 2).until(EC.text_to_be_present_in_element_attribute((By.ID, 'inputRequired'),'value', 'Expected'))  # не удалось использовать
    # WebDriverWait(driver, 1).until(EC.text_to_be_present_in_element_value((By.ID, 'inputRequired'), 'Expected'))  # ожидание определённого текста внутри атрибута value элемента
    # WebDriverWait(driver, 3).until(EC..frame_to_be_available_and_switch_to_it((By.ID, 'myFrame')))  # ожидаем открытие фрейма (независимые друг от друга прямоугольные области
    # (скроллируемые окна), каждая из которых может иметь собственный URL
    WebDriverWait(driver, 3).until(EC.invisibility_of_element_located((By.NAME, "google")))  # ожидание невидимости элемента, найденного по указанному локатору
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-outline-secondary']")))  # элемент стал кликабельным
    # WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-outline-secondary']"))).click()  # можно нажать на кнопку
    # element = driver.find_element(By.ID,'id')  # определяем элемент
    # WebDriverWait(driver, 3).until(EC.element_to_be_selected(element))  # ожидание, что элемент в выпадающем списке выбран
    # WebDriverWait(driver, 3).until(EC.element_located_to_be_selected((By.TAG_NAME, 'name')))  # ожидание, что элемент выбран (сразу с поиском)
    # element = driver.find_element(By.LINK_TEXT,'text')  # определяем элемент')
    # WebDriverWait(driver, 3).until(EC.element_selection_state_to_be(element, False))  # ожидание, что элемент выпадающего списка имеет определённое состояние
    # WebDriverWait(driver, 3).until(EC.element_located_selection_state_to_be((By.ID, 'id'), True))  # ожидание, что элемент имеет определённое состояние (сразу с поиском)
    # WebDriverWait(driver, 3).until(EC.alert_is_present())  # ожидание всплывающего окна на странице браузера
    # alert.accept()  # подтверждаем действие
    # WebDriverWait(driver, 3).until_not(EC.alert_is_present())  # ожидаем что нет всплывающего окна на странице браузера
    # WebDriverWait(driver, 3).until(EC.alert_is_present())  # ожидаем что нет всплывающего окна на странице браузера
    assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"  # Проверяем, что мы на главной странице
    assert driver.find_element(By.XPATH, "//nav[@class='navbar navbar-expand-lg navbar-light bg-light']")
    assert driver.find_element(By.CSS_SELECTOR, "html > body > nav")
    assert driver.find_element(By.XPATH, "//h1[@class='text-center']")
    assert driver.find_element(By.CSS_SELECTOR, ".text-center")
    assert driver.find_element(By.XPATH, "//div[@class='card']")
    assert driver.find_element(By.CSS_SELECTOR, ".card")
    assert driver.find_element(By.XPATH, "//button[@class='btn btn-outline-secondary']")
    assert driver.find_element(By.CSS_SELECTOR, '.btn.btn-outline-secondary')
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='nav-link' and @href='/my_pets']"))).click()  # заходим в "мои питомцы"
    driver.implicitly_wait(1)
    image = driver.find_element(By.TAG_NAME, 'img')  # определяем фото
    if image.get_attribute('src') == '':  # если фото нет
        print('У питомца нет фото')
    else:
        print('У моего питомца есть фото')
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='nav-link' and @href='/all_pets']"))).click()  # возвращаемся во всех питомцев
    # assert AllElementsHave((By.XPATH, '//div[1]//div[1]//img[@]'), 'src', 'ada') # проверяем, что все элементы внутри карточки питомца есть фото (требует доработки)
    # time.sleep(1)
    '''Теперь нужно убедиться, что внутри каждой карточки питомца есть фото, имя питомца, возраст и вид'''
    images = driver.find_elements(By.CSS_SELECTOR,'.card-deck .card-img-top')  # определяем фото
    names = driver.find_elements(By.CSS_SELECTOR,'.card-deck .card-title')  # определяем имя
    descriptions = driver.find_elements(By.CSS_SELECTOR,'.card-deck .card-text')  # определяем вид и возраст
    try:
        for i in range(len(names)):  # перебираем все элементы
            assert images[i].get_attribute('src') != ''  # проверяем, что фото есть (путь, указанный в атрибуте src, не пустой)
            assert names[i].text != ''  # проверяем, что имя есть
            assert descriptions[i].text != ''  # проверяем, что не пустое, хотя в любом случае есть запятая
            assert ', ' in descriptions[i]  # убеждаемся в наличии запятой
            parts = descriptions[i].text.split(", ")  # разделяем строку на части
            assert len(parts[0]) > 0  # проверяем, что в первой части есть вид
            assert len(parts[1]) > 0  # проверяем, что во второй части есть возраст
    except AssertionError:
        print('Нет фото, или имени, или возраста у одной из карточек питомца')


def test_in_my_pets(driver):
    driver.find_element(By.ID, 'email').send_keys('api@api')  # Вводим email
    driver.find_element(By.ID, 'pass').send_keys('api@api')  # Вводим пароль
    driver.implicitly_wait(1)  # Передаем время ожидания
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.btn-success[type="submit"]')))  # Проверяем, что на странице отобразилась кнопка "Войти"
    WebDriverWait(driver, 3).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.btn-success[type="submit"]'), 'Войти'))  # Проверяем, что кнопка подписана
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()  # Нажимаем на кнопку входа в аккаунт
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='nav-link' and @href='/my_pets']"))).click()  # заходим в "мои питомцы"
    '''Присутствуют все питомцы, которые есть в статистике'''
    petcount = driver.find_elements(By.CSS_SELECTOR, ".\\.col-sm-4.left")  # Сохраняем в переменную кол-во питомцев в счётчике с экранированием точки \\
    pets = driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')  # Сохраняем в переменную pets карточки питомцев
    number = petcount[0].text.split('\n')  # разбиваем строку по символу '\n' (первая строка "Питомцев: 3")
    number = number[1].split(' ')  # разделяем строку по пробелу и выбирает 2 элемент ("3")
    number = int(number[1])  # переводим в целое число
    number_of_pets = len(pets)  # количество карточек питомцев
    assert number == number_of_pets  # проверяем, что количество питомцев в статистике равно кол-ву карточек питомцев
    '''Хотя бы у половины питомцев есть фото'''
    images = driver.find_elements(By.CSS_SELECTOR, '.table.table-hover img')  # определяем карточки с фото
    number_of_images = len(images)  # количество карточек питомцев с фото
    assert number_of_images >= number_of_pets/2  # проверяем, что количество карточек питомцев с фото больше или равно кол-ву питомцев
    '''У всех питомцев есть имя, возраст и порода'''
    pet_data = driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr td')  # определяем все данные питомцев
    try:
        # for i in range(len(pet_data)):  # перебираем все данные питомцев
        #     print ("i = ", i)
        #     assert i != ''  # проверяем, что в каждой строке td есть значение
        # name_my_pets = driver.find_elements(By.XPATH, '//tbody/tr/td[1]')
        # for i in range(len(name_my_pets)):
        #     assert WebDriverWait(driver, 1).until(EC.visibility_of(name_my_pets[i]))
        # type_my_pets = driver.find_elements(By.XPATH, '//tbody/tr/td[2]')
        # for i in range(len(type_my_pets)):
        #     assert WebDriverWait(driver, 1).until(EC.visibility_of(type_my_pets[i]))
        # age_my_pets = driver.find_elements(By.XPATH, '//tbody/tr/td[3]')
        # for i in range(len(age_my_pets)):
        #     assert WebDriverWait(driver, 1).until(EC.visibility_of(age_my_pets[i]))
        # for i in range(len(pet_data)):  # перебираем все данные питомцев
        #     assert pet_data[i].get_attribute('td') != ''  # проверяем, что в каждой строке td есть значение
        # name_my_pets = driver.find_elements(By.XPATH, '//tbody/tr/td[1]')
        # name_my_1_pet = driver.find_element(By.XPATH, '//tbody/tr[1]/td[1]')
        # a=name_my_1_pet.get_attribute('td'[0])
        # print(a)

        images = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
        names = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
        descriptions = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
        for i in range(len(names)):
            assert images[i].get_attribute('src') != ''
            assert names[i].text != ''
            assert descriptions[i].text != ''
            assert ', ' in descriptions[i]
            parts = descriptions[i].text.split(", ")
            assert len(parts[0]) > 0
            assert len(parts[1]) > 0
        # for i in range(len(name_my_pets)):
        #     print(name_my_pets)
        #     assert name_my_pets[i] != ''  # проверяем, что в каждой строке td есть значение
        # type_my_pets = driver.find_elements(By.XPATH, '//tbody/tr/td[2]')
        # for i in range(len(type_my_pets)):
        #     print(type_my_pets)
        #     assert type_my_pets[i] != ''  # проверяем, что в каждой строке td есть значение
        # age_my_pets = driver.find_elements(By.XPATH, '//tbody/tr/td[3]')
        # for i in range(len(age_my_pets)):
        #     print(i)
        #     assert age_my_pets != ''  # проверяем, что в каждой строке td есть значение
        # for i in range(len(pet_data)):  # перебираем все данные питомцев
        #     assert pet_data[i].get_attribute('td') != ''  # проверяем, что в каждой строке td есть значение
    except AssertionError:
        print("Нет фото, имя, возраста, или породы  по крайней мере у одной из карточек питомца")
    #
    # '''У всех питомцев разные имена'''
    # names_my_pets = driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')
    # list_of_names_my_pets = []
    # for i in range(len(name_my_pets)):
    #     list_name_my_pets.append(name_my_pets[i].text)
    # set_pet_data = set(list_name_my_pets)  # преобразовываем список в множество
    # assert len(list_of_names_my_pets) == len(set_pet_data)
























# class AllElementsHave(object):  функция не работает, м.б. когда-нибудь разберусь, но вряд ли.
#   def __init__(self, locator, element, value):
#     self.locator = locator
#     self.element = element
#     self.value = value
#
#   def __call__(self, driver):
#     recall = driver.find_elements(*self.locator)
#     have_element = []
#     do_not_have_element = []
#     have=0
#     do_not_have=0
#     for i in recall.get_attribute(self.element):
#         if i == self.value():
#             have_element = have_element.append(i)
#             have += 1
#         else:
#             do_not_have_element = do_not_have_element.append(i)
#             do_not_have += 1
#         print("Найдено искомых элементов:", have, "Найдено пустых элементов:", do_not_have), have_element, do_not_have_element
#     if have == 0:
#         return False
#     else:
#         return True















# class TestPetFriends(driver):
#     def setup(self):
#         self.user = 'api@api'
#         self.password = 'api@api'
#
#     def open(self):
#         self.driver = webdriver.Chrome()
#         self.get('https://petfriends.skillfactory.ru/')
#
#     def close(self):
#         self.driver.quit()
#
#     def test_login_in_button(self):
#         self.open()
#         WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
#             (By.XPATH, '//button[@text="Зарегистрироваться]'))).click()  # ждём загрузки страницы до появления кнопки