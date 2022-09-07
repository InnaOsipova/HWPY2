#Реализуйте алгоритм перемешивания списка.


import string


def mixing(l, num, lk):
    import random
    import copy
    l1 = copy.deepcopy(l)
    if num == 1:
        lk.append(l1[num])
        lk.append(l1[num-1])
        return 
    else:
        index = random.randint(0,num-1)
        l1[index], l1[num] = l1[num], l1[index]
        lk.append(l1[num])
        mixing (l1, num-1, lk)
    return lk

initial_list = [1, 2, 3, 4, 5, 6, 7, 8]
n = len(initial_list)
lk = []
print (mixing (initial_list, n-1, lk))