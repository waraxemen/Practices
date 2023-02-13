class Customers:
    def __init__(self, first_name, second_name, city, balance):
        self.first_name = first_name
        self.second_name = second_name
        self.balance = balance
        self.city = city
    def __str__(self):
        return f'{self.first_name} {self.second_name}. {self.city}. Баланс: {self.balance} руб.'
    def no_balance(self): # т.к. выше уже есть функция строкового вывода, можно создать такую функцию
        return f'{self.first_name} {self.second_name}. {self.city}'

customer_1 = Customers('Иван', 'Петров', 'Москва', 50)
customer_2 = Customers('Владимир','Зайцев','Кострома',50)
customer_3 = Customers('Олеся','Янина','Новосибирск',50)
print(customer_1)
print(customer_1.no_balance())
list=[customer_1,customer_2,customer_3]
for _ in list: #Полный список покупателей
    print(_.__str__())

class Lite(Customers): #подкласс без баланса
    def __str__(self):
        return f'{self.first_name} {self.second_name}: {self.city}.'
l_1 = Lite('Виталий', 'Петров', 'Волгоград', 0)
l_2 = Lite('Полина','Иванова','Гомель',0)
l_3 = Lite('Екатерина','Сидорова','Владимир',0)
litelist=[l_1,l_2,l_3]

for _ in litelist: #Полный список покупателей
    print(_.__str__())

Ivanov = Customers('Иван', 'Иванов', 'Пермь', 150)
if __name__ == "__main__":
    print(Ivanov)

Ivanov = ['Иван', 'Иванов', 'Пермь', 150]
Kupystin = ['Пётр', 'Капустин', 'Пермь', 0]
List2 = [Ivanov, Kupystin]

def whichClass(*i):
 for j in i:
  for name in j:
   if name[3]==0:
    name=Lite(name[0],name[1],name[2],name[3])
   else: name=Customers(name[0],name[1],name[2],name[3])
   print(name)

whichClass(List2)