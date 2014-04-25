import urllib2
from collections import Counter
import time

def getNameVal(s):
  return sum([ord(c) - ord('A') + 1 for c in s])

names = sorted(urllib2.urlopen("http://projecteuler.net/project/names.txt").read().replace('"',"").split(","))

start = time.time()
print sum([getNameVal(names[i])*(i+1) for i in range(0,len(names))])
print time.time() - start

