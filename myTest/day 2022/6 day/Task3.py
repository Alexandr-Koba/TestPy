'''
Красивое число 🌶️
Назовем число красивым, если оно является четырехзначным 
и делится нацело на 7 или на 17. Напишите программу, определяющую, 
является ли введённое число красивым. Программа должна вывести «YES», 
если число является красивым, или «NO» в противном случае.
'''

x = int(input())
if (x % 7 == 0 or x % 17 == 0) and (x >= 1000 and x <= 9999):
    print('YES')
else:
    print('NO')