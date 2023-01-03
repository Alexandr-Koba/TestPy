'''
Сортировка трёх 🌶️
Напишите программу, которая упорядочивает три числа от большего к меньшему.

Формат входных данных
На вход программе подается три целых числа, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести три числа, каждое на отдельной строке, упорядоченных от большего к меньшему.
'''

a, b, c = int(input()), int(input()), int(input())
print(max(a, b, c))
print(a + b + c - min(a, b, c) - max(a, b, c))
print(min(a, b, c))


# 2-худший вариант
''' 
a, b, c = int(input()), int(input()), int(input())
minimum = min(a, b, c)
maximum = max(a, b, c)
if minimum < a < maximum:
    print(maximum, a, minimum, sep='\n')
elif minimum < b < maximum:
    print(maximum, b, minimum, sep='\n')
elif minimum < c < maximum:
    print(maximum, c, minimum, sep='\n')
elif a == maximum or b == maximum or c == maximum:
    print(maximum, maximum, minimum, sep='\n')
'''