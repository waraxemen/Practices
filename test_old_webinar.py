import pytest
import requests
import functools

def log_request(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        with open('log.txt', 'a') as f:
            f.write(f'{args[1]} {args[2]}\n')
            f.write(f'request headers: {args[0].headers}\n')
            response = func(*args, **kwargs)
            f.write(f'request body: {response.request.body}\n')
            f.write(f'response status code: {response.status_code}\n')
            f.write(f'response headers: {response.headers}\n')
            f.write(f'response body: {response.text}\n\n')
            return response
    return wrapper

@log_request
def api_request(session, method, url, headers_update='', data='', json=''):
    if headers_update is not None:
        session.headers.update(headers_update)
    if method == 'get':
        response = session.get(url, data=data, json=json)
    if method == 'post':
        response = session.post(url, data=data, json=json)
    if method == 'put':
        response = session.put(url, data=data, json=json)
    if method == 'delete':
        response = session.delete(url, data=data, json=json)
    else: response = ''
    return response

BASE_URL = 'https://petfriends.skillfactory.ru/api'
user = 'api@api'
password = 'api@api'

@pytest.fixture(scope='session')
def api_client():
    session = requests.Session()
    response = api_request(session, 'GET', f'{BASE_URL}/key',
                           headers_update={'email': user, 'password' : password})
    access_token = response.json().get('key')
    assert access_token is not None

    session.headers.update({"auth_key" : access_token, "accept" : "application/json"})
    yield session
    api_request(session, "GET", f'{BASE_URL}/logout')

@pytest.fixture(scope='session')
def create_pet(api_client):
    pet = {
        'name' : 'test_pet',
        'age' : 1,
        'animal_type' : 'cat'}
    response = api_request(api_client, 'post', f'{BASE_URL}/create_pet_simple', json=pet)
    pet_id = response.json()['id']  # get
    assert pet_id is not None
    yield pet_id
    api_request(api_client, 'delete', f'{BASE_URL}/delete_pet/{pet_id}')

def test_get_pets(api_client):
    response = api_request(api_client, 'get', f'{BASE_URL}/pets')
    assert response.status_code == 200
    assert response.json().get('pets') is not None



# def test_create_pet(api_client, create_pet):



