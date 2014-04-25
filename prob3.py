from math import sqrt
def largeFactor(num):
  factors = []
  for i in range(2, int(sqrt(num)) + 1):
    x = num/i
    if float(num)/i == x:
      factors = factors[:len(factors)/2] + [x, i] + factors[len(factors)/2:]
  primes = {}
  found = 0
  i = 2
  while i < int(sqrt(factors[0])) + 1:
    j = 0
    while j < len(factors)-found:
      factor = factors[j]
      if factor == i:
        j += 1
        found += 1
      elif factor/i == float(factor)/i:
        factors = factors[:j] + factors[j+1:]
        print str(factor) + " is divisible by: " + str(i) 
      else:
        j += 1
    i += 1
  print factors
largeFactor(999999999999999)
