x = 81**79 + 75**2022 - 12**35

count = 0
prevOK = False
while x:
  d = x % 5
  if prevOK and d == 4:
    count += 1
  x //= 5
  prevOK = d not in [4, 0]
print( count )
