heads = 35  # количество голов
legs = 94  # количество ног

for rabbits in range(heads + 1):  # количество кроликов
    for pheasant in range(heads + 1):  # количество фазанов
        #  если суммарное количество голов превышено или ног превышено, то переходим на следующий шаг цикла
        if (rabbits + pheasant) > heads or \
            (rabbits * 4 + pheasant * 2) > legs: 
            
        else (rabbits + pheasant) == heads and (rabbits * 4 + pheasant * 2) == legs:
            print("Количество кроликов", rabbits)
            print("Количество фазанов", pheasant)
            print("---")
            
