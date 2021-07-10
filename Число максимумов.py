Нахождение количества чисел, равных максимальному числу в последовательности

n = int(input())
max = n
a = []

while (n != 0):
    n = int(input())
    a.append(n)
    if (n > max):
      max = n

c = 0

for i in a:
  if (i == max):
    c = c + 1

print(c)