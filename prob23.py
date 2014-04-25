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

def abundantRange(n):
  abundant = []
  for i in range(1,n):
    if sum(divisors(i)) > i:
      abundant.append(i)
  return abundant

def sumAbunds(n):
  a = abundantRange(n)

  found = {
  }
  for i in range(0, len(a)):
    for j in range(i, len(a)):
      s = a[i] + a[j]
      if s not in found and s < n:
        found[s] = s
      elif s >= n:
        break
  return found

def coolSol(n):
  y=0
  abn = set()
  for i in range(1, n):
    s = sum(divisors(i))
    if s > i:
      abn.add(i)
    if not any((i-a in abn) for a in abn):
      y += i
  return y

start = time.time()
print coolSol(20162)
print time.time() - start

start = time.time()
print sum(range(0,20200)) - sum(sumAbunds(20200).keys())
print time.time() - start
