def primes(n):
  i = 3
  primes = [2]
  while len(primes) < n:
    for x, y in enumerate(primes):
      if i % y == 0:
        break
      elif x == len(primes)-1:
        primes += [i]
        break
    i += 2
  return primes[len(primes)-1]

print "the 6th prime should be 13:"
print primes(10001)
