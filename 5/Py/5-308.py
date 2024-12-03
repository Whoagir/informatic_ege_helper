def alg( n ):
  s = f"{n:b}"
  even = s.count('1') % 2 == 0
  invS = "".join( ('0' if c == '1' else '1') for c in s )
  if even:
    s = s[:-4] + invS[-4:]
  else:
    s = s[:-5] + invS[-5:-1] + s[-1]
  return int( s, 2 )

rr = set()
for n in range(64, 1000):
  rr.add( (alg(n), n) )

print( min(rr) )
