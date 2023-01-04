for i in range(1, 4):
    print(i)

for y in range(4):
    print('Привет babakoba')


num = input()
count = 0
for a in num:
    print(f"{count}, {a}")
    count += 1
print(f"Всего букв {count}")


# Квадрат

for i in range(5):
    num = int(input())
    print('Квадрат вашего числа равен:', num * num)
print('Цикл завершен')

# Task 1
for i in range(10):
    print('Python is awesome!')

# Подщет через переменную цикла
for i in range(10):
    print(i, '-- Привет')

# Если мы хотим начать с 1 а не с 0
for i in range(10):
    print(i + 1, '-- Привет')


# Для получения последней цифры
for i in range(100, 1000):  # перебираем числа от 100 до 999
    if i % 10 == 7:         # используем остаток от деления на 10, для получения последней цифры
        print(i)

