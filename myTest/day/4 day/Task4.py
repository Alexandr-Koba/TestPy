"""
Программа принимает 3 числа.
Проверяет на НЕ РАВЕНСТВО.
если а не равно b, а b не равно с.
то  числа не равны.
"""

a, b, c = int(input()), int(input()), int(input())

if a != b != c:
    print('числа не равны')
else:
    print('числа равны')