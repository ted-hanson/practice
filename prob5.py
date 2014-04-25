# Euclid's Algorithm
def gcd(x, y):
  while True:
    if x == 0:
      return y
    y = y % x 
    if y == 0:
      return x
    x = x % y

# LCM in terms of gcd
def lcm(x, y):
  z = gcd(x,y)
  return 0 if z == 0 else x / z * y

def divisible(vals):
  return reduce(lcm, vals)
print divisible(range(1,10))
