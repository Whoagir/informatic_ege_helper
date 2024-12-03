x = 19**81 + 23**709 - 4

count = 0
prevOK = False
while x:
  d = x % 9
  if prevOK and d == 8:
    count += 1
  x //= 9
  prevOK = d not in [8, 0]
print( count )    
  