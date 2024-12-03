start, end = 198372, 876193

ma = 0
count = 0
for x in range(start, end+1):
  s = sum( map(int, str(x)))
  if x % s == 11:
    count += 1
    ma = x

print( count, ma )