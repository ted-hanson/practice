from collections import defaultdict
def sumPrimes(max):
  p = defaultdict(int)
  i = 2
  while i**2 < max:
    if p[i] != 0:
      i += 1
      continue
    for j in range(2, int(max/i)+1):
      f = i * j
      p[f] = f
    i += 1
  return max*(max+1)/2 - 1 - sum(p.values())
  
print "The sum of primes below 10 is 17"
print sumPrimes(10)
print "The sum of primes below 2*10^6 is:"
print sumPrimes(2*10**6)
