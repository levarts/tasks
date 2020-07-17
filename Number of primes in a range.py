# Find the number of prime numbers in the range from [a, b].
# Input data format: two integers a, b (−3600≤a≤b≤3600), each on a new line.
# Output data format: the number of prime numbers in this range.
# Notes: a number is called prime if it is a natural (non-negative integer),
# and it has exactly two different natural divisors: 1 and the number itself.

a = int(input())
b = int(input())
c = 0

if (b <= 1):
	print(c)
else:
	if (a <= 1):
		a = 2
	for i in range(a, b+1):
		flag = 1
		for j in range(2, i//2 + 1):
			if (i%j == 0):
				flag = 0
				break
		if (flag): # if the number is prime
			c += 1
	print(c)
