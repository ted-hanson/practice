def prob1(numbers, max):
  sum = 0
  numsUsed = {}
  for n in numbers:
    t = n
    while t < max and t not in numsUsed:
      sum += t
      numsUsed[t] = True
      t += n
  print "The sum is: "+str(sum)

prob1([3, 5], 10)
