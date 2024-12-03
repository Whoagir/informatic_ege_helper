def F( s ):
  while '5555' in s:
    s = s.replace('5555', '8', 1)
    s = s.replace('88', '5', 1)
  return s

d = {}
for n in range(501,2000):
  s = '5'*n
  r = F(s)
  c = r.count('5')
  if not c in d:
    d[c] = (n, r)

for k in sorted(d, reverse=True):
  print( f"{k}: {d[k]}" )
