def f( s ):
  while'111' in s or '333' in s:
    if '111' in s:
      s = s.replace('111', '3')
    else:
      s = s.replace('333', '1')
  return int(s)

res = {}
for n in range(101,1000):
  r = f( n*'3' )
  if r not in res:
    res[r] = n

print( res[min(res.keys())] )


