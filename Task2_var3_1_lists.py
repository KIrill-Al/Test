#!/usr/bin/env python3
'''Программа получает на вход невозрастающую последовательность натуральных чисел. После этого вводится число X. Все числа во входных данных натуральные и не превышают 200.
Выведите индекс, где окажется число Х. Если в списке есть элемент с таким значением, то число Х помещается после него.'''
import random
numbers = [i for i in range(30,0,random.randint(0,5)-4)]#генерируем невозрастающую посл-ть
print ('Исходный список: ', numbers)
x = int(input('Введите новое число: '))
for i, number in enumerate(numbers,0):
    if number<x:
        numbers.insert(i,x)
        print ('Новый список: ', numbers)
        print('Индекс числа в списке: ', i)
        break
else:
    numbers.append(x)
    print ('Новый список: ', numbers)
    print('Индекс числа в списке: ', len(numbers) - 1)
