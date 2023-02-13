class MyException(Exception):  # создаём пустой класс – исключения
    pass
try:
    raise MyException("message")  # поднимаем наше исключение
except MyException as e:  # ловим его за хвост как шкодливого котёнка
    print(e)  # выводим информацию об исключении