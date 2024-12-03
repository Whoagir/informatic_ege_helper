start, end = 1000, 10001

mi = 0
count = 0
for x in range(start, end+1):
  if (x % 10 == 0 or x % 63 == 0) and x % 255 == 0:
    count += 1
    if not mi: mi = x
print( count, mi )