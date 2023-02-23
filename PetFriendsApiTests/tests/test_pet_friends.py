from api import PetFriends
from settings import my_email, my_password, key
import os  # для запуска с консоли необходимо полный путь до фото указывать
pf = PetFriends()


def test_get_api_key_for_valid_user(email=my_email, password=my_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result
    print(result)


def test_get_all_pets_with_valid_key(filter: str = ''):
    _, auth_key = pf.get_api_key(my_email, my_password)  # т.к. нам выдают email, password, то использовали _ для мыла
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0  # убеждаемся что в ответе по ключу pets есть данные о животных


def test_get_my_pets_with_valid_key(filter: str = 'my_pets'):
    _, auth_key = pf.get_api_key(my_email, my_password)  # т.к. нам выдают email, password, то использовали _ для мыла
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0  # убеждаемся что в ответе по ключу pets есть данные о животных
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

def test_delete_new_pet():
    _, auth_key = pf.get_api_key(my_email, my_password)
    _, my_pets= pf.get_list_of_pets(auth_key, filter= "my_pets")  # т.к. 2 значения в ответе, берем 2-список питомцев
    pet_id = my_pets ['pets'][0]['id']  # ключ 'pets' содержит 1 значение -[0] список ключей, в котором нам нужен ['id']
    print("удаляемый питомец", pet_id)
    status, result = pf.delete_new_pet(auth_key, pet_id)
    assert status == 200
    print('result',result)







def test_successful_delete_self_pet():  # (Чужая версия)
    # Получаем ключ auth_key и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key(my_email, my_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    # Проверяем - если список своих питомцев пустой, то добавляем нового и опять запрашиваем список своих питомцев
    if len(my_pets['pets']) == 0:
        pf.post_add_new_pet_with_photo(auth_key, "Суперкот", "кот", "3", "images/Pushistick.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
        print('Список был пустой')
    # Берём id первого питомца из списка и отправляем запрос на удаление
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_new_pet(auth_key, pet_id)
    # Ещё раз запрашиваем список своих питомцев
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    # Проверяем что статус ответа равен 200 и в списке питомцев нет id удалённого питомца
    assert status == 200
    assert pet_id not in my_pets.values()





def test_successful_update_self_pet_info(self, name='Мурзик', animal_type='Котэ', age=5):
   _, auth_key = self.pf.get_api_key(my_email, my_password)
   _, my_pets = self.pf.get_list_of_pets(auth_key, "my_pets")

   if len(my_pets['pets']) > 0:
       status, result = self.pf.update_pet_info(auth_key, my_pets['pets'][0]['id'],
                                                name, animal_type, age)
       assert status == 200
       assert result['name'] == name
   else:
       raise Exception("There is no my pets")


