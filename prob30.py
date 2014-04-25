import time

def pow5(a):
  return int(a)**5

i = 9
digits = 1
while pow5(9)*digits >= i:
  i += 9 * 10**digits
  digits += 1
i = pow5(9)*digits

start = time.time()
for i in range(2, i):
  j = sum(map(pow5, str(i)))
  if j == i:
    print i
print time.time() - start
