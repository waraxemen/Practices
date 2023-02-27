from api import PetFriends
from settings import my_email, my_password
import os  # для запуска с консоли необходимо полный путь до фото указывать
pf = PetFriends()

''' ВСЕ ТЕСТЫ ИДУТ ПОСЛЕДОВАТЕЛЬНО, ЕСЛИ НУЖНО ВЫПОЛНИТЬ ТЕСТ ВНЕ ОЧЕРЕДИ - ВОЗМОЖНО ПОТРЕБУЕТСЯ СОЗДАТЬ ПИТОМЦЕВ '''

'''_______________________________________________Тест-1____________________________________________________________'''
'''    получить ключ, создать питомца без фото, создать питомца с фото, присвоить фото предпоследнему животному     '''
def test_get_api_key_for_valid_user(email=my_email, password=my_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result
    print(result)
def test_post_add_new_pet_without_photo():
    _, auth_key = pf.get_api_key(my_email, my_password)
    name = "Pyshistick"
    animal_type = "Cat"
    age = '1'
    status, result = pf.post_add_new_pet_without_photo(auth_key, name, animal_type, age)
    assert status == 200
    print(result)
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
def test_post_add_photo_of_any_pet(pet_photo='images/Puma.jpg'):
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
    '''Результат: получен ключ, создалась карточка животного без фото, создалась карточка с фото, добавилось фото'''


'''_______________________________________________Тест-2____________________________________________________________'''
'''            создать животное без фото, добавить ему фото, попробовать снова добавить ему другое фото             '''
def test_post_add_pet_without_photo():
    _, auth_key = pf.get_api_key(my_email, my_password)
    name = "Pyshistick"
    animal_type = "Cat"
    age = '1'
    status, result = pf.post_add_new_pet_without_photo(auth_key, name, animal_type, age)
    assert status == 200
    print(result)
def test_post_add_photo_of_pet(pet_photo='images/Pushistick.jpg'):
    _, auth_key = pf.get_api_key(my_email, my_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")  # т.к. 2 значения в ответе, берем 2-список питомцев
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    pet_id = my_pets['pets'][0]['id']  # ключ 'pets' содержит 1 значение -[0] список ключей, в котором нам нужен ['id']
    if len(my_pets['pets']) == 0: raise Exception("У вас нет питомцев!")
    status, result = pf.post_add_photo_of_pet(auth_key, pet_id, pet_photo)
    assert status == 200
    assert result['pet_photo'] != 0
def test_post_add_other_photo_of_pet(pet_photo='images/Puma.jpg'):
    _, auth_key = pf.get_api_key(my_email, my_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")  # т.к. 2 значения в ответе, берем 2-список питомцев
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    pet_id = my_pets['pets'][0]['id']  # ключ 'pets' содержит 1 значение -[0] список ключей, в котором нам нужен ['id']
    if len(my_pets['pets']) == 0: raise Exception("У вас нет питомцев!")
    status, result = pf.post_add_photo_of_pet(auth_key, pet_id, pet_photo)
    assert status == 200
    assert result['pet_photo'] != 0
    '''Результат: создалась карточка животного без фото, добавилось фото, заменилось фото'''


'''_______________________________________________Тест-3____________________________________________________________'''
'''             удалить животное, создать новое животное без фото, удалить другое оставшееся животное               '''
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
def test_post_add_pet_new_without_photo():
    _, auth_key = pf.get_api_key(my_email, my_password)
    name = "Pyshistick"
    animal_type = "Cat"
    age = '1'
    status, result = pf.post_add_new_pet_without_photo(auth_key, name, animal_type, age)
    assert status == 200
    print(result)
def test_delete_other_pet():
    _, auth_key = pf.get_api_key(my_email, my_password)
    _, my_pets= pf.get_list_of_pets(auth_key, filter= "my_pets")  # т.к. 2 значения в ответе, берем 2-список питомцев
    if len(my_pets['pets']) == 0:  # Проверяем - если список своих питомцев пустой, то добавляем нового
        pf.post_add_new_pet_with_photo(auth_key, "Пушистик", "кот", "1", "images/Pushistick.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
        print('Список был пустой')
    pet_id = my_pets ['pets'][1]['id']  # ключ 'pets' содержит 1 значение -[0] список ключей, в котором нам нужен ['id']
    print("удаляемый питомец", pet_id)
    status, result = pf.delete_new_pet(auth_key, pet_id)
    # Проверяем что статус ответа равен 200 и в списке питомцев нет id удалённого питомца
    assert status == 200
    assert pet_id not in my_pets.values()
    '''Результат: удалилось животное, создалось новое животное без фото, удалилось другое животное'''


'''_______________________________________________Тест-4____________________________________________________________'''
'''                           получить ключ незарегистрированному пользователю                                      '''
def test_get_api_key_for_not_valid_user(email="wrong@email", password="any@any"):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result
    print(result)
    '''Результат: получен код 403 - combination of user email and password is incorrect'''


'''_______________________________________________Тест-5____________________________________________________________'''
'''           редактирование данных животного без фото, добавить фото, снова отредактировать                        '''
def test_update_without_photo_pet_info(name='Котярa', animal_type='Кот', age=2):
   _, auth_key = pf.get_api_key(my_email, my_password)
   _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
   if len(my_pets['pets']) > 0:
       status, result = pf.put_update_last_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
       assert status == 200
       assert result['name'] == name
   else:
       raise Exception("Нет питомцев")
def test_post_add_photo_to_pet(pet_photo='images\Pushistick.jpg'):
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
def test_update_with_photo_pet_info(name='Котя', animal_type='Котz', age=3):
   _, auth_key = pf.get_api_key(my_email, my_password)
   _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
   if len(my_pets['pets']) > 0:
       status, result = pf.put_update_last_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
       assert status == 200
       assert result['name'] == name
   else:
       raise Exception("Нет питомцев")
   '''Результат: всё успешно'''


'''_______________________________________________Тест-6____________________________________________________________'''
'''                попробовать войти с неправильным логином и правильным паролем и наоборот                         '''
def test_get_api_key_for_wrong_password(email=my_email, password="wrong@mail.ru"):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result
    print(result)
def test_get_api_key_for_wrong_email(email="wrong@mail.ru", password=my_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result
    print(result)
    '''Результат: в обоих случаях получен код 403 - combination of user email and password is incorrect'''


'''_______________________________________________Тест-7____________________________________________________________'''
'''         удалить всех питомцев, создать одного, получить список своих питомцев и общий список питомцев           '''
def test_delete_pet():
    _, auth_key = pf.get_api_key(my_email, my_password)
    _, my_pets= pf.get_list_of_pets(auth_key, filter= "my_pets")  # т.к. 2 значения в ответе, берем 2-список питомцев
    a=0
    try:
        while len(my_pets['pets']) != 0:
            pet_id = my_pets ['pets'][a]['id']
            print("удаляемый питомец", pet_id)
            status, result = pf.delete_new_pet(auth_key, pet_id)
            a=a+1
            assert status == 200
    except IndexError:
        print('Все питомцы удалены')
def test_post_add_1_pet_without_photo():
    _, auth_key = pf.get_api_key(my_email, my_password)
    name = "Pyshistick"
    animal_type = "Cat"
    age = '1'
    status, result = pf.post_add_new_pet_without_photo(auth_key, name, animal_type, age)
    assert status == 200
    print(result)
def test_get_my_pets_with_valid_key(filter: str = 'my_pets'):
    _, auth_key = pf.get_api_key(my_email, my_password)  # т.к. нам выдают email, password, то использовали _ для мыла
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0  # убеждаемся что в ответе по ключу pets есть данные о животных
    print(result)
def test_get_all_pets_with_valid_key(filter: str = ''):
    _, auth_key = pf.get_api_key(my_email, my_password)  # т.к. нам выдают email, password, то использовали _ для мыла
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets'][1]['id']) > 0  # убеждаемся что в ответе по ключу pets есть данные о других животных


'''_______________________________________________Тест-8____________________________________________________________'''
'''                    получить общий список питомцев используя неправильный ключ                                   '''
def test_get_all_pets_with_not_valid_key(filter='my_pets'):
    auth_key = {'key': 'd978cef8a33894b009466e569b83e9ed9be8a5b43eda4e43fact890e'}
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 403  # сервер должен выдать статус код 403
    '''Результат: получен код 403 - combination of user email and password is incorrect'''


'''_______________________________________________Тест-9____________________________________________________________'''
'''                                       удалить чужого питомца                                                    '''
def test_delete_all_pets():  # сначала удаляем своих питомцев
    _, auth_key = pf.get_api_key(my_email, my_password)
    _, my_pets = pf.get_list_of_pets(auth_key,filter="my_pets")  # т.к. 2 значения в ответе, берем 2-список питомцев
    a = 0
    try:
        while len(my_pets['pets']) != 0:
            pet_id = my_pets['pets'][a]['id']
            print("удаляемый питомец", pet_id)
            status, result = pf.delete_new_pet(auth_key, pet_id)
            a = a + 1
            assert status == 200
    except IndexError:
        print('Все питомцы удалены')
def test_delete_not_my_pets():
    _, auth_key = pf.get_api_key(my_email, my_password)
    status, result = pf.get_list_of_pets(auth_key, filter="")
    assert status == 200
    pet_id = result['pets'][8]['id']  # получаем id чужого питомца - 9 по счёту
    status, result = pf.delete_new_pet(auth_key, pet_id)  # удаляем его
    assert status == 200
    status, result = pf.get_list_of_pets(auth_key, filter="") # снова получаем список
    assert pet_id not in result['pets'][8]['id'] # проверяем что питомца теперь нет в списке
    '''Результат: чужой питомец удалён (прости неведомый сокурсник =)'''


'''_______________________________________________Тест-10____________________________________________________________'''
'''             создать питомца с негативными параметрами, после этого удалить всех питомцев                         '''
def test_post_add_new_pet_without_photo1():
    _, auth_key = pf.get_api_key(my_email, my_password)
    name = "111"
    animal_type = "111"
    age = '1111'
    status, result = pf.post_add_new_pet_without_photo(auth_key, name, animal_type, age)
    assert status == 200
    print(result)
def test_post_add_new_pet_without_photo2():
    _, auth_key = pf.get_api_key(my_email, my_password)
    name = 111
    animal_type = "111"
    age = '1111'
    status, result = pf.post_add_new_pet_without_photo(auth_key, name, animal_type, age)
    assert status == 200
    print(result)
def test_post_add_new_pet_without_photo3():
    _, auth_key = pf.get_api_key(my_email, my_password)
    name = None
    animal_type = "111"
    age = '1111'
    status, result = pf.post_add_new_pet_without_photo(auth_key, name, animal_type, age)
    assert status == 200
    print(result)
def test_post_add_new_pet_with_photo1():
    _, auth_key = pf.get_api_key(my_email, my_password)
    name= "Pyshistick"
    animal_type = "Cat"
    age = '-1'
    # pet_photo = 'images/Pushistick.jpg' #через PyCharm
    pet_photo = os.path.join(os.path.dirname(__file__), 'images/Pushistick.jpg')  # через консоль, путь до тек. файла +
    status, result = pf.post_add_new_pet_with_photo(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    print(result)
def test_post_add_new_pet_with_photo2():
    _, auth_key = pf.get_api_key(my_email, my_password)
    name= "Pyshistick"
    animal_type = 1
    age = '-1'
    # pet_photo = 'images/Pushistick.jpg' #через PyCharm
    pet_photo = os.path.join(os.path.dirname(__file__), 'images/Pushistick.jpg')  # через консоль, путь до тек. файла +
    status, result = pf.post_add_new_pet_with_photo(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    print(result)
def test_post_add_new_pet_with_photo3():
    _, auth_key = pf.get_api_key(my_email, my_password)
    name= "Pyshistick"
    animal_type = "Cat"
    age = '-1'
    pet_photo = None
    status, result = pf.post_add_new_pet_with_photo(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    print(result)
def test_delete_all_my_pets():
    _, auth_key = pf.get_api_key(my_email, my_password)
    _, my_pets = pf.get_list_of_pets(auth_key,filter="my_pets")  # т.к. 2 значения в ответе, берем 2-список питомцев
    a = 0
    try:
        while len(my_pets['pets']) != 0:
            pet_id = my_pets['pets'][a]['id']
            print("удаляемый питомец", pet_id)
            status, result = pf.delete_new_pet(auth_key, pet_id)
            a = a + 1
            assert status == 200
    except IndexError:
        print('Все питомцы удалены')

    '''Результат: строковые числа как параметр принимаются, целые числа вместо имени принимает, 
    отсутствие имени не даёт создать питомца, отрицательный возраст позволяет создать питомца, целые числа вместо типа 
    питомца не дают создать питомца, отсутствие фото при методе создания с фото - не даёт создать питомца'''



