# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X


import random

my_list = []
for i in range(10):
    my_list.append(random.randint(0,10))
print(my_list)

n = int(input('Введите число N: '))
close_numb = abs(n - my_list[0])


for i in range(len(my_list)):
    numb = abs(n - my_list[i])
    if numb <= close_numb:
        close_numb = numb
print (f"Ближайшее число {numb}") 