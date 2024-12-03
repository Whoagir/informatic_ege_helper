def alg( n ):
  s = f"{n:b}"
  if n % 2 == 0:
    s = '1' + s + '11'
  else:
    s = '11' + s + '0'
  return int(s, 2)

count = 0
res = set()
for n in range(1000):
  if 500 <= alg(n) <= 1000:
    count += 1
    res.add( alg(n) )

print( count )
print( len(res) )