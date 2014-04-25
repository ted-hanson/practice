import time

def fib():
  a = 1
  i, j = (1,1)
  yield i
  while True:
    t, i = (i, j)
    j = t + j
    yield i

start = time.time()
for i, num in enumerate(fib()):
  if len(str(num)) == 1000:
    print i+1
    print num
    break
print time.time() - start
