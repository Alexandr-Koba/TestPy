"""
Наименьшее из двух чисел
Напишите программу, которая определяет наименьшее из двух чисел.

Формат входных данных
На вход программе подаётся два различных целых числа.

Формат выходных данных
Программа должна вывести наименьшее из двух чисел.

"""

x, y = int(input()), int(input())
if x > y:
    print(y)
else:
    print(x)

# Супер в одну строчку. (я до этого еще не дошел)
print(min(int(input()), int(input())))