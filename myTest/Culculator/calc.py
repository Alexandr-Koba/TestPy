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

def delit(x, y):
    c  = x / y
    print(f'{x} / {y} = {c}')
    return c

def proc(x, y):
    c  = x % y
    print(f'{x} % {y} = {c}')
    return c


user_input = input('Введите: " + ", " - ", " * ", "/", "%" ')
if user_input == '+':
    plus(int(input('цифра 1: ')), int(input('цифра 2: ')))
if user_input == '-':
    minus(int(input('цифра 1: ')), int(input('цифра 2: ')))
if user_input == '*':
    umnoj(int(input('цифра 1: ')), int(input('цифра 2: ')))
if user_input == '/':
    if user_input == 0:
        print('На 0 делить нельзя!')
    else:
        delit(int(input('цифра 1: ')), int(input('цифра 2: ')))
if user_input == '%':
    proc(int(input('цифра 1: ')), int(input('цифра 2: ')))

