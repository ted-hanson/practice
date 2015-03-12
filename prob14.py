def isOdd(n):
  return bool(n & 1)

known = {1:0}
def calcIters(num):
  onum = num
  count = 0
  while num not in known:
    if isOdd(num):
      num = 3 * num + 1
    else:
      num /= 2
    count += 1
  known[onum] = known[num] + count
  return known[onum]

maxVal = (0,0)
for i in range(1,10**6):
  count = calcIters(i)
  print str(i) + " has a sequence of " + str(count)
  if count > maxVal[1]:
    maxVal = (i, count)

print maxVal
