''' 
Начало столетия

Напишите программу, которая определяет, оканчивается ли год с данным номером на два нуля. Если год оканчивается, то выведите «YES», иначе выведите «NO».

Формат входных данных
На вход программе подаётся натуральное число.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
'''

age = int(input())
z = age % 10 # Вычисляем последнюю цифру числа.
x = (age % 100) // 10 # Вычисляем вторую цифру с конца (предпоследнюю) 
if z == 0 and x == 0:
    print("YES")
else:
    print("NO")


# Более красивый вариант
'''
age=int(input())
if age%100==0:
    print("YES")
else:
    print("NO")
'''
# С помощью приведения в str и используя срезы [-2::]
n = int(input())

if str(n)[-2::] == '00':
    print('YES')
else:
    print('NO')
