known = {1:1}

maxCount = -1
num = None
for i in range(1,10**7):
  count = 0
  curNum = i
  while i > 1:
    if i in known:
      break
    elif float(i)/2 == i/2:
      i /= 2
    else:
      i *= 3
      i += 1
    count += 1
  known[curNum] = known[i] + count
  if count > maxCount:
    maxCount = count
    num = curNum
  print str(curNum) + " has a sequence of "+str(count)
print str(num) + " has a sequence of "+str(maxCount)
