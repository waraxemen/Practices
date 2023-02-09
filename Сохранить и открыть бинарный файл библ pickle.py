import pickle
f='bin.dat'
data=[1,2,3,15,'some text',1.5]
with open(f,'wb') as file:
    pickle.dump(data,file) #запись массива или текста из data

open(f,'ab')# дозапись в конец
for i in range(4):
    num=(int(input("Введите текст")))
    with open(f,'ab') as file:
        pickle.dump(num, file)
print(len(f))
result=[]
with open(f,'rb') as file:
    for i in range(5): #1 data и 4 введённых цифры
        result.append(pickle.load(file))
print(result)