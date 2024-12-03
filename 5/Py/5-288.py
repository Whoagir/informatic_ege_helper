def alg( n ):
  s = f"{n:b}"
  if n % 2 == 0:
    s = '1' + s + '10'
  else:
    s = '11' + s + '0'
  return int(s, 2)

count = 0
res = set()
for n in range(1000):
  if 800 <= alg(n) <= 1500:
    count += 1
    res.add( alg(n) )

print( count )
print( len(res) )