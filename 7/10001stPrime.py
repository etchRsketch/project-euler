#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?

#sieve of eratosthenes

integers = []
numbers = 110000
print numbers
for x in range(3, numbers, 2):
  integers.append(x)
print integers[-1]
primes = [2]

def nthPrime(n):
  for p in integers:
    for element in integers:
      if element % p == 0:
        if element == p:
          primes.append(p)
          if len(primes) == n:
            return primes[-1]
        if element != p:
          integers.remove(element)
  return 0


print "10001th prime is " + str(nthPrime(10001))
