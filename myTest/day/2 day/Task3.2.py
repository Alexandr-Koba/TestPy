"""
Сама неотвратимость 🌶️
Безумный титан Танос собрал все 6 камней бесконечности и намеревается уничтожить половину населения Вселенной по щелчку пальцев. При этом если население Вселенной является нечетным числом, то титан проявит милосердие и округлит количество выживших в большую сторону. Помогите Мстителям подсчитать количество выживших.

Формат входных данных
На вход дается число целое nn – население Вселенной.

Формат выходных данных
Программа должна вывести одно число – количество выживших.

"""

guys = int(input())
print(guys // 2 + guys % 2)