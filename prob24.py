import time

def appendToAll(a, all):
  for item in all:
    yield a+item

def list_num(digits):
  if len(digits) == 1:
    yield digits
  elif len(digits) == 2:
    yield digits
    yield digits[::-1]
  else:
    for i in range(0,len(digits)):
      for y in appendToAll(digits[i], list_num(digits[:i]+digits[i+1:])): 
        yield y

i = 1
j = 2
start = time.time()
for e in list_num("0123456789"):
  if i == j:
    print e
    break
  i += 1
print time.time() - start
