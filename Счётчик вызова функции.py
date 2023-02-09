def counter(func):
   count = 0
   def wrapper(*args, **kwargs):
       nonlocal count
       func(*args, **kwargs)
       count += 1
       print(f"Функция {func} была вызвана {count} раз")
   return wrapper

@counter
def say_word(word):
   print(word)

say_word("Oo!!!")
say_word("Oo!!!")