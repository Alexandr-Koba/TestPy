''' 
 Напишите программу, которая считывает три числа и подсчитывает количество чётных чисел.

'''

a, b, c = int(input()), int(input()), int(input())
count = 0
if a % 2 == 0:
    count += 1
if b % 2 == 0:
    count += 1
if c % 2 == 0:
    count += 1

print(f'>>> {count} - колличество четных чисел')