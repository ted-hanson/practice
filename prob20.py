import math
import time

def sumDigits(n):
  return sum([int(d) for d in str(math.factorial(n))])

start = time.time()

print sumDigits(100)

print time.time() - start
