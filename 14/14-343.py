x = 7*512**3200 + 6*256**3100 - 5*64**3000 - 4*8**2900 - 1542

count = 0
while x > 0:
  if x % 64 == 0:
    count += 1
  x //= 64

print( count )