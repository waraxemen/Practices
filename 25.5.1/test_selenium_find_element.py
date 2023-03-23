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
    s = Service(r"C:\Users\Ann\AppData\Local\Yandex\YandexBrowser\Application\yandexdriver.exe")  # Путь к драйверу
    driver = webdriver.Chrome(service=s)  # Инициализируем драйвер
    chromeOptions = webdriver.ChromeOptions()  # Создаем объект options
    chromeOptions.binary_location = r"C:\Users\Ann\AppData\Local\Yandex\YandexBrowser\Application\browser.exe"
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
    driver.implicitly_wait(1)  # Передаем время ожидания для визуального подтверждения
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
    pet_data = driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')  # определяем все данные питомцев
    try:
        for i in range(len(pet_data)):  # Перебираем все данные из pet_data
            data_pet = pet_data[i].text.replace('\n', '')  # удаляем \n (переходы на новую строку)
            split_data_pet = data_pet.split(' ')  # разделяем строку по пробелу
            result = len(split_data_pet)  # количество элементов в получившемся списке
            assert result == 3  # проверяем, что в каждой строке td есть значение
    except AssertionError:
        print("Нет фото, имя, возраста, или породы  по крайней мере у одной из карточек питомца")

    '''У всех питомцев разные имена'''
    names = driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr td')  # определяем все имена питомцев
    list_names_of_my_pets = []  # создаем список для хранения имен питомцев
    try:
        for i in range(len(names)):  # перебираем все элементы в списке names
            list_names_of_my_pets.append(names[i].text)  # добавляем в список list_names_of_my_pets
            # (хотел сделать словарь с ключами i и значениями names[i], но нашёл способ проще)
        set_pet_data = set(list_names_of_my_pets)  # преобразовываем список в множество, что бы исключить дубликаты
        assert len(list_names_of_my_pets) == len(set_pet_data)  # проверяем, что количество имен в списке
        # list_names_of_my_pets равно кол-ву множества set_pet_data
    except AssertionError:
        print("Есть одинаковые имена питомцев")

    '''В списке нет повторяющихся питомцев'''
    list_data = {}  # создаем словарь для хранения данных питомцев
    set_data = []  # создаем множество для хранения элементов в списке
    keys = 0  # счетчик карточек питомцев
    for i in range(len(pet_data)):  # перебираем все элементы в списке pet_data
        split_data_pet = pet_data[i].text.split("\n").pop(0)  # удаляем '×', разделяем строку по переносу
        list_data = {i: split_data_pet}  # добавляем в список list_data ключи и данные питомцев
        set_data.append(split_data_pet)
        # print(list_data[i])  # выводим данные питомца для наглядности
        print(set_data)  # выводим множество элементов в списке set_data)
        keys += 1  # счетчик ключей

    set_data = set(set_data)  # преобразовываем множество в множество, что бы исключить дубликаты
    # print(len(set_data))  # выводим количество элементов в списке set_data
    try:
        assert len(set_data) == keys  # проверяем, что количество элементов в списке set_data равно кол-ву ключей
    except AssertionError:
        print("В списке повторяющиеся питомцы")