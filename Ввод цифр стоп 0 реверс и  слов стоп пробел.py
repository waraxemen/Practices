
num=int(input("Введите значение:"))
data=[]
while num !=0:
    data.append(num)
    num=int(input("Введите значение:"))
print (sorted(data,reverse=True))

words=input("Введите слово:")
data=[]
while words!=' ':
    if words not in data:
        data.append(words)
    words = input("Введите слово:")
for a in data:
    print (a, end=",")