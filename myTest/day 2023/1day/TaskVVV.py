'''
Интересное число
Назовем число интересным, если в нем разность максимальной и минимальной цифры равняется средней по величине цифре.
 Напишите программу, которая определяет интересное число или нет. Если число интересное, 
 следует вывести – «Число интересное» иначе «Число неинтересное».

Формат входных данных
На вход программе подается целое трехзначное число.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
'''

x = int(input())
a = x % 10
b = x // 10 % 10
c = x // 100
if a + b + c == 2 * max(a, b, c):
    print("Число интересное")
else:
    print("Число неинтересное")


# Про вариант
a = list(input())
a.sort()
print("Число интересное" if int(a[0]) - int(a[2]) == int(a[1]) or int(a[2]) - int(a[0]) == int(a[1]) else "Число неинтересное")