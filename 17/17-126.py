start, end = 2125, 665123

su = 0
count = 0
for x in range(start, end+1):
  s = str(x)
  sumDig = sum(map(int,s))
  if sumDig > 12 and '0' in s:
    count += 1
    su += x
print( count, su % 10000 )