def palCount( n ):
  count = 0
  while count < 100:
    n += int(str(n)[::-1])
    count += 1
    if str(n) == str(n)[::-1]: break
  return count

count = 0
for n in range(100, 201):
  if palCount(n) <= 5:
    count += 1

print( count )