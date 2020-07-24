# How many ways can you choose K paints from the available 50 different ones?
# Input: 1 <= K <= 50
# Output: one number – the answer
# The solution is to compute the combinations

k = int(input())
n = 50

fact_n = 1
for t in range(n - k + 1, n + 1):
  fact_n *= t

fact_k = 1
for t in range(2, k + 1):
  fact_k *= t

print(fact_n // fact_k)

# or:
k = int(input())
n = 50

n_fact = 1
k_fact = 1

for t in range(1, min(k, n - k) + 1):
  n_fact *= n
  k_fact *= t
  n -= 1
  
print(n_fact // k_fact)