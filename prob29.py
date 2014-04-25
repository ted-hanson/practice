import time
from sets import Set

start = time.time()
s = set()
for i in range(2, 101):
  for j in range(2, 101):
    s.add(i**j)
print len(s)
print time.time() - start
