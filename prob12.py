solved = {2:{2:2}, 3:{3:2}, 4:{2:3}, 5:{5:2}}

def mult(a, b):
  return a*b

def getTri(n):
  return n*(n+1)/2

def add(key, hash, val=1):
  if key in hash:
    hash[key] += val
  else:
    hash[key] = val+1
  return hash

def factorize(n):
  global solved
  o = n #save value
  i = 2
  factors = {}
  while i <= n:
    while float(n)/i == int(n/i):
      if i in factors:
        factors[i] += 1
      else:
        factors[i] = 2
      n /= i
    i += 1
  solved[o] = factors 
  return factors

import time

start = time.time()
for i in range(10,100000):
  j = factorize(getTri(i))
  if reduce(mult, j.values()) > 500:
    print "Triangle #"+str(i)+" aka "+ str(getTri(i)) + " of value: "+str(reduce(mult, j.values()))
    break
print time.time() - start, "seconds"
