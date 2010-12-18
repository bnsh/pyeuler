#! /usr/local/bin/python

def sieve(n):
	isPrime = []
	primes = []
	i = 1
	while (i <= n):
		isPrime.append(1)
		i = i+1

	j = 2
	while (j < n):
		while ((j < n) and (not isPrime[j])): j = j + 1
		if (j < n):
			primes.append(j)
			k = 2 * j
			while (k < n):
				isPrime[k] = 0
				k += j
			j = j + 1
	return(primes)

n = 200000
s = sieve(n)
print s[10001-1]
