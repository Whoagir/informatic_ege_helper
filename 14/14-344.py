x = 343**1515 - 6*49**1520 + 5*49**1510 - 3*7**1530 - 1550

count = 0
while x > 0:
  if x % 7 == 0:
    count += 1
  x //= 7

print( count )