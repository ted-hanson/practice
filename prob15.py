import math

def mult(a, b):
  return a*b

def sqrGen(e):
  return [[0 for i in range(0,e)] for i in range(0,e)]

def calcPts(e):
  l = sqrGen(e)
  l[0][0] = 1
  for i in range(0, len(l)):
    for j in range(0, len(l)):
      if j+1 < len(l):
        l[i][j+1] += l[i][j]
      if i+1 < len(l):
        l[i+1][j] += l[i][j]
  return l 

print "Matrix of 0's"
for row in sqrGen(20):
  print row

l = calcPts(5)
print l
print l[len(l)-1][len(l)-1] 
