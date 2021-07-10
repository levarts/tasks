Сколько раз менялся знак в последовательности?

prev = int(input())
c = 0

while (prev != 0):
  n = int(input())
  if (prev * n < 0):
    c = c + 1
  prev = n

print(c)