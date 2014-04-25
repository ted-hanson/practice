def sum(x,y):
  return x+y
def sqr(x):
  return x*x
def rangeDif(r):
  return sqr(reduce(sum, r)) - reduce(sum, map(sqr, r))

print "Testing [1..10] should be 2640"
print rangeDif(range(1,11))
print rangeDif(range(1,101))
