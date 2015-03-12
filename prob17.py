words = {
    0: 'zero ',
    1: 'one ',
    2: 'two ',
    3: 'three ',
    4: 'four ',
    5: 'five ',
    6: 'six ',
    7: 'seven ',
    8: 'eight ',
    9: 'nine ',
    10: 'ten ',
    11: 'eleven ',
    12: 'twelve ', 
    13: 'thirteen ', 
    14: 'fourteen ', 
    15: 'fifteen ', 
    16: 'sixteen ', 
    17: 'seventeen ', 
    18: 'eighteen ', 
    19: 'nineteen ', 
    20: 'twenty ', 
    30: 'thirty ', 
    40: 'forty ', 
    50: 'fifty ', 
    60: 'sixty ', 
    70: 'seventy ', 
    80: 'eighty ', 
    90: 'ninety ', 
    10**3: 'thousand ',
    10**6: 'million ',
    10**9: 'billion ',
    10**12: 'trillion ',
    10**15: 'quadrillion '
  }

def addAnd(left, right, should_and):
  return left + ('and ' if right != '' and should_and else '') + right

def digits(n):
  global words
  s = str(n)
  i = len(s)
  if i == 0 or int(s) == 0:
    return ''
  elif i > 3:
    # map digits to hundreds correctly: 123|457 -> 1:get next 3 digits, 2: get next 2 digits, 3: only get 1 digit, 4:3, 5:2, 6:1
    lead = (i + 2) % 3 + 1 
    # get number on the left side of 10**3
    left = digits(int(s[:lead])) + words[10**(i-lead)]
    # get number on the right side of 10**3
    right = digits(int(s[lead:]))
    # don't add and between 1000's and 100's
    word = addAnd(left, right, int(s[lead:]) <= 99)
    # Don't overwrite defaults i.e. 1000
    if n not in words:
      words[n] = word
    return word
  # take custom digits <= 3 before automating
  elif n in words:
    return words[n]
  # make word for two digit numbers
  elif i == 2:
    return words[int(s[0])*10] + digits(int(s[1:])) 
  # make word for 3 digit numbers
  elif i == 3:
    # hundreds digit
    left = words[int(s[0])] + 'hundred '
    # rest of number
    right = digits(int(s[1:])) 
    return addAnd(left, right, True)

nums = [digits(i).replace(' ', '') for i in range(1, 1001)]
print nums
print sum(map(len, nums))
