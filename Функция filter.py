numbers = [-10,-7,-1,0,1, 2, 4, 5, 7, 8, 10, 11,None,True,False,'','f']

filtered_numbers=filter(None, numbers)# Если первое значение поставить None, то останутся только True значения
print(list(filtered_numbers))
#[-10, -7, -1, 1, 2, 4, 5, 7, 8, 10, 11, True, 'f']

filtered_numbers2=filter(lambda x: x, numbers) # тоже True
print(list(filtered_numbers2))
#[-10, -7, -1, 1, 2, 4, 5, 7, 8, 10, 11, True, 'f']

filtered_numbers3=filter(lambda x:  type(x) is int, numbers) # отсеивание не целочисленных значений
print(list(filtered_numbers3))
#[-10, -7, -1, 0, 1, 2, 4, 5, 7, 8, 10, 11]

filtered_numbers3=filter(lambda x: type(x) is int and x>=0, numbers) # отсеивание не целочисленных и - значений
print(list(filtered_numbers3))
#[0,1, 2, 4, 5, 7, 8, 10, 11]

# Первое значение - любая функция возвращающая условия для True и в соответствии с ним отсеиваются элементы
# Второе - список