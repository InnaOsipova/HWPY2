#Реализуйте алгоритм перемешивания списка.

import string

def mixing(l, num, lk):
    import random
    if num == 1:
        lk.append(l[num])
        lk.append(l[num-1])
        return 
    else:
        index = random.randint(0,num-1)
        l[index], l[num] = l[num], l[index]
        lk.append(l[num])
        mixing (l, num-1, lk)
    return lk

initial_list = [1, 2, 3, 4, 5, 6, 7, 8]
n = len(initial_list)
lk = []
print (mixing (initial_list, n-1, lk))