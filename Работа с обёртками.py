USERS = ['admin', 'guest', 'director', 'root', 'superstar']

yesno = input("""Введите Y, если хотите авторизоваться или N, 
             если хотите продолжить работу как анонимный пользователь: """)
auth = yesno == "Y"

if auth:
    username = input("Введите ваш username:")

def is_auth(func):
    def wrapper():
        if auth:
            print("Пользователь авторизован")
            func()
        else:
            print("Пользователь неавторизован. Функция выполнена не будет")
    return wrapper

def has_access(func):
    def wrapper():
        if username in USERS:
            print("Авторизован как", username)
            func()
        else:
            print("Доступ пользователю", username, "запрещен")
    return wrapper

@is_auth # указываем 1 вызываемую функцию куда нужно встроить код, но так как есть 2 фнкция, программа переходит к ней
@has_access # выполняется 2 функция и from_db встроится туда где прописано func()
def from_db():
    print("some data from database")
from_db() #запускаем функцию в работу