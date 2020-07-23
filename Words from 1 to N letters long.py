# The manufacturers of flakes "Alphabet"
# have released a new line of flakes "Four Letters",
# where, as you might guess, there are only 4 types of letters.
# She considers "Words" any words from 1 to N letters long.
# How many "Words" can she make up this time?
# Input: 1 <= N <= 20
# Output: one number – answer to the problem

n = int(input())

s = 0
p = 1

for i in range(0, n):
  p *= 4
  s += p

print(s)

# or if you notice that this is a geometric progression:
n = int(input())
res = 4 * (pow(4, n) - 1) // 3
print(res)