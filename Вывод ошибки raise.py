age = int(input("How old are you?"))
 
if age > 100 or age <= 0:
    raise ValueError("Тебе не может быть столько лет")
 
print(f"Тебе {age} лет!") # Возраст выводится только в случае, если пользователь ввёл правильный возраст.

...........................

try:
    age = int(input("How old are you?"))
    if age > 100 or age <= 0:
        raise ValueError("Тебе не может быть столько лет")
except ValueError as error: #исключаем остановку программы
    print(error)
    print("Неправильный возраст")
else:
    print(f"You are {age} years old!") # Возраст выводится только в случае, если пользователь ввёл правильный возраст.
