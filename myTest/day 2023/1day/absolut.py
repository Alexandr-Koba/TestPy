'''
Абсолютная сумма

Даны пять чисел a_1, \, a_2, \, a_3, \, a_4, \, a_5a1​,a2​,a3​,a4​,a5​. 
Напишите программу, 
которая вычисляет сумму их модулей |a_1| + |a_2| +|a_3| +|a_4| + |a_5|∣a1​∣+ ∣a2​∣+∣a3​∣+∣a4​∣+ ∣a5​∣.

Формат входных данных
На вход программе подается пять действительных чисел a_1, \, a_2, \, a_3, \, a_4, \, a_5a1​,a2​,a3​,a4​,a5​, 
каждое на отдельной строке.

Формат выходных данных
Программа должна вывести одно число – сумму модулей введёных чисел.
'''

a = abs(float(input()))
b = abs(float(input()))
c = abs(float(input()))
d = abs(float(input()))
e = abs(float(input()))

print(a + b + c + d + e)