def prod(a):
  if not a: return 1
  else: return a[0]*prod(a[1:])

maxNum = 0
count = 0
for i in range(333666, 666999+1):
  digits = list(map(int, str(i)))
  if digits.count(7) >= 2 and i % 17 == 0:
    count += 1
    maxNum = i

print( maxNum, count )