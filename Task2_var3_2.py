#!/usr/bin/env python3
'''Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000, и возвращающую True, если оно простое, и False - иначе.'''
def is_prime(n, div=3):
    if (n%2 == 0) or (n%div==0) or (n == 1) or (n == 0):
        return False
    elif div>=n//2:
        return True
    else:
        return is_prime(n, div+2)

n = int(input('Введите число от 0 до 1000: '))
if 0<=n<=1000:
    print(is_prime(n))
else:
    print('Необходимо число от 0 до 1000!')
