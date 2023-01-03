'''
Площадь и длина
Напишите программу определяющую площадь круга и длину окружности по заданному радиусу RR.

Формат входных данных
На вход программе подается одно вещественное число RR​.

Формат выходных данных
Программа должна вывести два числа – площадь круга и длину окружности радиуса RR.



Примечание. Используйте константу math.pi. 
'''

R = float(input())
from math import pi # импорт math и дал ей псевдоним pi 
print(pi*R**2)      # площадь круга
print(2*pi*R)       # длина окружности