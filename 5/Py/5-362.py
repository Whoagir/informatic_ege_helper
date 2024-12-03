def alg( n ):
  s = f"{n:b}"
  if '0' not in s: return 0
  p = s.rfind('0')
  s = s[:p] + s[:2] + s[p+1:]
  return int( s[::-1], 2 )

print( [x for x in range(1,100) if alg(x) == 123][0] )

