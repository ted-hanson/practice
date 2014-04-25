
# constant time pal test
def isPal(num):
  i = str(num)
  j = i[::-1]
  return i[:int(len(i)/2)] == j[:int(len(i)/2)]

# streaming delta pair generator
def delta(num):
  for i in xrange(0, num/2+1):
    yield (i, num-i)

def largePal(digits):
  num = 10**digits-1
  curStack = []
  for i in xrange(0, num):
    for x, y in delta(i):
      print "trying: "+str(x)+","+str(y)
      curVal = (num-x)*(num-y)
      if isPal(curVal):
        print str(x)+","+str(y)+" is: "+str(curVal)+"!"
        curStack += [curVal]
    if len(curStack) > 0:
      print curStack
      break
  return max(curStack)

print largePal(6)
