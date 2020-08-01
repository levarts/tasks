# Даны координаты четырёх точек на плоскости. Проверьте, могут ли они являться вершинами квадрата ненулевой площади.
# Формат входных данных: в четырёх строках вводятся четыре пары вещественных чисел.
# Все числа по модулю не превосходят 100, и заданы с точностью не более 2 знаков после десятичной точки.
# Формат выходных данных: требуется вывести «YES», если точки могут являться координатами вершин квадрата, и «NO», если нет.
# Вывод: у квадрата совпадают две стороны и две диагонали

x1, y1 = map(float, input().split())

x2, y2 = map(float, input().split())

x3, y3 = map(float, input().split())

x4, y4 = map(float, input().split())

d1_2 = (x1 - x2)*(x1 - x2) + (y1 - y2)*(y1 - y2)
d1_3 = (x1 - x3)*(x1 - x3) + (y1 - y3)*(y1 - y3)
d1_4 = (x1 - x4)*(x1 - x4) + (y1 - y4)*(y1 - y4)
d2_3 = (x2 - x3)*(x2 - x3) + (y2 - y3)*(y2 - y3)
d2_4 = (x2 - x4)*(x2 - x4) + (y2 - y4)*(y2 - y4)
d3_4 = (x3 - x4)*(x3 - x4) + (y3 - y4)*(y3 - y4)
 
if (d1_2 and d1_3 and d1_4 and d2_3 and d2_4 and d3_4):
  if (d1_2 == d1_3 and 2*d1_2 == d1_4 and 2*d2_4 == d2_3):
    print("YES")
  elif (d1_3 == d1_4 and 2*d1_3 == d1_2 and 2*d2_3 == d3_4):
    print("YES")
  elif (d1_2 == d1_4 and 2*d1_2 == d1_3 and 2*d2_3 == d2_4):
    print("YES")
else:
  print("NO")