# The flakes "Alphabet" had N different letters.
# Ira designated with the "Word" any sequence of N letters
# in which there are at least two identical letters.
# How many "Words" can Ira make from flakes?
# Input: 2 <= N <= 10

n = int(input())
all_words = pow(n, n)
uniq_words = 1

for i in range(2, n + 1):
  uniq_words *= i

print(all_words - uniq_words)
