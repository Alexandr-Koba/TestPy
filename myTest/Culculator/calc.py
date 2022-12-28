print("Калькулятор")

def plus(x, y):
    c = x + y
    print(f'{x} + {y} = {c}')
    return c

def minus(x, y):
    c = x - y
    print(f'{x} - {y} = {c}')
    return c

def umnoj(x, y):
    c  = x * y
    print(f'{x} * {y} = {c}')
    return c


user_input = input('Введите: сложение " + ", вычитание " - ", умножение " * ": ')
if user_input == '+':
    plus(int(input('цифра 1: ')), int(input('цифра 2: ')))
if user_input == '-':
    minus(int(input('цифра 1: ')), int(input('цифра 2: ')))
if user_input == '*':
    umnoj(int(input('цифра 1: ')), int(input('цифра 2: ')))

