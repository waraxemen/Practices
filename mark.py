@pytest.mark.skip(reason="Баг в продукте - <ссылка>")  # помечает тест как пропущенный, при запуске тест не будет выполняться
def test_one():  # Это наш тест, который находит тот самый баг


@pytest.mark.skipif(sys.version_info < (3, 6), reason="Тест требует python версии 3.6 или выше")  # пропуск если
def test_python36_and_greater():
# Можно использовать её в тестах в виде декоратора:
minversion = pytest.mark.skipif(sys.version_info < (3, 6), reason="Тест требует python версии 3.6 или выше")
@minversion
def test_python36_and_greater():


@pytest.mark.xfail(sys.platform == "win32",reason="Ошибка в системной библиотеке")  # На платформе Windows ожидаем, что тест будет падать
    def test_not_for_windows(): # нестабильный, если тест прошел успешно- пометится XPASS. При неудачном прохождении теста статус будет XFAILED
# Например, следующий тест будет помечен xfail только в том случае, если произойдет исключение типа RuntimeException,
# в противном случае тест будет выполняться как обычно (помечаться passed, если пройдет успешно, и failed, если пройдет неуспешно):
@pytest.mark.xfail(raises=RuntimeError)
def test_x_status_runtime_only():


                                            """Пользовательские группы"""
# необходимо в проекте создать файл pytest.ini, туда внести информацию об описанных в тестах группах.
# Например. У нас есть четыре теста, два из них на аутентификацию пользователя, остальные два — это тесты мероприятий.
# В каждой такой группе соответственно API и UI тесты:
@pytest.mark.api
@pytest.mark.auth
def test_auth_api():
   pass

@pytest.mark.ui
@pytest.mark.auth
def test_auth_ui():
   pass

@pytest.mark.api
@pytest.mark.event
def test_event_api():
   pass

@pytest.mark.ui
@pytest.mark.event
def test_event_ui():
   pass
# В корне проекта создадим файл pytest.ini и добавим туда описание наших категорий.
# Тесты будут запускаться и без этого файла, но его наличие избавит нас от постоянных предупреждений в отчетах:
[pytest]
markers =
   api: тесты API
   ui: тесты UI
   event: тесты мероприятий
   auth: тесты авторизации
# Например, если нам нужно запустить только API тесты, то в консоли надо набрать:
pytest test.py -v -m "api" # test.py замените на имя своего файла в проекте
# если мы хотим запустить только UI тесты авторизации:
pytest test.py -v -m "ui and auth"
# тесты на модули авторизации и мероприятий:
pytest test.py -v -m "auth or event"
# Опцию -k командной строки можно использовать, чтобы указать подстроку, которая должна присутствовать в именах тестов
# (при использовании опции -m проверяется точное совпадение). Это облегчает отбор тестов по именам.
pytest test.py -v -k name
# Можно назначить список маркеров классу:
class TestClass:
    pytestmark = [pytest.mark.webtest, pytest.mark.slowtest]
#Можно также установить пометку на уровне модуля:
import pytest pytestmark = pytest.mark.webtest
# равно как и список маркеров:
pytestmark = [pytest.mark.webtest, pytest.mark.slowtest]
# В этом случае маркеры будут применяться (слева направо) ко всем функциям и методам модуля.


Получение списка маркеров с помощью pytest --markers в командной строке