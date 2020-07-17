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
