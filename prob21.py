import time
cache = {
  2: [1,2],
  3: [1,3]
}

acache = {
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
      factors += [i, int(factor)]
    i += 1
  cache[n] = factors
  return factors

def isAmicable(n):
  global acache
  if n in acache:
    return acache[n]
  ns = sum(divisors(n))
  if ns == n:
    return False
  nss = sum(divisors(ns))
  if n == nss:
    acache[n] = True
    acache[nss] = True
  else:
    acache[n] = False
  return acache[n]

def d(n):
  tot = [] 
  for i in range(2, n):
    if isAmicable(100):
      tot += [i]
  return tot

start = time.time()

print sum(d(10000))

print time.time() - start
