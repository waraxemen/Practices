from api import PetFriends
from settings import my_email, my_password, key
import os  # для запуска с консоли необходимо полный путь до фото указывать
pf = PetFriends()

'''получение ключа зарегистрированным пользователем'''
def test_get_api_key_for_valid_user(email=my_email, password=my_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result
    print(result)


'''получение списка всех животных авторизованным пользователем'''
def test_get_all_pets_with_valid_key(filter: str = ''):
    _, auth_key = pf.get_api_key(my_email, my_password)  # т.к. нам выдают email, password, то использовали _ для мыла
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0  # убеждаемся что в ответе по ключу pets есть данные о животных


'''получение списка СВОИХ животных авторизованным пользователем'''
def test_get_my_pets_with_valid_key(filter: str = 'my_pets'):
    _, auth_key = pf.get_api_key(my_email, my_password)  # т.к. нам выдают email, password, то использовали _ для мыла
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0  # убеждаемся что в ответе по ключу pets есть данные о животных
    print(result)


'''добавление животного с фото, авторизованным пользователем'''
def test_post_add_new_pet_with_photo():
    _, auth_key = pf.get_api_key(my_email, my_password)
    name= "Pyshistick"
    animal_type = "Cat"
    age = '1'
    # pet_photo = 'images/Pushistick.jpg' #через PyCharm
    pet_photo = os.path.join(os.path.dirname(__file__), 'images/Pushistick.jpg')  # через консоль, путь до тек. файла +
    status, result = pf.post_add_new_pet_with_photo(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    print(result)


'''удаление последнего добавленного животного авторизованным пользователем'''
def test_delete_new_pet():
    _, auth_key = pf.get_api_key(my_email, my_password)
    _, my_pets= pf.get_list_of_pets(auth_key, filter= "my_pets")  # т.к. 2 значения в ответе, берем 2-список питомцев
    if len(my_pets['pets']) == 0:  # Проверяем - если список своих питомцев пустой, то добавляем нового
        pf.post_add_new_pet_with_photo(auth_key, "Пушистик", "кот", "1", "images/Pushistick.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
        print('Список был пустой')
    pet_id = my_pets ['pets'][0]['id']  # ключ 'pets' содержит 1 значение -[0] список ключей, в котором нам нужен ['id']
    print("удаляемый питомец", pet_id)
    status, result = pf.delete_new_pet(auth_key, pet_id)
    # Проверяем что статус ответа равен 200 и в списке питомцев нет id удалённого питомца
    assert status == 200
    assert pet_id not in my_pets.values()


'''добавление животного БЕЗ ФОТО, авторизованным пользователем'''
def test_post_add_new_pet_without_photo():
    _, auth_key = pf.get_api_key(my_email, my_password)
    name = "Pyshistick"
    animal_type = "Cat"
    age = '1'
    status, result = pf.post_add_new_pet_without_photo(auth_key, name, animal_type, age)
    assert status == 200
    print(result)


'''добавление фото для ЛЮБОГО животного без фото, авторизованным пользователем'''
def test_post_add_photo_of_any_pet(pet_photo='images/Pushistick.jpg'):
    _, auth_key = pf.get_api_key(my_email, my_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")  # т.к. 2 значения в ответе, берем 2-список питомцев
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    a = 0
    while len(my_pets['pets'][a]['pet_photo']) != 0:  # пока индекс с фото не равен 0 - смотрим следующий индекс
        a = a + 1
        print(f"Питомец {a} имеет фотографию")
    pet_id = my_pets['pets'][a]['id']  # ключ 'pets' содержит животных,[а] индекс животного, в котором нам нужен ['id']
    status, result = pf.post_add_photo_of_pet(auth_key, pet_id, pet_photo)
    assert status == 200
    assert result['pet_photo'] != 0
    # print('result', result)


'''добавление фото для последнего животного без фото, авторизованным пользователем'''
def test_post_add_photo_of_pet(pet_photo='images\Pushistick.jpg'):
    _, auth_key = pf.get_api_key(my_email, my_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")  # т.к. 2 значения в ответе, берем 2-список питомцев
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    try:
        pet_id = my_pets['pets'][0]['id']  # ключ 'pets' содержит животных,[0] индекс животного, в котором нам нужен ['id']
    except IndexError as e:
        raise Exception("Нет питомцев")
    try:
        status, result = pf.post_add_photo_of_pet(auth_key, pet_id, pet_photo)
        assert status == 200
        assert result['pet_photo'] != 0
    except UnboundLocalError as e:
        print("Нет питомцев")
    # print('result', result)


'''обновление информации для последнего животного, авторизованным пользователем'''
def test_update_pet_info(name='Котяря', animal_type='Кот', age=2):
   _, auth_key = pf.get_api_key(my_email, my_password)
   _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
   if len(my_pets['pets']) > 0:
       status, result = pf.put_update_last_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
       assert status == 200
       assert result['name'] == name
   else:
       raise Exception("Нет питомцев")


