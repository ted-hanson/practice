import time
# Use Fermat's little theorem 10^n-1 mod d = 0 for prime d and n < d
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

start = time.time()
max = 999
for i in range(max, 1, -2):
  if len(divisors(i)) == 1:
    n = 1
    while (pow(10, n) - 1) % i != 0:
      n += 1
    if i - n == 1:
      print i
      break
print time.time() - start
