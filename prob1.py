#! /usr/local/bin/python

sum = 0
for x in xrange(1,1000):
	if (((x % 3) == 0) or ((x % 5) == 0)):
		sum += x

print sum

# Or this?
# print sum(i for i in range(1,1000) if (((i % 3) == 0) or ((i % 5) == 0)))
