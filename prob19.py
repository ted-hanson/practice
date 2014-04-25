import time

"""
Thanks Gauss!
"""

months = {
  1: 0,
  2: 3,
  3: 3,
  4: 6,
  5: 1,
  6: 4,
  7: 6,
  8: 2,
  9: 5,
  10: 0,
  11: 3,
  12: 5
}

def isLeap(y):
  return y % 400 == 0 or (y % 4 == 0 and not y % 100 == 0)

def mval(m, leap):
  if m < 3 and leap:
    return months[m] - 1
  else:
    return months[m]

def cnum(y):
  return 6 - int(str(y)[:2]) % 4 * 2

def gausDay(month, day, year):
  m = mval(month, isLeap(year))
  y = int(str(year)[2:])
  c = cnum(year)
  return (day + m + y + y/4 + c) % 7

def findSundaysTo(y):
  l = []
  for year in range(1901, y+1):
    for month in range(1, 13):
      if gausDay(month, 1, year) == 0:
        l += [(month, 1, year)]
  return l

start = time.time()

print len(findSundaysTo(2000))

print time.time() - start
