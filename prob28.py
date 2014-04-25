import time
def genTriangle(side):
  if side <= 1:
    return 1
  return 4 * side**2 - 6 * (side - 1) + genTriangle(side-2) 

start = time.time()
print genTriangle(1001)
print time.time() - start
