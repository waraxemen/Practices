per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money=int(input("Введите сумму, которую планируете положить под проценты: "))
dict_values=list(per_cent.values())
pre_deposit=list(map(lambda num: num*money/100,dict_values))
deposit=[int(x) for x in pre_deposit] 
print ("Максимальная сумма, которую вы можете заработать —", max(deposit))
