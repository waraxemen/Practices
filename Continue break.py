text=[1,2,3,4]
for i in text:
	if i==3:
		print('333')
	print(i)
else: print('end')
print('end2')

#

text=[1,2,3,4]
for i in text:
	if i==3:
		print('333')
		continue
	print(i) # цифра 3 не выведится, т.к. программа перейдёт к следующему значению
else: print('end')
print('end2')

text=[1,2,3,4]
for i in text:
	if i==3:
		print('333')
		break
	print(i) #выведет 1 2 "333" после чего завершит выполнение м выведет 'end2'
else: print('end')
print('end2')