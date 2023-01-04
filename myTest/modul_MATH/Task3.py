'''
Средние значения

В математике выделяют следующие средние значения:

среднее арифметическое чисел aa и bb: \dfrac{a+b}{2}2a+b​;
среднее геометрическое чисел aa и bb: \sqrt{a\cdot b}a⋅b​;
среднее гармоническое чисел aa и bb: \dfrac{2ab}{a+b}a+b2ab​;
среднее квадратичное чисел aa и bb: \sqrt{\dfrac{a^2+b^2}{2}}2a2+b2​​.

Формат входных данных
На вход программе подается два вещественных числа aa и bb​, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести 4 числа – среднее арифметическое, геометрическое, гармоническое и квадратичное
'''

import math
a, b  = float(input()), float(input())
sab, pab = a + b, a * b
print(sab / 2)                         # Среднее арифметическое
print(math.sqrt(pab))                  # Среднее геометрическое
print(2 * pab / sab)                   # Среднее гармоническое
print(math.sqrt((a**2 + b**2) / 2))    # Среднее квадратичное