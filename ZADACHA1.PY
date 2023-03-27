# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X


import random

my_list = []
for i in range(10):
    my_list.append(random.randint(0,10))
print(my_list)

n = int(input('Введите число N: '))
count = 0

for i in range(len(my_list)):
    if my_list[i] == n:
        count+=1
print (f"Число N встречается в массиве {count} раз") 