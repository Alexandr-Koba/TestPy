'''
Примечания
Примечание 1. Функция range() может принимать от одного до трех параметров: range(n), range(n, m), range(n, m, k)

первый параметр – это старт последовательности (включительно);
второй параметр – это стоп последовательности (не включительно);
третий параметр – это величина шага.
Примечание 2. Функция range() может генерировать только целые числа, включая отрицательные.

Примечание 3. Величина шага не может равняться нулю. Следующий код:

for i in range(1, 10, 0):
    print(i)
приведет к ошибке ValueError: range() arg 3 must not be zero.

'''

for i in range(5):
    print(i + 1)

print("NEXT:")

for j in range(5, 0, -1):
    print(j)

print("NEXT:")

name = input('Введите текст для подсчета символов: ')
for k in name:
    count = 0
    print(k, end=' ')
    count =+ 1
    print(count)


