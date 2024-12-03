N = 1000
v = set()
for n in range(2,N):
  s = '8'*n
  while '555' in s or '888' in s:
    s = s.replace('555', '8', 1)
    s = s.replace('888', '55', 1)
  v.add( s )

print( len(v), v )
