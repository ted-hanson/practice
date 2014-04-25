from math import sqrt
def delta(n):
  for i in range(0, n/2+1):
    if i != 0 and i != n-i:
      yield (i, n-i)

def triplets(val):
  for i in range(0, val):
    for x, y in delta(i):
      print "trying "+str(x) + ", " +str(y)
      z = sqrt(x**2 + y**2)
      if z == int(z) and x+y+z == val:
        return x*y*int(z)    
  
print triplets(1000)
