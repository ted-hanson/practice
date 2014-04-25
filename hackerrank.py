import random
from math import log

def getCurrentVals(first, second):
  x = (0, 100, 100)
  for i in range(0, len(first)):
    if first[i] > second[i]:
      x = (x[0], x[1] - first[i], x[2])
    elif second[i] > first[i]:
      x = (x[0], x[1], x[2] - second[i])
    else:
      if x[0] % 2 == 0:
        x = (x[0] + 1, x[1] - first[i], x[2])
      else:
        x = (x[0] + 1, x[1], x[2] - second[i])
  return x

def avg(l):
  return sum(l)/len(l)

# 0 1 2 3 4 5 6 7 8 9 10
def calculate_bid(player, pos, first_moves, second_moves):
  s = [first_moves, second_moves]
  ties, first, second = getCurrentVals(first_moves, second_moves)
  counts = [first, second]
  mine = counts[player-1]
  other = counts[player-2]
  mytie = ties % 2 == player - 1
  d = pos if player == 1 else 10 - pos
  if d == 1:
    return mine
  elif d == 2:
    return 1
  elif d >= 5 or d <=7:
    return int(min(min(float(other)/10 + float(mine)/10 + (0 if mytie else 1), (other if other > 0 else 1)), mine))
  else:
    return int(min(min(avg(s[player-2]) + (0 if mytie else 1), (other if other > 0 else 1)), mine))

print calculate_bid(1,2,[20, 18, 16, 1, 13, 1, 10, 1, 8, 7, 8, 1,6],[15, 15, 14,16, 11, 12, 8, 8, 6, 6, 9, 3, 2])
