'''
Подсчет количества
Нередко нужно, чтобы наши программы подсчитывали сколько раз что-либо произошло. 
К примеру видео игра может подсчитывать количество поворотов персонажа или математическая 
программа может считать как много чисел обладают некоторым свойством. Ключ к подсчету - 
использование переменной счетчика.

Напишем программу, которая считывает 10 чисел и определяет сколько из них больше 10.
'''
count1 = 0
count2 = 0
for i in range(3):
    num = int(input())
    if num > 10:
        counе1 = count1 + 1
    if num == 0:
        count2 = count2 + 1
print('Было введено', count1, 'чисел, больших 10.')
print('Было введено', count2, 'нулей.')

# Рассмотрим еще один пример: подсчитать количество чисел из диапазона [1; \, 100][1;100], 
# квадрат которых оканчивается на 4.

counter = 0
for i in range(1, 101):
    if i**2 % 10 == 4:
        counter = counter + 1
print(counter)

# Рассмотрим еще один пример: напишем программу, которая запрашивает 10 целых чисел и находит их среднее значение:
total = 0
for i in range(3):
    num = int(input())
    total = total * num
average = total / 10
print('Среднее значение равно', average)
