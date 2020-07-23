# A natural number k is given.
# Find the k-th super prime number in this order.

k = int(input())
super = 0 # serial number of a super prime number
c = 2 # ordinal number of a prime number
num = 2 # numbers in order from 3, because number 2 is not super-prime

while (super < k):
  num += 1
  flag = 1
  for i in range(2, num//2 + 1): # find a prime number
    if (num % i == 0):
      flag = 0
      break
  if (flag): # if the number is prime
    for i in range(2, c//2 + 1): # check if its index is prime
      if (c % i == 0):
        flag = 0
        break
    if (flag): #if the index is also prime
      super += 1 # that number is super prime
    c += 1 # increase the ordinal number of a prime number

print(num) # output of the k-th super-prime number