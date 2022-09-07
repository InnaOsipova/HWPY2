#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
#Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
import random

# создание списка
n = int(input('Введите количество элементов :   '))
run = range(-n, n, 2)
numbers = list(run)
print(numbers)

#Запись позиций в файл
number = random.randint(2, n)
f = open('text.txt','w')
for i in range (number):
    index = random.randint(0,n-1)
    f.write(str(index))
    f.write('\n')
f.close()

# умножение элементов, соответсвующих позициям в файле.
multiplicator = 1
with open ("text.txt", "r") as f:
    for i in f :
        print(i)
        multiplicator = multiplicator * numbers[int(i)]
print(f' произведение чисел под заданными в файле номерами  = {multiplicator}')

