Даны два числа A и B, большие 0.
Выведите все числа на отрезке от A до B,
запись которых является палиндромом.

a = int(input())
b = int(input())

for n in range(a, b + 1):
  n = str(n)
  l = len(n)
  for i in range(0, l//2):
    if (n[i] != n[l-1 - i]):
      break
  else:
    print(n)