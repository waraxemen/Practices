from rectangle import Rectangle# копируем из текущей папки из файла rectangle класс Rectangle
from rectangle import Square, Circle # or from rectangle import Rectangle, Square

r1 = Rectangle(10,5)#переменная содержит значения для класса
print("width=",r1.width,"height=",r1.getHeight(), 'Area=',r1.getArea())#запрос как к переданному содержанию так и к функции

s1=Square(6)
print("Площадь квадрата : ",s1.get_area_square())

c1=Circle(3)
print("Площадь круга : ",c1.areaCircle())

#создаём коллекцию
figures=[r1,s1,c1]

for _ in figures:
    if isinstance(_,Rectangle): # isinstance - принадлежность переменной из списка к классу Rectangle.
        print(_.getArea())# фунция прямоугольника
    elif isinstance(_,Circle): print(_.areaCircle())
    else: print(_.get_area_square())# логично если не прямоугольник, то квадрат

#Создайте метод, который возвращает атрибуты прямоугольника как строку Rectangle : 5, 10
# (метод __str__ - как аргумент метод ожидает только экземпляр и должен возвращать строку)
def __str__(self):
    print (f"Rectangle : {self.height} {self.width}")
__str__(r1)