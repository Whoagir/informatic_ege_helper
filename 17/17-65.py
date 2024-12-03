def prod(a):
  if not a: return 1
  else: return a[0]*prod(a[1:])

maxNum = 0
count = 0
for i in range(8800, 55535+1):
  digits = list(map(int, str(i)))
  if digits.count(7) >= 1 and prod(digits) > 35:
    count += 1
    maxNum = i

print( maxNum, count )