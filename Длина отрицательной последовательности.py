Вычислить максимальную длину подпоследовательности,
состоящей из отрицательных элементов.
Вся последовательность оканчивается нулем.

prev = int(input())
c = 1
max = 0

while (prev != 0):
  curr = int(input())
  if (curr < 0) and (prev < 0):
    c = c + 1
  elif (curr < 0):
    c = 1
  else:
    if (c > max):
      max = c
    c = 1
  prev = curr

print(max)