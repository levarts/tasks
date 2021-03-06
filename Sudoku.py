Цель игры (не данного задания) состоит в том, чтобы заполнить все игровое поле цифрами от 1 до 9 так, 
чтобы выполнялись следующие три условия:
1. в любой строке каждая цифра встречается только 1 раз
2. в любом столбце каждая цифра встречается только 1 раз
3. в любом квадрате 3х3 каждая цифра встречается ровно 1 раз

В данном же задании Вам необходимо ответить на следующий частный вопрос: 
Имеется некоторое состояние игрового поля и координаты пустой ячейки. 
Какие цифры можно в текущий момент поставить в эту ячейку, чтобы не нарушалось ни одно из трех правил выше?

Ввод
Первые 9 строк задают игровое поле. Каждая строка состоит из 9 символов от '0' до '9'.
Символ '0' обозначает пустую ячейку.
10-я строка - номер строки целевой ячейки на игровом поле (нумерация от 0 до 8)
11-я строка - номер столбца целевой ячейки на игровом поле (нумерация от 0 до 8)
Гарантируется, что целевая ячейка является пустой. 
В двух примерах ниже закодировано игровое поле из картинки выше.

Вывод
Цифры, которые можно в текущий момент поставить в целевую ячейку, не нарушая ни одно из 3 ограничений, описанных
в условии игры выше. Цифры необходимо вывести в порядке возрастания, каждая цифра в отдельной строке.
Учитывая, что целевая ячейка пустая и игровое поле корректно, всегда будет хотя бы одна возможная цифра.

Пример 1:
Ввод
530070000
600195000
098000060
800060003
400803001
700020006
060000280
000419005
000080079
4
4

Вывод
5

Пример 2:
Ввод
530070000
600195000
098000060
800060003
400803001
700020006
060000280
000419005
000080079
7
2

Вывод
2
3
7
______________________________________________________________________________________________________________________
Идея: собрать все числа из строки, столбца и квадрата, где находится искомая клетка, и
вывести числа, которых там нет.

a = []

for i in range(9):
    a.append(list(input())) # заполнение двуменого массива

n, m = int(input()), int(input())
already = set() # создание множества (содержит не повторяющиеся элементы в случайном порядке)

for i in range(9):
    already.add(a[n][i]) # добавление элементов строки в множество
    already.add(a[i][m]) # добавление элементов столбца в множество

# в множестве already будут числа, содержащиеся в строке и стобце искомой клетки

# определение в каком квадрате 3х3 находится клетка
n = (n // 3) * 3
m = (m // 3) * 3

# добавление элементов квадрата 3х3 в множество
for i in range(n, n + 3):
    for j in range(m, m + 3):
        already.add(a[i][j])
        
# если числа от 1 до 9 нет в множестве, то выводим его
for i in range(1, 10):
    if str(i) not in already:
        print(i)