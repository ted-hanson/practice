import time
cache = {
  2: [1],
  3: [1]
}

def divisors(n):
  global cache
  if n in cache:
    return cache[n]
  i = 2 
  factors = [1]
  while i ** 2 <= n:
    factor = n/float(i)
    if factor == int(factor):
      if i != int(factor):
        factors += [i, int(factor)]
      else:
        factors += [i]
    i += 1
  cache[n] = factors
  return factors

def primesRange(n):
  for i in range(1, n+1,2):
    if len(divisors(i)) == 1:
      yield -i
      yield i

def maxSequence(a, b):
  n = 0
  while len(divisors(abs(n**2+a*n+b))) == 1:
    n += 1
  return n


start = time.time()
p = None
m = -1
for prime in primesRange(1000):
  for a in range(-1000, 1000):
    cm = maxSequence(a, prime)
    if m < cm:
      m = cm
      p = (a, prime)

print p
print m
print time.time() - start
