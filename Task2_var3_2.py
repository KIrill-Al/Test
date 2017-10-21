#!/usr/bin/env python3
def is_prime(number):
    for i in range(3,number//2,2):
        if number%i == 0:
            return False
    else:
        return True

number = int(input('Введите число от 0 до 1000: '))
if 0<=number<=1000:
    print(is_prime(number))
else:
    print('Необходимо число от 0 до 1000!')
