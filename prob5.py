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

n = 20
p = 1
s = sieve(n)
for f in s:
	k = 0 # we're trying to model f^k
	v = 1
	while ((v*f) < n):
		v = v * f
		k = k + 1
	p = p * v

print p
