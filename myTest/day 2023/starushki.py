'''
Два автомобиля 

Два автомобиля едут навстречу друг другу с постоянными скоростями V_1V1​ и V_2V2​ км/ч. Определите, через какое время автомобили встретятся, если расстояние между ними равно SS км.

Формат входных данных
На вход программе подаются три числа с плавающей точкой S, \, V_1, \, V_2S,V1​,V2​, каждое на отдельной строке.

Формат выходных данных 
Программа должна вывести одно число в соответствии с условием задачи.
'''


distance = float(input())
car1 = float(input())
car2 = float(input())
print(distance / (car1 + car2))