words = {
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
    10**12: 'trillion '
  }

def digits(n):
  global words
  s = str(n)
  i = len(s)
  if i == 0 or s == '0':
    return ''
  elif n in words:
    if i > 3:
      return 'one ' + words[n]
    else:
      return words[n]
  elif i == 2:
    return words[int(s[0])*10] + digits(int(s[1:])) 
  elif i == 3:
    u = words[int(s[0])] + 'hundred '
    v = digits(int(s[1:])) 
    if v != '':
      u += 'and '
    return u + v 
  elif i > 3:
    lead = (i+2)%3+1 # map digits correctly: 123|457 -> 1:3, 2:2, 3:1, 4:3, 5:2, 6:1
    # split digits before 3*n digits ie (12)|345 and then print the name appended to the following number
    u = digits(int(s[:lead])) + words[10**(i-lead)]
    v = digits(int(s[lead:]))
    if v != '' and len(str(int(s[lead:]))) <= 2:
      u += 'and '
    words[n] = u + v 
    return words[n]

print sum([len(digits(i).replace(' ', '')) for i in range(1, 1001)])
