import time
from itertools import izip
def calcVal(count, coins):
  s = 0
  for i,j in izip(count,coins):
    s += i*j
  return s

def waysToAmt(amt, coins):
  if amt == 0:
    return 1
  elif coins == []:
    return 0
  else:
    s = 0
    maxcoin, i = coins[0], 0
    while maxcoin*i <= amt:
      s += waysToAmt(amt - maxcoin*i, coins[1:])
      i += 1
    return s

#mk2
def waysToAmt(amt, coins):
  ways = [1 if i == 0 else 0 for i in range(0, amt+1)]
  for c in coins:
    for i in range(c, amt+1):
      ways[i] += ways[i-c]
  return ways[amt]


start = time.time()
print waysToAmt(200,[1,2,5,10,20,50,100,200])
print time.time() - start
