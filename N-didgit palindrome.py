# How many N-digit numbers are there that
# read the same from left to right and right to left?
# Input: 1 <= N <= 30
# Output: one number - the answer
# The solution based on combinatorics

n = int(input()) 
res = 9

for i in range(0, (n - 1)//2):
  res *= 10

print(res)