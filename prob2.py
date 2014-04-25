def prob2(x, y, odd1, odd2, maxVal):
  if y < maxVal:
    print [x, y, odd1, odd2] if odd1 and odd2 else "nope"
    return (x if odd1 and odd2 == 0 else 0) + prob2(y, x+y, odd2, odd1 != odd2, maxVal)
  print [x, y, odd1, odd2] if odd1 and odd2 else "nope"
  return (x if odd1 and odd2 else 0)
print prob2(1, 2, False, True,  4000000)
