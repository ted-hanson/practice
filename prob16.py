def digits(n):
  return str(n)

def dsum(a,b):
  return int(a)+int(b)

def sumDigits(n):
  return reduce(dsum, digits(n))

print sumDigits(2**1000000)
