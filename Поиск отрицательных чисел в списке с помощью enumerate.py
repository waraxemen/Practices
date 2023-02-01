list_ = [-5, 2, 4, 8, 12, -7, 5]

index_negative = 0
all_index=[]
negative_numbers=[]
for i, value in enumerate(list_): #value in enumerate(list_)==in range(len(list_))
    if list_[i] < 0:
        print("Отрицательное число: ", value)
        index_negative = i  # перезаписываемое значение индекса
        all_index.append(i)
        negative_numbers.append(value)
        print("Новый индекс отрицательного числа: ", index_negative)
    else:
        print("Положительное число: ", list_[i])
    print("---"*3)

print("Ответ: индекс последнего отрицательного элемента = ", index_negative)
print("Индексы всех отрицательных чисел ", all_index)
print("Все отрицательные числа",negative_numbers )
