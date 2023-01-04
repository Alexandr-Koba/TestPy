# Напишем программу, которая отсчитывает от 5 до 1, а затем выводит текст Взлетаем!!!:
for i in range(1, 6):
    print(i, end=' ')
    print('Старт')

# Отрицательная нумерация
for j in range(5, 0, -1):
    print(j, end = ' ')
    print('start')


# Подщет
count = int(input())
name = input()
for k in range(count, 0, -1):
    print(k, end=' ')
    print(name)