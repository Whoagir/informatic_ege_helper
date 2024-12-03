start, end = 25552, 58885

ma = 0
count = 0
for x in range(start, end+1):
  dCount = 0
  for d in range(10,min(100,x+1)):
    if x % d == 0:
      dCount += 1
  if dCount >= 15:
    count += 1
    ma = x
print( ma, count )