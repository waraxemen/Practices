import os

print(os.getcwd()) #выдаёт текущий путь

os.chdir(r'C:\Users\Администратор\Desktop')#меняет текущую папку на указанную
print(os.getcwd())

os.mkdir('Удалить') #Создание папки
print('Удалить' in os.listdir())#True

os.rename('Удалить','Удалить папку')

path=r'C:\Users\Администратор\Desktop'
path=os.path.join(path,'Удалить папку') #метод добавления папки к пути
print(path)

name=os.path.join(path,'NewFile.txt')#инструкция по созданию файла
f=open(name,'w')# создание пустого и открытие файла для записи
f.write('some text to writing')
f.close()
print(os.listdir(path))#показывает что внутри папки

os.rename(r'C:\Users\Администратор\Desktop\Удалить папку\NewFile.txt',
          r'C:\Users\Администратор\Desktop\Удалить папку\NewFile2.txt')#обязательно указывать путь или переименует и
# переместит в текущую папку, если имя не менять - просто переместит файл
# os.rename(name, os.path.join(path,'Архив','NewFile3.txt')) тоже вариант перемещения с переименованием только замороченный
for a,b,c in os.walk(r'C:\Users\Администратор\Desktop'):
    print(a)#все возможные папки
    print(b)#нагляднее показывает папки в папках вместе с print(a)
    print(c)#все файлы в каких папках вместе с print(a)