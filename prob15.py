import math

def sqrGen(e):
  return [[0 for i in range(0,e)] for i in range(0,e)]

def calcRoutes(e):
  l = sqrGen(e + 1)
  # only one way to start :)
  l[0][0] = 1
  for i in range(0, len(l)):
    for j in range(0, len(l)):
      # add ways to get to point from above
      if j+1 < len(l):
        l[i][j+1] += l[i][j]
      # add ways to get to point from left
      if i+1 < len(l):
        l[i+1][j] += l[i][j]
  return l 

square = calcRoutes(20)
for row in square:
  print row

print square[-1][-1] 
