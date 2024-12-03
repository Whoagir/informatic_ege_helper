start, end = 1110, 1111101

mi = 0
count = 0
for x in range(start, end+1):
  if (x % 16 == 0 or x % 48 == 0) and \
     (x % 2 == 0 or (x % 3 != 0 and x % 18 != 0 and x % 63 != 0)):
    count += 1
    if not mi: mi = x
print( count, mi )