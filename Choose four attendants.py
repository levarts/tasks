# From the class in which N people study,
# 4 people are assigned to duty in the dining room.
# Kolya became very interested in how many ways this can be done.
# Kolya is a special boy,so immediately after the first question he had a second:
# how many ways are there to recruit a team of attendants,
# which Kolya himself will definitely get into?
# Input: 4 <= N <= 100
# Output: two numbers – the number of ways to select four attendants
# and the number of ways to select four attendants, if Kolya must be among them.

# Hint: If Kolya is selected, then it remains to choose 3 people from the remaining N-1

n = int(input())
k = 4

n_fact = 1
k_fact = 1
nn = n - 1 # number of students without Kolya

for t in range(1, min(k - 1, n - k) + 1):
  n_fact *= nn
  k_fact *= t
  nn -= 1

res = n_fact // k_fact

print(res * n // k) # number of ways to select four attendants
print(res) # the number of ways to choose four attendants, if Kolya must be among them

# or:
n = int(input())
k = 4

n_fact = (n - 3)*(n - 2)*(n - 1)
k_fact = 6

res = n_fact // k_fact

print(res * n // k)
print(res)