# Input: a number
# Output: true/false
n = int(input())

if (n % 2 == 0): # if a number is even, then it is definitely composite
  print(n == 2)
else: 
  i = 3
  while (i * i <= n) and (n % i != 0):
    i += 2
  print(i * i > n)
