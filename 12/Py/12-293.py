def F( s ):
  while '55555' in s:
    s = s.replace('55555', '88', 1)
    s = s.replace('888', '555', 1)
  return s

d = {}
for n in range(201,2000):
  s = '5'*n
  r = F(s)
  c = r.count('5')
  if not c in d:
    d[c] = (n, r)

for k in sorted(d, reverse=True):
  print( f"{k}: {d[k]}" )
