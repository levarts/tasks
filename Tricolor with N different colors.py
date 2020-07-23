# How many ways can you make a tricolor
# flag with horizontal stripes
# of the same width if
# you have N different colors?
# Input: 3 <= N <= 1000
# Output: one number - the answer

n = int(input())
res = 1

for i in range(n - 2, n + 1):
  res *= i

print(res)

# or:
n = int(input())

for i in range(n - 2, n):
  n *= i

print(n)

# or:
print(n*(n - 1)*(n - 2))