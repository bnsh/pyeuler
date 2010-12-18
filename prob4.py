#! /usr/local/bin/python

def isPalindrome(n):
	digits = []
	d = n
	while (d > 0):
		digits.append(d % 10)
		d = d // 10
	retVal = True
	reversed = digits[:]
	reversed.reverse()
	for i in xrange(0,len(digits)):
		retVal = retVal and (digits[i] == reversed[i])

	return(retVal)

maxpalindrome = 0
for i in xrange(100,1000):
	for j in xrange(100,1000):
		if (isPalindrome(i*j)):
			if (maxpalindrome < i*j):
				maxpalindrome = i*j

print maxpalindrome
