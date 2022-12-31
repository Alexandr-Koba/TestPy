'''
Гонка спидстеров
Зум бросил вызов Флэшу и предложил ему честный поединок в виде гонки вокруг магнетара. В 
случае проигрыша эта нейтронная звезда зарядится и уничтожит мир, 
поэтому Флэш решил не рисковать без причины, и узнать у своего друга Циско 
Рамона есть ли смысл принимать вызов. Циско получил данные, что скорость Зума равна nn, 
а скорость Флэша равна kk.

Напишите программу, которая должна вывести ответ Циско на вопрос Флэша.

Формат входных данных
На вход программе подаётся два целых числа nn и kk, скорость Зума и Флэша.

Формат выходных данных
Если Зум быстрее Флэша нужно вывести «NO», если Флэш быстрее Зума нужно вывести «YES», 
если их скорости равны нужно вывести "Don't know".
'''


Zoom_Speed = int(input())      # Скорость Зума
Flash_Speed = int(input())     # Скорость Флеша
if Zoom_Speed > Flash_Speed:   # Если Зум быстрее Флеша - Флеш проиграет
    print('NO')                
elif Flash_Speed > Zoom_Speed: # Если Флеш быстрее Зума - Флеш выиграет
    print('YES')               
else:                          # Если скорость Флеша и Зума одинакова, то выиграет тот, на чьей стороне будет удача
    print("Don't know")