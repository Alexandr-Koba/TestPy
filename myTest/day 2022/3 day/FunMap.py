'''


'''

a = [-1, 2, -3, 4, 5]

b = list(map(abs, a)) # Положительные
print(b)

c = ['Koba', 'Babakoba', 'ProKoba'] # Верхний регистр
x = list(map(str.upper, c))
print(x)

h = list(map(len, c)) # Кол-во символов в строке.
print(h)

def info_user(x, b):
    c = x + b
    print(c)
    return c

info_user(int(input()), int(input()))