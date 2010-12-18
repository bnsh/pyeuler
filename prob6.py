#! /usr/local/bin/python

sum2 = 0
sum = 0
for i in range(1,101):
	sum += i
	sum2 += i*i

print sum*sum - sum2
