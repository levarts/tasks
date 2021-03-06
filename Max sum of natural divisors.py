# Find a number in the interval [l;r]
# with the maximum sum of its natural divisors
# Input: left and right border of the interval
# Output: a number with the maximum sum of its natural divisors

l = int(input())
r = int(input())
max_sum = 0

for i in range(l, r+1):
  sum = 0
  for j in range(1, i):
    if (i % j == 0):
      sum += j
  if (sum >= max_sum):
    max_sum = sum
    num = i

print(num)
