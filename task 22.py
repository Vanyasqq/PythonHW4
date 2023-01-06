# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа.
# n - кол-во элементов первого набора.
# m - кол-во элементов второго набора.
# Значения генерируются случайным образом.

# Input: 11 6
# (значения сгенерированы случайным образом
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18)

# Output: 11 6
# 6 12

n = int(input('длинна первого списка: '))
m = int(input('длинна второго списка: '))

import random

ArrayN = []
for i in range(0, n):
    RandomNum = round(random.randint(0,7))
    ArrayN.append(RandomNum)
print(ArrayN)

ArrayM = []
for i in range(0,m):
    RandomNum = round(random.randint(0,7))
    ArrayM.append(RandomNum)
print(ArrayM)

NewArray = []

for i in ArrayN:
    for j in ArrayM:
        if i == j:
            NewArray.append(i)
print(set(NewArray))

