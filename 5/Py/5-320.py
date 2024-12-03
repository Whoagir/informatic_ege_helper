def tri( n ):
  s = ''
  while n:
    s = str(n%3) + s
    n //= 3
  return s

def alg( n ):
  s = tri(n)
  if n % 2 == 0:
    s += s[-2:]
  else:
    s += tri( sum(map(int, s)) )
  return int(s, 3)

rMin = 10**10
for n in range(10,1000):
  r = alg(n)
  if r < rMin:
    rMin = r
    print( n, rMin )
