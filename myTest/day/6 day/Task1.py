"""
Принадлежность

Напишите программу, которая принимает целое число xx и определяет, 
принадлежит ли данное число указанным промежуткам.
"""

n = int(input())
if not (-3 < n < 7):
    print('Принадлежит')
else:
    print('Не принадлежит') 