start, end = 251763, 514827

mi = 0
count = 0
for x in range(start, end+1):
  s = sum( map(int, str(x)))
  if x % s == 0:
    count += 1
    if not mi:
      mi = x

print( count, mi )