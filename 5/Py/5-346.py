Rmax = 0
for n in range(1000, 10000):
  s = f'{n:o}'
  for _ in range(2):
    [s:=s.replace(c,'1') for c in '0246']
    s += str(n%8)
  R = int(s,8)
  if R % 234 == 0:
    Rmax = max( R, Rmax )

print( Rmax )