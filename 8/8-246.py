MIN, MAX = 3, 9

count = 0
for L in range(MIN,MAX+1):
  p = 7
  for i in range(L-1): p *= 6
  print( L, p)
  count += p

print(count)

