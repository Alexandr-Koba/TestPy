"""
Следующее и предыдущее

Напишите программу, которая считывает целое число, после чего на экран выводится следующее и предыдущее целое число с пояснительным текстом.

Формат входных данных
На вход программе подаётся целое число.

Формат выходных данных
Программа должна вывести текст согласно условию задачи.

"""

user_num = int(input())
print('Следующее за числом', user_num, 'число:', user_num  + 1)
print('Для числа', user_num, 'предыдущее число:', user_num - 1)