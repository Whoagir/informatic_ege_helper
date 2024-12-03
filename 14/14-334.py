x = 53**123 + 65**2222 - 172**12
count = 0
prevOK = False
while x:
  d = x % 7
  if prevOK and d == 6:
    count += 1
  x //= 7
  prevOK = d not in [6, 0]
print( count )
